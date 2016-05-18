Текст
=====

color
-----

Цвет текста в элементе

.. code-block:: css

    body {
        color: #ffff33;
    }


font
----

Задает в сокращенном виде шрифт: стиль, начертание, толщину, размер, высоту, наименование

.. code-block:: css

    body {
        font: italic small-caps bold 1.25em/150% Arial, Helvetica, sans-serif;
    }


font-family
-----------

Семейство шрифтов: arial, helvetica ...

.. code-block:: css

    body {
        font-family: "Lucida Grande", Arial, sans-serif;
    }


font-size
---------

Размер шрифта

* число

* xx-small

* x-small

* small

* medium - по умолчанию

* large

* x-large

* xx-large

.. code-block:: css

    body {
        font-size: 1.25em;
    }


font-style
----------

Стиль начертания шрифтов

* normal - по умолчанию

* italic

* oblique

.. code-block:: css

    body {
        font-style: italic;
    }


font-variant
------------

Вариант начертания шрифта

* normal - по умолчанию

* small-caps

.. code-block:: css

    body {
        font-variant: small-caps;
    }


font-weight
-----------

Жирность шрифта

* normal - по умолчанию

* bold

* bolder

* lighter

* число от 100 до 900 с шагом 100

.. code-block:: css

    body {
        font-weight: bold;
    }


letter-spacing
--------------

Межсимволный интервал

* normal - по умолчанию

* число

.. code-block:: css

    body {
        letter-spacing: -1px;
    }


line-height
-----------

Межстрочный интервал

* normal - по умолчанию

* число

.. code-block:: css

    body {
        line-height: 200%;
    }


text-align
----------

Горизонтальное выравнивание текста

* left

* right

* center

* justify

.. code-block:: css

    body {
        text-align: center;
    }


text-decoration
---------------

Начертание шрифта

* none - по умолчанию

* underline

* overline

* line-throught

* blink

.. code-block:: css

    body {
        text-decoration: underline overline line-through;
    }


text-indent
-----------

Отступ первой строки

.. code-block:: css

    body {
        text-indent: 3em;
    }


text-shadow
-----------

Тень

.. code-block:: css

    body {
        text-shadow: -4px 4px 3px #999999 2px 3px 10px #000;
    }


text-transform
--------------

Регистр

* capitalize

* uppercase

* lowercase

* none - по умолчанию

.. code-block:: css

    body {
        text-transform: uppercase;
    }


vertical-align
--------------

Вертикальное положение относительно базовой линии

* baseline

* sub

* super

* top

* text-top

* middle

* bottom

* text-bottom

* число

.. code-block:: css

    body {
        vertical-align: top;
    }


white-space
-----------

Отображение пробелов, табуляции, перевода строки

* normal - по умолчанию

* pre - преформативное

* nowrap - безразрывное

.. code-block:: css

    body {
        white-space: pre;
    }


word-spacing
------------

Интервал между словами

* normal - по умолчанию

* число

.. code-block:: css

    body {
        word-spacing: -1px; word-spacing: 2em;
    }
