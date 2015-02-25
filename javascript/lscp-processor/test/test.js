var assert = require('assert');
var ccpo = require('../parsecsv.js').createCallsProcessedObject;
var scpm = require('../parsecsv.js').storeCallsProcessedToMongo;
var MongoClient = require('mongodb').MongoClient;

var options = {
  mongodb: true,
  fieldFormat: [
    { name: 'processingStart', type: 'Date', zone: '+0000' },
    { name: 'processingEnd', type: 'Date', zone: '+0000' },
    { name: 'callStartTime', type: 'Date', zone: '+0000' },
    { name: 'elsProcessingStart', type: 'Date', zone: '+0000' },
    { name: 'elsProcessingEnd', type: 'Date', zone: '+0000' },
    { name: 'elsProcessingEnd', type: 'Date', zone: '+0000' },
    { name: 'processingTimeSec', type: 'Number' },
    { name: 'elsProcessingTimeSec', type: 'Number' },
    { name: 'accountId', type: 'Number' },
    { name: 'index', type: 'Number' },
    { name: 'callDuration', type: 'Number' },
    { name: '_id', type: 'Number' },
  ]
};

describe('LSCP Parser', function () {
  it('should define ccpo as a function', function () {
    assert.equal(typeof ccpo, 'function');
  });
  it('should create an array with 30 elements', function (done) {
    var csvPath = 'test/ECPwiththirtyelements.csv';
    console.log('Processing file:', csvPath);
    ccpo(csvPath, options, function (callsProcessedObjects) {
      assert.equal(callsProcessedObjects.length, 30);
      done();
    });
  });
});

describe('MongoDB data store Tests.', function () {
  var ecpOne = 'test/ECPwiththirtyelements.csv';
  var ecpTwo = 'test/ECPwithconflict.csv';
  var scores;
  var weirdScores;
  var mongodb;
  //var lcpOne = '';
  //var lcpTwo = '';
  beforeEach(function (done) {
    var objectsCreated = 0;
    var droppedDb = false;
    var connectedToDb = false;
    var isProcessingFinished = function () {
      if (droppedDb && connectedToDb) {
        done();
      }
    };
    MongoClient.connect('mongodb://localhost/test', function (err, db) {
      if (err) throw err;
      connectedToDb = true;
      mongodb = db;
      scores = mongodb.collection('scores');
      weirdScores = mongodb.collection('weirdScores');
      mongodb.dropDatabase(function (err, result) {
        droppedDb = true;
        isProcessingFinished();
      });
      isProcessingFinished();
    });
  });
  it('should store the 30 elements contained in ' + ecpOne + '.', function (done) {
    var afterInsert = function () {
      scores.count(function (err, count) {
        assert.equal(30, count);
        return done();
      });
    };
    scpm(ecpOne, mongodb, afterInsert);
  });
  it('should not store objects contained in' + ecpOne + ' twice.', function (done) {
    var insertCount = 0;
    var afterInsert = function () {
      ++insertCount;
      if (insertCount === 2) {
        scores.count(function (err, count) {
          assert.equal(30, count);
          return done();
        });
      }
    };
    scpm(ecpOne, mongodb, afterInsert);
    scpm(ecpOne, mongodb, afterInsert);
  });
  it('should store a record in weirdScores.', function (done) {
    var afterInsert = function () {
      weirdScores.count(function (err, count) {
        if (err) throw err;
        assert.equal(1, count);
        return done();
      });
    };
    scpm(ecpTwo, mongodb, afterInsert);
  });
});
