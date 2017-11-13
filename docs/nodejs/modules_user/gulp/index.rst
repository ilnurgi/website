gulp
====

https://gulpjs.com/

Сборщик проектов

В рабочей директории создать файл gulpfile.js

.. code-block:: sh

    # установка
    npm i -g gulp-cli

    # запуск сборщика, задачи берет из gulpfile.js и выполняет таск default
    gulp

    # запустить конкретный таск
    gulp test


.. code-block:: js

    // gulpfile.js

    const gulp = require('gulp');

    gulp.task('default', function(){
        console.log('hello world');
    });

    gulp.task('test', function(){
        console.log('hello world');
    });

.. code-block:: js

    const gulp = require('gulp');
    const autoprefixer = require('gulp-autoprefixer');
    const cleanCSS = require('gulp-clean-css');
    const browserSync = require('browser-sync').create();
    const sourcemaps = require('gulp-sourcemaps');

    const config = {
        src: './src',
        css: {
            watch: '/precss/**/*.css',
            src: '/precss/project.css',
            dest: '/css'
        }
        html: {
            src: 'index.html'
        }
    };

    gulp.task('build', function(){
        gulp.src(config.src + config.css.src)
            .pipe(sourcemaps.init())
            .pipe(autoprefixer({
                browsers: ['last 2 versions'],
                cascade: false
            }))
            .pipe(cleanCSS())
            .pipe(sourcemaps.write('.'))
            .pipe(gulp.dest(config.src + config.css.dest))
            .pipe(browserSync.reload({
                stream: true
            }));
    });

    gulp.task('watch', ['browserSync'], function(){
        gulp.watch(config.src + config.css.watch, ['build']);
    });

    gulp.task('browserSync', function(){
        browserSync.init({
            server: {
                baseDir: config.src
            }
        });
    });

dest
---

.. js:function:: dest(path[, options])

    Копирует файлы в указанную папку

    * path - строка или функция, путь назначения

    * options - объект параметры

        * cwd - строка, рабочая директория

        * mode - число, права на файл

    .. code-block:: js

        gulp.src('./src/precss/**/*.css')
            .pipe(gulp.dest('./src/'));

        gulp.src('./client/templates/*.jade')
            .pipe(jade())
            .pipe(gulp.dest('./build/templates'))
            .pipe(minify())
            .pipe(gulp.dest('./build/minified_templates'));


src
---

.. js:function:: src(globs[, options])

    Возвращает поток объектов, которые можно обработать через pipe

    * globs - строка или список строк, путь для чтения

    * options - объект параметры

        * base - строка, базовая директория

        * buffer - булево, по умолчанию истина, буферизованное чтение

        * read - булево, по умолчанию истина, читать содержимое

    .. code-block:: js

        gulp.src('./src/precss/*.css');

        gulp.src(['client/*.js', '!client/b*.js', 'client/bad.js']);

        gulp.src('./src/precss/**/*.css')
            .pipe(gulp.dest('./src/'));

    .. code-block:: js

        // базовая папка будет client/js
        // и все запишется в папку build/
        gulp.src('client/js/**/*.js')
            .pipe(gulp.dest('build'));

        // задаем базовую папку client
        // и все запишется в папку build/js
        gulp.src('client/js/**/*.js', { base: 'client' })
            .pipe(gulp.dest('build'));


pipe
----

Обрабатывает поток данных

.. code-block:: js

    gulp.src('./src/precss/**/*.css')
        .pipe(gulp.dest('./src/'));


task
----

.. js:function:: task(name[, deps][, fn])

    Создает задачу

    По умолчнаию запускается задача default

    * name - название задачи

    * deps - список задач, зависимостей, которые должны быть выполнены перед этой задачей.
        Задачи выполнятся асинхронно.

    .. code-block:: js

        // эта задача запускается при вызове gulp
        gulp.task('default', function(){
            console.log('hello world');
        });

        // эта задача запускается при вызове gulp test
        gulp.task('test', function(){
            console.log('hello world');
        });

        gulp.task('default', ['task1', 'task2'], function(){
            console.log('hello world');
        });

        gulp.task('build', ['task1', 'task2']);


watch
-----

.. js:function:: watch(glob[, opts], tasks)
.. js:function:: watch(glob[, opts, cb])

    Следит за файлами и что-то делает при их изменении

    * glob - строка или массив, путь к папке слежения

    * opts - объект, параметры

    * tasks - список задач, которые необходимо выыполнить

    * cb - обработчик каждого изменения

    .. code-block:: js

        var watcher = gulp.watch('js/**/*.js', ['uglify','reload']);

        watcher.on('change', function(event) {
            console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
        });

    .. code-block:: js

        gulp.watch('js/**/*.js', function(event) {
            console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
        });


.. toctree::
    :maxdepth: 2

    autoprefixer
    browser_sync
    clean_css
    less
    less