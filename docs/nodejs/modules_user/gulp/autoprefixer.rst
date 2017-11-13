gulp-autoprefixer
=================

https://github.com/postcss/autoprefixer

Добавляет префиксы для браузеров

.. code-block:: sh

    npm i gulp-autoprefixer

.. code-block:: js

    const gulp = require('gulp');
    const autoprefixer = require('gulp-autoprefixer');

    gulp.task('default', () =>
        gulp.src('src/app.css')
            .pipe(autoprefixer({
                browsers: ['last 2 versions'],
                cascade: false
            }))
            .pipe(gulp.dest('dist'))
    );