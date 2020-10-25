This is fork of [Juanfran's](https://github.com/juanfran) [gulp-jade-inheritance](https://github.com/juanfran/gulp-jade-inheritance) gulp-plugin migrated to new Pug parser (former Jade) and added some new features.

---
#gulp-pug-inheritance
[![Build Status](https://travis-ci.org/pure180/gulp-pug-inheritance.svg?branch=master)](https://travis-ci.org/pure180/gulp-pug-inheritance)
[![Dependency Status](https://david-dm.org/pure180/gulp-jade-inheritance.svg)](https://david-dm.org/pure180/gulp-jade-inheritance)
> Rebuild a pug file with other files that have extended or included those file

Inspired by [pug-inheritance](https://github.com/adammockor/pug-inheritance)

## Table of contents

* [Install](#install)
* [Usage](#usage)
* [Large Pug-Applikation](#large-pug-applikation)
* [Only process changed files](#only-process-changed-files)
* [Options / Defaults](#options--defaults)
* [jade >= 1.11](#jade--111)

## Install

```shell
npm install gulp-pug-inheritance@1.0.0-rc.5 --save-dev
```

## Usage

`gulpfile.js`
```js
var pugInheritance = require('gulp-pug-inheritance');
var pug = require('gulp-pug');

gulp.task('pug-inheritance', function() {
  gulp.src('/pug/example.pug')
    .pipe(pugInheritance({basedir: '/pug/'}))
    .pipe(pug());
});
```

In this example pug compile `example.pug` and all other files that have been extended or included `example.pug`. The plugin searches for those dependencies in the `basedir` directory.

## Large Pug-Applikation

Through experience with larger Pug-Applikation, building in approximately +100 \*.pug files, the used Pug-Walk in [pug-inheritance](https://github.com/adammockor/pug-inheritance) takes a lot of time to retrieve the whole inheritance tree for each file. Therefore, as of version `^1.0.0`, you can use a temporary file to save the whole inheritance tree now. This file will be created at the first run of your applikation and used on all upcoming starts. To use this feature you will need set the `saveInTempFile` option to `true`. In other words this feature is set to `false` by default.

```js
gulp.task('pug', function() {
  return gulp.src('app/**/*.pug')
  // ...
  .pipe(pugInheritance({
    saveInTempFile: true
  }))
  // ...
  .pipe(pug())
  .pipe(gulp.dest('dist'));
});
```

### Only process changed files

You can use `gulp-pug-inheritance` with `gulp-changed` and `gulp-cached` to only process the files that have changed. This also prevent partials from being processed separately by marking them with an underscore before their name.

```js
'use strict';
var gulp = require('gulp');
var pugInheritance = require('gulp-pug-inheritance');
var pug = require('gulp-pug');
var changed = require('gulp-changed');
var cached = require('gulp-cached');
var gulpif = require('gulp-if');
var filter = require('gulp-filter');

gulp.task('pug', function() {
    return gulp.src('app/**/*.pug')

        //only pass unchanged *main* files and *all* the partials
        .pipe(changed('dist', {extension: '.html'}))

        //filter out unchanged partials, but it only works when watching
        .pipe(gulpif(global.isWatching, cached('pug')))

        //find files that depend on the files that have changed
        .pipe(pugInheritance({basedir: 'app'}))

        //filter out partials (folders and files starting with "_" )
        .pipe(filter(function (file) {
            return !/\/_/.test(file.path) && !/^_/.test(file.relative);
        }))

        //process pug templates
        .pipe(pug())

        //save all the files
        .pipe(gulp.dest('dist'));
});
gulp.task('setWatch', function() {
    global.isWatching = true;
});
gulp.task('watch', ['setWatch', 'pug'], function() {
    //your watch functions...
});
```

If you want to prevent partials from being processed, mark them with an underscore before their name or their parent folder's name. Example structure:

```
/app/index.pug
/app/_header.pug
/app/_partials/article.pug
/dist/
```

To install all that's need for it:

```shell
npm install gulp-pug-inheritance@1.0.0-rc gulp-pug gulp-changed gulp-cached gulp-if gulp-filter --save-dev
```
You can find a working example in this test repository: [gulp-pug-inheritance-test](https://github.com/pure180/gulp-pug-inheritance-test).

## Options / Defaults
These are the default options, you can override them in your pug-task:
```js
GulpPugInheritance.prototype.DEFAULTS = {
  basedir :         process.cwd(),
  extension:        '.pug',
  skip:             'node_modules',
  saveInTempFile:   false,
  tempFile:         'temp.pugInheritance.json'
};
```
### Overview of all options
| Option | Type | Default | Description |
| ------ | ---- | ------- | ----------- |
| `basedir` | `string` | `./` | Defines the root, from where pug-inheritance starts to scan for all *.pug files in all existing folders within the basedir. |
| `extension` | `string` | `.pug` | Defines the used file extension. This option was integrated because of the conversion of Jade to Pug. If you allready use `*.pug` as file extension you can leave this option aside, but if you still use `*.jade` you need to set this option. |
| `skip` | `string` or `array` | `'node_modules'` | If you are using the root folder  `options.basedir = '.'` to process your *.pug files, you have to skip node_modules. Because of dependant PUG-packages which may contain test files, that may cause errors during the compile. This option accepts a string or an array. |
| `saveInTempFile` | `boolean` | `false` | If you want to save the inheritance tree in to a temporary file, you should set this option to `true`. **Recommended for larger build applikations with +50 files.** |
| `tempFile` | `string` | `temp.pugInheritance.json` | Path and name of the file for the temporary inheritance tree. |
| `debug` | `boolean` | `false` | Enable logs to displays them in Terminal. |


### jade >= 1.11

if your using jade 1.11 add `"jade": "^1.11.0"` to your `package.json` to overwrite the jade-inheritance version. [Issue](https://github.com/paulyoung/jade-inheritance/issues/15)
