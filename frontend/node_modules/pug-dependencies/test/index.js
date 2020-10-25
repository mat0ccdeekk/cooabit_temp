var test = require('tape');
var path = require('path');

var PugDependencies = require('../index.js'),
    baseDir = 'test/fixtures';

var plugin = function(file) {
    return new PugDependencies(file);
};

test('Length of dependencies should be 2', function(t) {
  var pugDependencies = plugin('test/fixtures/index.pug');
  var expectedResult = [
    path.join(baseDir, 'extends', 'extends.pug'),
    path.join(baseDir, 'include', 'include1.pug')
  ];
  t.deepEqual(pugDependencies, expectedResult, 'Array of dependencies with a length of 2 should be returnd.');
  t.end();
});
