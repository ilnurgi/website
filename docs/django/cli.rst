Консольные команды
==================

.. code-block:: sh

    # создание проекта
    django-admin startproject mysite

.. code-block:: sh

    # создание приложения
    django-admin startapp blog

.. code-block:: sh

    # миграция БД
    python manage.py migrate

.. code-block:: sh

    # создание миграции БД
    python manage.py makemigrations app_name

    python manage.py makemigrations shop --name "add_translation_model"

.. code-block:: sh

    # просмотр sql миграции БД
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

.. code-block:: sh

    # запуск сервера для разработки
    python manage.py runserver

    python manage.py runserver --settings mysite.settings

.. code-block:: sh

    # создание суперпользователя
    python manage.py createsuperuser

.. code-block:: sh

    # создать файлы локализации
    python manage.py makemessages

    # скомпилировать файлы локализации
    python manage.py compilemessages