var csvparser = require('csv-parse');
var fs = require('fs');
var camelCase = require('camel-case');
var filesdir = process.argv[2];

function formatFields(fieldFormat, data) {
  for (var i in fieldFormat) {
    var field = fieldFormat[i].name;
    switch(fieldFormat[i].type) {
      case 'Number':
        if (!data[field]) break;
        data[field] = +data[field];
        break;
      case 'Date':
        if (!data[field]) break;
        var zone = fieldFormat[i].zone;
        data[field] = new Date(data[field] + zone);
        break;
    }
  }
}

function callsProcessedJson(csvFilePath, options, callback) {
  var opts = options || {};
  var callback = arguments[arguments.length-1];
  var start;
  var parser = csvparser({ columns: true, relax: true });
  var result = [];
  start = Date.now();
  fs.createReadStream(csvFilePath).pipe(parser);
  parser.on('data', function (data) {
    for (var key in data) {
      // Note: Always a string... if empty ignore, keep the database clean
      // of empty attributes.
      if (!!data[key]) {
        data[camelCase(key)] = data[key];
      }
      delete data[key];
    }
    if (data.callId && opts.mongodb) {
      data._id = data.callId;
      delete data.callId;
    }
    if (opts.fieldFormat) {
      formatFields(opts.fieldFormat, data);
    }
    result.push(data);
  });
  parser.on('end', function () {
    console.log('finished @', (Date.now()-start) / 1000, 'sec/s');
    console.log('data size:', result.length);
    callback(result);
  });
}

function isEnhancedCallProcessed(data) {
  return !!data['elsScorerName'];
}

function storeCallsProcessed(pathToCsv, finished) {
  var MongoClient = require('mongodb').MongoClient;
  MongoClient.connect('mongodb://localhost/test', function (err, db) {
    if (err) {
      console.log('Database connection error.');
    }
    var upsertedScores = 0;
    var updateDbRecords = function (indx, scores) {
      var selector = { _id: scores[indx]._id };
      var opts = { upsert: true };
      var updated = function (err, data) {
        upsertedScores++;
        if (err) {
          console.log(err.message);
          console.log('Record already uploaded...')
        }
        if (upsertedScores === scores.length) {
          console.log('ELS file successfully uploaded!');
          return db.close();
        }
      };
      db.collection('score').update(selector, scores[indx], opts, updated);
    };
    var insertScores = function (scores) {
      if (scores.length < 1) {
        console.log('Nothing to process...', pathToCsv);
        db.close();
        return;
      }
      db.collection('score').insert(scores, function (err, data) {
        console.log('Processing file:', pathToCsv);
        if (err) {
          console.error(err.code);
          var DUP_CODE = 11000
          if (err.code === DUP_CODE) {
            var insertData = err.toJSON().op;
            if (isEnhancedCallProcessed(insertData)) {
              for (var i = 0; i < scores.length; i++) {
                updateDbRecords(i, scores);
              }
            } else {
              console.log('Scores already uploaded!');
              db.close();
            }
          } else {
            console.log('Closing db...', err.message);
            db.close();
          }
        } else {
          console.log('inserted @', (Date.now()-start) / 1000, 'sec/s');
          db.close();
        }
      });
    };
    var start = Date.now();
    var options = {
      mongodb: true,
      fieldFormat: [
        { name: 'processingStart', type: 'Date', zone: '+0000' },
        { name: 'processingEnd', type: 'Date', zone: '+0000' },
        { name: 'callStartTime', type: 'Date', zone: '+0000' },
        { name: 'processingTimeSec', type: 'Number' },
        { name: 'accountId', type: 'Number' },
        { name: 'index', type: 'Number' },
        { name: 'callDuration', type: 'Number' },
        { name: '_id', type: 'Number' },
      ]
    }
    //db.collection('score').drop(function() {
      var scores = callsProcessedJson(pathToCsv, options, insertScores);
    //});
  });
}

(function () {
  //var dir = '/home/irvin/Documents/callsprocessed/othersources/January 2015/';
  //fs.readdir(dir, function (err, files) {
    //for (var i = 0; i < files.length; i++) {
      //storeCallsProcessed(dir + files[i]);
    //}
  //});
  var file = process.argv[2];
  storeCallsProcessed(file);
})();
