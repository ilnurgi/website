browser-sync
============

https://browsersync.io/docs/gulp

.. code-block:: sh

    npm install browser-sync

.. code-block:: js

    const browserSync = require("browser-sync");


create
------

.. js:function:: create([name])

    Возвращает инстанс сервера :js:class:`BrowserSync`

    .. code-block:: js

        const bs = browserSync();

        const bs = browserSync("MyServer");


get
---

.. js:function:: get(name)

    Возвращает инстанс готово сервера :js:class:`BrowserSync`

    .. code-block:: js

        const bs = browserSync("MyServer");


has
---

.. js:function:: has(name)

    Проверяет, существует ли сервер с данным именем

    .. code-block:: js

        browserSync.has("MyServer");


BrowserSync
-----------

.. js:class:: BrowserSync()

    Объект сервера

    .. code-block:: js

        const bs = require("browser-sync").create();

    .. js:function:: init(config, cb)

        Инициализирует сервер

        * cb - обработчик

        * config - объект, параметры сервера

            * server - объект, по умолчанию false

                * baseDir - родительская папка

        .. code-block:: js

            bs.init({
                server: {
                    baseDir: "/app"
                }
            });

    .. js:function:: reload(options)

        Перезагружает сервер и браузер

        * options

            * stream

        .. code-block:: js

            bs.reload({
                stream: false
            });