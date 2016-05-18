Конспекты по HTML
=================

.. code-block:: html
   
    <!DOCTYPE>

    <html>

       <head>
           <meta charset="utf-8" />
       </head>

       <body></body>

    </html>
    
.. toctree::
    :maxdepth: 1

    doc
    meta    
    mnemonic
    table
    text
    list
    form


.. toctree::
    :maxdepth: 2

    html5/index


a
-

Якорь, гипертекстовая ссылка, строчный элемент

* download = "имя файла"

    Ссылка для загружаемого ресурса

    .. note:: HTML5.1

* href = "URI"

    Адрес ресурса

* hreflang = "код языка"

    Язык целевого документа

* media = "all | aural | braille | handheld | print | projection | screen | tty | tv"

    .. note:: HTML5
    
    .. note:: HTML5.1 удален

    Носитель целевого документа

* rel = "alternate | author | bookmark | help | license | next | nofollow | noreferrer | prefetch | prev | search | tag"

    Связь между исодным и связанными документами

* target = "текст"

    Имя окна или области iframe, где будет отображаться документ

* type = "MIME"

    Тип контента для связанного контента

.. code-block:: html

    <a href="http:/ilnurgi.ru" id="my_anchor"></a>
    <a href="http:/ilnurgi.ru/post.html#news"></a>
    <a href="mailto:ilnurgi87@gmail.com"></a>
    <a href="tel:+1234567890"></a>

.. code-block:: html

    <a id="anchor_bottom"></a>
    <a href="#anchor_bottom"></a>


code
----

Фрагмент кода


div
---

Блочный элемент, секция

.. code-block:: html

    <div id="summary">
        ....
    </div>


em
---

Выделение текста


embed
-----

.. note:: HTML5

Внедрение объекта на страницу

* height - высота элемента

* src - ссылка на ресурс

* type - тип ресурса

* width - ширина элемента

.. code-block:: html

    <embed src="ilnurgi.mov" width="240" height="320" type="video/quicktime"


iframe
------

Фрейм, используемый для внедрения другого документа

* allowfullscreen

    .. note:: HTML5

* height - высота элемента

* sandbox

    .. note:: HTML5

    * allow-forms

    * allow-pointer-lock

    * allow-popups

    * allow-same-origin

    * allow-scripts

    * allow-top-navigation

* seamless

    .. note:: HTML5

* src

* srcdoc

    .. note:: HTML5

* width - ширина элемента

.. code-block:: html

    <iframe src="ads.html" width="320" height="240"></iframe>


img
---

Изображение

* alt - альтернативный текст

* crossorigin - anonymous | use-credentials

* height - высота элемента

* ismap

* src

* usemap

* width - ширина элемента

.. code-block:: html

    <img src='' alt='' title='' width='' height=''>


span
----

Строчный элемент, используется для верстки

.. code-block:: html

    <span></span>