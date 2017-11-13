fs
==

Модуль для работы с файлами

.. code-block:: js

    const fs = require('fs');


readFileSync
------------

.. js:function:: readFileSync(file_path)

    Возвращает строку, содержимое файла

    .. code-block:: js

        let content = fs.readFileSync('./index.html');
        let content = fs.readFileSync(__dirname + '/index.html');