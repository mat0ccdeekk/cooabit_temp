var pluginPath = '../index';
var plugin = require(pluginPath);
var chai = require('chai');
var path = require('path');
var expect = chai.expect;
var gutil = require('gulp-util');
var fs = require('fs');

var getFixtureFile = function (path) {
  return new gutil.File({
    path: './test/fixtures/' + path,
    cwd: './test/',
    base: './test/fixtures/',
    contents: fs.readFileSync('./test/fixtures/' + path)
  });
};

describe('gulp-pug-inheritance', function(done) {
  it('pug with parents', function(done) {
    var fixture = getFixtureFile('fixture1.pug');

    var fileNames = [
      path.join('test', 'fixtures', 'fixture1.pug'),
      path.join('test', 'fixtures', 'fixture2.pug'),
      path.join('test', 'fixtures', 'fixture3.pug'),
    ];

    var files = [];

    var stream = plugin();
    stream
      .on('data', function (file) {
        expect(fileNames).to.include(file.relative);

        files.push(file);
      })
      .once('end', function() {
        expect(files).to.have.length(3);

        done();
      });

    stream.write(fixture);
    stream.end();
  });

  it('pug without parents', function(done) {
    var fixture = getFixtureFile('fixture4.pug');

    var files = [];

    var stream = plugin({extension: '.pug'});
    stream
      .on('data', function (file) {
        files.push(file);
      })
      .once('end', function() {
        expect(files).to.have.length(1);

        done();
      });

    stream.write(fixture);
    stream.end();
  });

  it('empty pug', function(done) {
    var fixture = getFixtureFile('fixture5.pug');

    var files = [];

    var stream = plugin({extension: '.pug'});
    stream
      .on('data', function (file) {
        files.push(file);
      })
      .once('end', function() {
        expect(files).to.have.length(0);

        done();
      });

    stream.write(fixture);
    stream.end();
  });

  it('subfolder pug', function(done) {
    var fixture = getFixtureFile('subfolder/fixture5.pug');

    var files = [];

    var stream = plugin({basedir: 'test/fixtures', extension: '.pug'});
    stream
      .on('data', function (file) {
        expect(file.base).to.be.eql('test/fixtures');
        files.push(file);
      })
      .once('end', function() {
        expect(files).to.have.length(1);

        done();
      });

    stream.write(fixture);
    stream.end();
  });

  describe('custom basedir', function(done) {
    it('wrong path', function(done) {
      var fixture = getFixtureFile('fixture1.pug');

      var files = [];

      var stream = plugin({basedir: 'test/fixtures5', extension: '.pug'});
      stream
        .on('data', function (file) {
          files.push(file);
        })
        .once('end', function() {
          expect(files).to.have.length(1);

          done();
        });

      stream.write(fixture);
      stream.end();
    });

    it('valid path', function(done) {
      var fixture = getFixtureFile('fixture1.pug');

      var files = [];

      var stream = plugin({basedir: 'test/fixtures', extension: '.pug'});
      stream
        .on('data', function (file) {
          files.push(file);
        })
        .once('end', function() {
          expect(files).to.have.length(3);

          done();
        });

      stream.write(fixture);
      stream.end();
    });
  });

  describe('Use temporary file', function(done) {
    it('Save inheritance to temporary file as object', function(done){
      var fixtureName = 'fixture1.pug';
      var fixture = getFixtureFile(fixtureName);

      var fileNames = [
        path.join('test', 'fixtures', 'fixture1.pug'),
        path.join('test', 'fixtures', 'fixture2.pug'),
        path.join('test', 'fixtures', 'fixture3.pug'),
      ];

      var temporaryFile = path.join(process.cwd(), 'temp.pugInheritance.json');
      var temporaryKey  = 'fixture1.pug'.replace( /\/|\\|\\\\|\-|\.|\:/g, '_' );
      var files = [];

      var stream = plugin({basedir: 'test/fixtures', saveInTempFile: true});

      stream
        .on('data', function (file) {
          files.push(file);
        })
        .once('end', function() {
          expect(files).to.have.length(3);

          if (fs.existsSync( temporaryFile )) {
            var inheritance = require( temporaryFile );
            expect(inheritance).to.be.a('object');
            expect(inheritance[temporaryKey].files).to.have.length(files.length);
          }
          done();
          if (fs.existsSync( temporaryFile )) {
            fs.unlinkSync(temporaryFile);
          }
        });

      stream.write(fixture);
      stream.end();
    });
  });
});
