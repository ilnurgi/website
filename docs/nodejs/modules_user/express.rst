express
=======

.. code-block:: sh

    npm install express

.. code-block:: js

    const express = require('express');
    const app = express();

express
-------

.. js:function:: express()

    Возвращает оъект сервера :js:class:`Server`

    .. code-block:: js

        const app = express();


static
------

.. js:function:: static()

    .. code-block:: js

        express.static('static');


Server
------

.. js:class:: Server()

    Объект сервера


    .. js:function:: get(route, callback)

        Задает обработчик для маршрута/урла

        .. code-block:: js

            app.get('/', (req, res) => {
                res.sendFile('index.html');
            });

        .. code-block:: js

            let context = {
                content: "Hello World"
            };

            app.get('/', (req, res) => {
                res.render('index', context);
            });


    .. js:function:: listen(port[, host[, callback]])

        Запускает сервер по указанным параметрам

        ..  code-block:: js

            app.listen(8000);
            app.listen(8000, () => console.log("Server started"));


    .. js:function:: set(key, value)

        Задает значения для параметров

        .. code-block:: js

            // задаем шаблонизатор для рендеринга
            app.set("view engine", "ejs");


    .. js:function:: use()

        .. code-block:: js

            import apiRouter from './apiRouter';

            app.use(express.static('static'));
            app.use('/api', apiRouter);


Router
------

.. js:class:: Router()

    .. code-block:: js

        const router = express.Router();

    .. js:function:: get(url, callback)

        .. code-block:: js

            router.get('/', (req, res) => {
                res.send("Hello World");
            });

            router.get('/books/:bookId', (req, res) =>{
                // req.params.bookId
            });
