Теги, описывающие документ
==========================


body
----

Тело документа, должно находиться внутри корневого элемента html

.. code-block:: html
   
    <!DOCTYPE>

    <html>

       <head>
           ...
       </head>

       <body></body>

    </html>


head
----

Содержит информацию о документе и должно находиться внутри корневого элемента html

.. code-block:: html
   
    <!DOCTYPE>

    <html>

       <head>
           ...
       </head>

       <body></body>

    </html>


html
----

Корневой элемент

* manifest - ссылка на кеш память

* lang -

.. code-block:: html
   
    <!DOCTYPE>

    <html>

       <head>
           ...
       </head>

       <body></body>

    </html>


link
----

Ссылка на различные доп файлы документа.

Должен находится внутри тега head

* href - ссылка на файл

* media - тип медиа документа

    * all - все устройства
    * aural
    * braille - устройства с тактильной обратной связью
    * handled - портативные устройства
    * print - режим вывода на печать
    * projection - проекторы
    * screen - цветные компьютерные экраны
    * tty - моноширинная символьная сетка
    * tv - телевизоры
    * orientation - ориентация экрана
    * (min/max)-width - ширина области просмотра
    * (min/max)-height - высота области просмотра
    * (min/max)-aspect-ratio - соотношение сторон области просмотра
    * (min/max)-device-width - ширина экрана
    * (min/max)-device-height - высота экрана
    * (min/max)-device-aspect-ratio - соотношение сторон экрана

* rel - отношение к актуальному документу

    * alternate - альтернативная версия документа
    * contents - оглавление документа или сайта
    * copyright - авторские права
    * glossary - термины
    * help - справочный документ
    * icon - иконка страницы
    * index - индекс документа
    * next - ссылка на следующий документ
    * prev - ссылка на предыдущую страницу
    * stylesheet - стили

* hreflang - язык медиаинформации

* sizes - размер пиктограммы

.. code-block:: html

    <link rel="stylesheet" media="screen and (max-width: 960px)" />


meta
----

Мета информация

Должен находиться внутри тега head

.. code-block:: html

    <head>
        <meta charset="utf-8"/>
    <head>


charset
+++++++

Кодировка документа

.. code-block:: html

    <meta charset="utf-8"/>


description
+++++++++++

Описание документа

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

Ключевые слова документа

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

script
------

Скрипты документа


style
-----

Стили документа


title
-----

Заголовок страницы

Должен находиться внутри тега head

.. code-block:: html

    <head>
        <title>Заголовок страницы</title>
    </head>