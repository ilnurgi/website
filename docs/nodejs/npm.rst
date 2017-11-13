npm
===

Пакетный менеджер node.js

.. code-block:: js

    // package.json
    // настройки проекта, создается через init, обрабатывается через up


access
------


adduser
-------


bin
---


bugs
----


c
-


cache
-----


completion
----------


config
------


ddp
---


dedupe
------


deprecate
---------


dist-tag
--------


docs
----


edit
----


explore
-------


get
---


help
----


help-search
-----------


i
-

Установить  пакет

* -g - выполнить команду глобально, иначе для указанной папки

* --save - добавить в зависиомсти package.json

* --save-dep - добавить в зависимости разработки package.json

.. code-block:: sh

    # глобальная установка
    npm i -g gulp-cli

    # локальная установка
    npm i gulp


init
----

Инициализирует package.json

.. code-block:: js

    // package.json
    {
        "name": "19870128",
        "version": "1.0.0",
        "main": "gulpfile.js",
        "dependencies": {
            "gulp": "^3.9.1"
        },
        "devDependencies": {},
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "author": "",
        "license": "ISC",
        "description": ""
    }


install
-------


install-test
------------


it
--


link
----


list
----


ln
--


login
-----


logout
------


ls
--

Список установленных пакетов

* -g - выполнить команду глобально, иначе для указанной папки

* --depth - глубина

.. code-block:: sh

    npm ls -g --depth 0
    -- phonegap@10.0.0


outdated
--------


owner
-----


pack
----


ping
----


prefix
------


prune
-----


publish
-------


r
-

Удалить пакет

* -g - выполнить команду глобально, иначе для указанной папки

.. code-block:: sh

    npm r  -g gulp-cli


rb
--


rebuild
-------


repo
----


restart
-------

root
----


run
---


run-script
----------


s
-

Поиск пакета

.. code-block:: sh

    npm s


se
--


search
------


set
---


shrinkwrap
----------


star
----


stars
-----


start
-----


stop
----


t
-


tag
---


team
----


test
----


tst
---


un
--


uninstall
---------


unpublish
---------


unstar
------


up
--

Создает окружение для проекта по package.json файлу

.. code-block:: sh

    npm up

update
------


v
-


version
-------


view
----


whoami
------

