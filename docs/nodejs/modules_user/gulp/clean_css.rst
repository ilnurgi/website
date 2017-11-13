clean_css
=========

https://www.npmjs.com/package/gulp-clean-css

Очищает css от пробелов

.. code-block:: sh

    npm install gulp-clean-css

cleanCSS
--------

.. js:function:: cleanCSS([options][, callback])

    .. code-block:: js

        const gulp = require('gulp');
        const cleanCSS = require('gulp-clean-css');

        gulp.task('minify-css', () => {
            gulp.src('styles/*.css')
                .pipe(cleanCSS({
                    compatibility: 'ie8',
                    // уровень сжатия
                    level: 2
                }))
                .pipe(gulp.dest('dist'));
        });

    .. code-block:: js

        const gulp = require('gulp');
        const cleanCSS = require('gulp-clean-css');

        gulp.task('minify-css', () => {
            gulp.src('styles/*.css')
                .pipe(cleanCSS({debug: true}, function(details) {
                    console.log(details.name + ': ' + details.stats.originalSize);
                    console.log(details.name + ': ' + details.stats.minifiedSize);
                }))
                .pipe(gulp.dest('dist'));
        });