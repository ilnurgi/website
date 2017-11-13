Разметка
========

bottom
------

.. code-block:: css

    div {
        bottom: 5em;
    }


clear
-----

Запрещает обтекание элемента текстом

* none - по умолчанию

* left

* right

* both

.. code-block:: css

    div {
        clear: both;
    }


clip
----

Определяет прямоугольную область, в которую выводится содержимое элемента

* rect

* auto - по умолчанию

* crosshair

* default

* pointer

* move

* e-resize

* ne-resize

* nw-resize

* n-resize

* se-resize

* sw-resize

* s-resize

* w-resize

* text

* wait

* help

.. code-block:: css

    div {
        clip: rect(5px,110px,35px,10px);
    }


display
-------

Определяет тип элемента и управляет отображением элемента:
    
    * none - элемент скроется из документа

    * block - блочный
    
    * inline - строчный

    * inline-block - строчно-блочный

    * list-item

    * table-cell - ячейка таблицы


.. code-block:: css
    
    div {
        display: inline;
    }


float
-----

Плавающий элемент, задает обтекание элемента текстом

* left

* right

* none - по умолчанию

.. code-block:: css

    img {
        float: left;
    }


height
------

Высота элемента

* auto - по умолчанию

* число

.. code-block:: css

    table {
        height: 500px;
    }


left
----

.. code-block:: css

    div {
        left: 5em;
    }


max-height
----------

Максимальная высота элемента

.. code-block:: css

    div {
        max-height: 100px;
    }


max-width
---------

Максимальная ширина элемента

.. code-block:: css

    div {
        max-width: 100px;
    }


min-height
----------

Минимальная высота элемента

.. code-block:: css

    div {
        min-height: 100px;
    }


min-width
---------

Минимальная ширина элемента

.. code-block:: css

    div {
        min-width: 100px;
    }


overflow
--------

Управляет отображением содержимого элемента за пределами области вывода

* visible

* hidden

* scroll

* none - по умолчанию

.. code-block:: css

    div {
        overflow: hidden;
    }


position
--------

Позиционирование элементов

* absolute - элемент исключается из потока документа

* fixed - элемент исключается из потока документа и при прокрутке окна будет оставаться на месте

* relative - элемент будет смещаться относительно своего положения, его место будет оставаться не заполненным

* static - по умолчанию, нормальный поток документов

* sticky - закрепленное, комбинация относительного и фиксированного

.. code-block:: css

    div {
        position: absolute;
    }


right
-----

.. code-block:: css

    div {
        right: 5em;
    }


top
---

.. code-block:: css

    div {
        top: 10px;
    }


visibility
----------

Видимость элемента

* visible

* hidden

* inherit

.. code-block:: css

    div {
        visibility: hidden;
    }


width
-----

Ширина элемента

* auto - по умолчанию

* число

.. code-block:: css

    div {
        width: 500px;
    }


z-index
-------

Порядок расположения перекрывающихся элементов

* auto - по умолчанию

* число

.. code-block:: css

    div {
        z-index: 2;
    }