a
=

Якорь, гипертекстовая ссылка

Строчный элемент

.. code-block:: html

    <a>текст ссылки</a>

.. code-block:: html

    <a href="http:/ilnurgi.ru" id="my_anchor"></a>
    <a href="http:/ilnurgi.ru/post.html#news"></a>
    <a href="mailto:ilnurgi87@gmail.com"></a>
    <a href="tel:+1234567890"></a>

.. code-block:: html

    <a id="anchor_bottom"></a>
    <a href="#anchor_bottom"></a>


download
--------

Данная ссылка будет открыта не в новом окне, а будет скачана браузером.

.. note:: HTML5.1

.. code-block:: html

    <a href="img.png" download>Картинка</a>


href
----

Адрес ресурса, куда ведет ссылка

.. code-block:: html

    <a href="http://ilnurgi1.ru">ilnurgi1.ru</a>
    <a href="mailto: mail@mail.rur">Почта</a>
    <a href="tel: +7..">Телефон</a>

.. code-block:: html

    <a href="#name">ilnurgi1.ru</a>

    <div id="name"></div>


hreflang
--------

Язык целевого документа

.. code-block:: html

    <a hreflang='ru'>...</a>


rel
---

Связь между исодным и связанными документами

* alternate
* author
* bookmark
* help
* license
* next
* nofollow
* noreferrer
* prefetch
* prev
* search
* tag


target
------

Имя окна или области iframe, где будет открываться документ

.. code-block:: html

    <a href="http://ilnurgi1.ru" target="_blank">ilnurgi1.ru</a>


title
-----

Добавляет всплывающую подсказу при наведении

.. code-block:: html

    <a href="http://ilnurgi1.ru" title="ссылка на мой проект">ilnurgi1.ru</a>


type
----

Тип контента для связанного контента
