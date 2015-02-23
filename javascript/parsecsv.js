var csvparser = require('csv-parse');
var fs = require('fs');
var camelCase = require('camel-case');

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
      /* Note: Always a string... if empty ignore, keep the database clean
       * of empty attributes.
       */
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
    console.log('finished creating ls records @',
                (Date.now()-start) / 1000, 'sec/s');
    console.log('data size:', result.length);
    callback(result);
  });
}

function isECPScore(data) {
  return !!data['elsScorerName'];
}

function storeCallsProcessed(pathToCsv, finished) {
  var MongoClient = require('mongodb').MongoClient;
  MongoClient.connect('mongodb://localhost/test', function (err, db) {
    if (err) {
      console.log('Database connection error.');
    }
    var executeExitScripts = function() {
      if (finished && typeof(finished) == 'function') finished.call();
      return db.close();
    }
    /* A safer but slower method of inserting scores. */
    var individuallyUpsertScores = function (scores) {
      var upsertedScores = 0;
      var updateDbRecords = function (index, scores) {
        var selector = { _id: scores[index]._id };
        var opts = { upsert: true };
        var update = { $set: scores[index] };
        var updated = function (err, data) {
          upsertedScores++;
          if (err) {
            console.log(err.message);
            if (err.code === 11000) console.log('Record already uploaded...');
          }
          if (upsertedScores === scores.length) {
            console.log('upserted @', (Date.now()-start) / 1000, 'sec/s');
            executeExitScripts();
          }
        };
        db.collection('score').update(selector, update, opts, updated);
      };
      for (var i = 0; i < scores.length; i++) {
        updateDbRecords(i, scores);
      }
    };
    var checkIfUpdatable = function (duplicate, cb) {
      var collection = db.collection('score');
      var selector = { _id: duplicate._id };
      collection.findOne(selector, function (err, doc) {
        if (err) console.log(err);
        cb(!!(isECPScore(doc) ^ isECPScore(duplicate)));
      });
    };
    var insertScores = function (scores) {
      if (scores.length < 1) {
        console.log('Nothing to process...', pathToCsv);
        executeExitScripts();
      }
      db.collection('score').insert(scores, function (err, data) {
        if (err) {
          var DUP_CODE = 11000
          if (err.code === DUP_CODE) {
            console.log('Duplicate found... executing fallback.');
            var duplicate = err.toJSON().op;
            checkIfUpdatable(duplicate, function updateScores(updatable) {
              if (!updatable) {
                console.log('These Scores are already uploaded!');
                console.log('exited @', (Date.now()-start) / 1000, 'sec/s');
                executeExitScripts();
              } else {
                individuallyUpsertScores(scores);
              }
            });
          } else {
            console.log('Closing db...', err.message);
            executeExitScripts();
          }
        } else {
          console.log('inserted @', (Date.now()-start) / 1000, 'sec/s');
          executeExitScripts();
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
      console.log('Processing file:', pathToCsv);
      var scores = callsProcessedJson(pathToCsv, options, insertScores);
    //});
  });
}

(function () {
  var filesdir = process.argv[2];
  fs.readdir(filesdir, function (err, files) {
    for (var i = 0; i < files.length; i++) {
      storeCallsProcessed(filesdir + files[i]);
    }
  });
  //var file = process.argv[2];
  //storeCallsProcessed(file);
})();
