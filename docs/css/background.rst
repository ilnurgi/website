Фон
===

background
----------

Задает в сокращенном виде фон элемента: цвет, URL изображения, повторение, позиционирование изображения

.. code-block:: css

    body {
        background: #333 url(images/logo.gif) no-repeat fixed left top;
    }

    body {
        background: url(images/logo.gif) no-repeat center cover;
    }
    
background-attachment
---------------------

Определяет, как ведет себя фон при прокрутке страницы

* scroll - прокручивается вместе с элементом

* fixed - не прокручивается совсем

.. code-block:: css

    body {
        background-attachment: fixed;
    }


background-clip
---------------

Ограничивает область, в которой появляется фон

* border-box - под границей, отступами и содержимым

* padding-box - в области отступов и содержимого

* content-box - в области содержимого

.. code-block:: css

    div {
        background-clip: content-box;
    }


background-color
----------------

Цвет фона элемента, по умолчанию

* transparent - по умолчанию

* цвет

.. code-block:: css

    div {
        background-color: #fff;
    }


background-image
----------------

URL изображения

* none - по умолчанию

* URL

.. code-block:: css

    div {
        background-image: url(images/photo.jpg);
    }


background-origin
-----------------

Куда  помещать изображение относитльно границ, отступов и содержимого

* border-box - верхний левый угол

* padding-box - в области отступов

* content-box - в области содержимого

.. code-block:: css

    div {
        background-origin: content-box;
    }


background-position
-------------------

Позиционирование фонового изображения

* top

* center

* bottom

* left

* right

* число - по умолчанию, 0 0

.. code-block:: css

    div {
        background-position: left top;
    }


background-repeat
-----------------

Повторение фонового изображения

* repeat - повторяется по горизонтали и по вертикали

* repeat-x - повторить по горизонтали

* repeat-y - повторить по вертикали

* no-repeat - не повторять

.. code-block:: css

    div {
        background-repeat: no-repeat;
    }


background-size
---------------

Размер фонового изображения

.. code-block:: css

    div {
        background-size: 200px 400px;
    }
    