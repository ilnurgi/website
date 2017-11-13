head
====

Содержит информацию о документе и должно находиться внутри корневого элемента html

.. code-block:: html

    <!doctype html>

    <html>

       <head>
           ...
       </head>

    </html>


meta
----

Мета информация

Должен находиться внутри тега head

.. code-block:: html

    <head>
        <meta charset="utf-8"/>
    <head>


author
++++++

Автор контента, для поисковых роботов

.. code-block:: html

    <meta name="author" content="Ильнур">


charset
+++++++

Кодировка документа

.. code-block:: html

    <meta charset="utf-8"/>


description
+++++++++++

Описание документа, используется поисковыми роботами.

.. code-block:: html

    <meta name="description" content="some description" />


format-detection
++++++++++++++++

Автоматическое обнаружение иноформации на странице

* telephone

.. code-block:: html

    <meta name="format-detection" content="telephone=no"/>


keyword
+++++++

Ключевые слова документа, для поисковых роботов.

.. code-block:: html

    <meta name="keyword" content="python, django" />


viewport
++++++++

Задает логические размеры и масштабирование для окна браузера.

Используется для мобильной среды

* width = число или device-width - ширина области просмотра

* height = число или device-height - высота области просмотра

* user-scalable = no или yes - может ли пользователь увеличивать или уменьшать размеры контента

* initial-scale = float число - исходный коэффициент масштабирования

* maximum-scale = float число - максимальный лимит пользовательского увеличения

* minimum-scale = float число - минимальный лимит пользовательского увеличения

.. code-block:: html

    <meta
        name="viewport"
        content="user-scalable=no, width=device-width, initial-scale=1.0" />


style
-----

CSS стили документа

.. code-block:: html

    <head>
        <style>
            body {
                color: red;
            }
        </style>
    </head>


title
-----

Заголовок страницы

Должен находиться внутри тега head

.. code-block:: html

    <head>
        <title>Заголовок страницы</title>
    </head>