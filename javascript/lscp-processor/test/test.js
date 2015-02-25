var assert = require('assert');
var ccpo = require('../parsecsv.js').createCallsProcessedObject

describe('LSCP Parser', function () {
  it('should define ccpo as a function', function () {
    assert.equal(typeof ccpo, 'function');
  });
  it('should create an array with 30 elements', function () {
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
    console.log(process.cwd());
    var csvPath = 'test/ECPwiththirtyelements.csv';
    console.log('Processing file:', csvPath);
    ccpo(csvPath, options, function (callsProcessedObjects) {
      assert.equal(callsProcessedObjects.length, 30);
    });
  });
});
