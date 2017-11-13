pg
==

Модуль  для подключения к СУБД postgres

.. code-block:: sh

    npm install pg

.. code-block:: js

    const pg = require('pg');


Client
------

.. js:class:: Client(config)

    Клиент работы с postgres

    * config - объект параметров

        * database - название базы данных

        * user

        * password

        * host

        * port

        * max

        * idleTimeoutMillis

    .. code-block:: js

        const pg_client = pg.Client({
            database: "db"
        });

    .. js:function:: connect(callback)

        Подключается к субд

        .. code-block:: js

            pg_client.connect(function(err){
                if (err) throw err;

                // pg_client.query(...);
            });


    .. js:function:: end(callback)

        Завершает работу с базой

        .. code-block:: js

            pg_client.end(function(err) {
                if (err) throw err;
            });


    .. js:function:: query(sql, params, callback)

        Выполняет зпрос к базе

        .. code-block:: js

            pg_client.query(
                "select $1::text as name from table",
                ["ilnurgi"],
                function(err, result) {
                    if (err) throw err;

                    console.log(result.rows[0]);

                    pg_client.end(function(err) {
                        if (err) throw err;
                    });
                }
            )


Pool
----

.. js:class:: Pool(config)

    Создает пул соединении

    * config - объект параметров

        * database - название базы данных

        * user

        * password

        * host

        * port

        * max

        * idleTimeoutMillis

    .. code-block:: js

        const pg_pool = pg.Pool();


    .. js:function:: connect(callback)

        Выполняет соединение с базой

        .. code-block:: js

            pg_pool.connect(function(err, client, done){

            });


    .. js:function:: query(sql, params, callback)

        Выполняет запрос к базе

        .. code-block:: js

            pg_pool.query(
                "select $1::text as name from table",
                ["ilnurgi"],
                function(err, result) {
                    if (err) throw err;

                    console.log(result.rows[0]);

                    pg_client.end(function(err) {
                        if (err) throw err;
                    });
                }
            )


    .. js:function:: on(event, callback)

        Задает обработчик события

        .. code-block:: js

            pg_pool.on('error', function(err, client){
            });