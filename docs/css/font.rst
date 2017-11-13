Текст
=====

color
-----

Цвет текста в элементе

.. code-block:: css

    body {
        color: #ffff33;
        color: red;
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

Семейство шрифтов

* serif - шрифты с засечками

* sans-serif - рубленые шрифты

* cursive - курсивные шрифты

* fantasy - декоративные шрифты

* monospace - моноширинные шрифты

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
        font-size: 60px;
    }


font-style
----------

Стиль начертания шрифтов

* normal - по умолчанию

* italic - курсивый

* oblique - наклонный

.. code-block:: css

    body {
        font-style: italic;
    }


font-variant
------------

Вариант начертания шрифта

* normal - по умолчанию

* small-caps - строчные буквы модифицируются в заглавные, но меньшего размера

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

* center - по центру

* justify - по ширине

* left - по левому краю

* right - по правому краю

* start - если направление текста слева направо, то слева, иначе справа

* end - если направление текста слева направо, то справа, иначе слева

.. code-block:: css

    body {
        text-align: center;
    }


text-align-last
---------------

Тип выравнивания последней строки элемента, если text-align задан как justify.

Принимает теже параметры что и text-align

.. code-block:: css

    .content {
        text-align: justify;
        text-align-last: left;
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


text-overflow
-------------

Видимость текста

* clip - текст обрезается, если вылезает за пределы элемента

* ellipsis - добавляется многоточие

.. code-block:: css

    .content {
        text-overflow: clip;
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

Преобразование текста в заглавные или прописные буквы

* capitalize - первый символ заглавный

* uppercase - символы в верхнем регистре

* lowercase - символы в нижнем регистре

* none - по умолчанию

.. code-block:: css

    body {
        text-transform: uppercase;
    }


vertical-align
--------------

Вертикальное положение относительно базовой линии

* baseline - выравнивание базовой линии по соответсвующей линии родительского элемента

* bottom - выравнивание по нижней части элемента

* middle - по центру родительского элемента

* sub - базовая линия по базовой линии нижнего индекса родительского элемента

* super - базовая линия по базовой линии верхнего индекса родительского элемента

* top - по верхней части родителя

* text-bottom - нижний край фрагмента по нижнему краю текста родителя

* text-top - верхний край фрагмента текста по верхнему краю текста родителя

* число

.. code-block:: css

    body {
        vertical-align: top;
    }


white-space
-----------

Отображение пробелов, табуляции, перевода строки

* normal - по умолчанию, несколько пробелов преобразуются в один,
  переводы строк преобразуются в пробелы. браузер сам разрывает текст

* pre - преформативное, пробелы и переводы строк сохраняются как есть.
  браузер сам ничего не разрывает

* pre-line - пробелы схлопываются, переводы строк сохраняются.
  браузер сам все разрывает

* pre-wrap - пробелы и переводы строк сохрнаяются, брузер сам разрывает

* nowrap - безразрывное, несколько пробелов преобразуются в один,
  переводы строк преобразуются в пробелы. браузер не разрывает текст

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


word-wrap
---------

Указывает места, где браузер может осуществить перевод строки

* break-word - разрыв строк может быть внутри слов

* normal - строки разбиваются пробелами

