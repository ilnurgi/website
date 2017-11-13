Консольные команды
==================


compilemessages
---------------

Скомпилировать файлы локализации

.. code-block:: sh

    python manage.py compilemessages


createsuperuser
---------------

Создать суперпользователя

.. code-block:: sh

    python manage.py createsuperuser


makemessages
------------

Создать файлы локализации

.. code-block:: sh

    python manage.py makemessages


makemigrations
--------------

Создать файлы миграции

* name - название миграции

.. code-block:: sh

    python manage.py makemigrations app_name

    python manage.py makemigrations shop --name "add_translation_model"


migrate
-------

Миграция базы данных

.. code-block:: sh

    python manage.py migrate


runserver
---------

Запуск сервера разработки

* settings - моудль файла настроек

.. code-block:: sh

    python manage.py runserver

    python manage.py runserver --settings mysite.settings


sqlmigration
------------

Выводит sql запросы миграции

.. code-block:: sh

    python manage.py sqlmigration app_name 0001
    """
    BEGIN;
    CREATE TABLE "blog_post" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "title" varchar(250) NOT NULL,
        "slug" varchar(250) NOT NULL,
        "body" text NOT NULL,
        "publish" datetime NOT NULL,
        "created" datetime NOT NULL,
        "updated" datetime NOT NULL,
        "status" varchar(10) NOT NULL,
        "author_id" integer NOT NULL REFERENCES "auth_user" ("id"));
    CREATE INDEX "blog_post_2dbcba41" ON "blog_post" ("slug");
    CREATE INDEX "blog_post_4f331e2f" ON "blog_post" ("author_id");
    COMMIT;
    """


startapp
--------

Создать приложение в проекте

.. code-block:: sh

    django-admin startapp blog


startproject
------------

Создать проект

.. code-block:: sh

    django-admin startproject mysite
