Границы, отступы и поля
=======================

box-shadow
----------

Тень вокруг элемента

.. code-block:: css

    div {
        box-shadow: inset 4px 4px 3px 5px #999999 2px 2px 5px black;
    }


border
------

Задает в сокращенном виде свойства границ элемента: ширину, стиль, цвет линии

.. code-block:: css

    div {
        border 1px solid red;
    }


border-bottom
-------------

Задает в скоращенном виде свойства нижней границы элемента: ширина, стиль, цвет

.. code-block:: css

    div {
        border-bottom: 1px solid red;
    }


border-bottom-color
+++++++++++++++++++

Задает цвет нижней границы элемента

.. code-block:: css

    div {
        border-bottom-color: #000;
    }


border-bottom-style
+++++++++++++++++++

Задает стиль нижней границы элемента, значения из :ref:`border_style`

.. code-block:: css

    div {
        border-bottom-style: none;
    }


border-bottom-width
+++++++++++++++++++

Задает ширину нижней границы, значения из :ref:`border_width`

.. code-block:: css

    div {
        border-bottom-width: 3em;
    }


border-color
------------

Задает цвет границ

.. code-block:: css

    div {
        border-color: #000;
    }


border-left
-----------

Задает в скоращенном виде свойства левой границы элемента: ширина, стиль, цвет

.. code-block:: css

    div {
        border-left: 1px solid red;
    }


border-left-color
+++++++++++++++++

Задает цвет левой границы элемента

.. code-block:: css

    div {
        border-left-color: #000;
    }


border-left-style
+++++++++++++++++

Задает стиль левой границы элемента, значения из :ref:`border_style`

.. code-block:: css

    div {
        border-left-style: none;
    }


border-left-width
+++++++++++++++++

Задает ширину левой границы, значения из :ref:`border_width`

.. code-block:: css

    div {
        border-left-width: 3em;
    }


border-radius
-------------

Скругляет углы границ элемента

.. code-block:: css

    div {
        border-radius: 15px 10px 25px 5px;
    }

border-top-right-radius
+++++++++++++++++++++++

border-bottom-right-radius
++++++++++++++++++++++++++

border-bottom-left-radius
+++++++++++++++++++++++++

border-top-left-radius
++++++++++++++++++++++


border-right
------------

Задает в скоращенном виде свойства правой границы элемента: ширина, стиль, цвет

.. code-block:: css

    div {
        border-right: 1px solid red;
    }


border-right-color
++++++++++++++++++

Задает цвет правой границы элемента

.. code-block:: css

    div {
        border-right-color: #000;
    }


border-right-style
++++++++++++++++++

Задает стиль правой границы элемента, значения из :ref:`border_style`

.. code-block:: css

    div {
        border-right-style: none;
    }


border-right-width
++++++++++++++++++

Задает ширину правой границы, значения из :ref:`border_width`

.. code-block:: css

    div {
        border-right-width: 3em;
    }


border-spacing
--------------

Определяет зазор между границами смежных ячеек таблицы

.. code-block:: css

    td {
        border-spacing: "0";
        /* границы соседних ячеек будут двойными, уберем это */
        border-collapse: collapse;        
    }

    td {
        border-spacing: 5px 10px;
    }


.. _border_style:

border-style
------------

Задает стиль границ элемента

* none - по умолчанию

* hidden

* dotted

* dashed

* solid

* double

* groove

* ridge

* inset

* outset

.. code-block:: css

    div {
        border-style: solid dotted dashed double;
    }


border-top
----------

Задает в скоращенном виде свойства верхней границы элемента: ширина, стиль, цвет

.. code-block:: css

    div {
        border-top: 1px solid red;
    }


border-top-color
++++++++++++++++

Задает цвет верхней границы элемента

.. code-block:: css

    div {
        border-top-color: #000;
    }


border-top-style
++++++++++++++++

Задает стиль верхней границы элемента, значения из :ref:`border_style`

.. code-block:: css

    div {
        border-top-style: none;
    }


border-top-width
++++++++++++++++

Задает ширину верхней границы, значения из :ref:`border_width`

.. code-block:: css

    div {
        border-top-width: 3em;
    }


.. _border_width:

border-width
------------

Задает ширину границ

* thin

* medium - по умолчанию

* thick

* число

.. code-block:: css

    div {
        border-width: 3em 1em 2em 3.5em;
    }


box-sizing
----------

Порядок измерения высоты и ширины элемента

* context-box - обычный порядок

* padding-box - включить в расчет значение padding

* border-box - включить в расчет значение border

.. code-block:: css

    div {
        box-sizing: border-box;
    }


margin
------

Внешний отступ от границ элемента

.. code-block:: css

    div {
        margin: 2em 3em 2.5em 0;
    }


margin-bottom
+++++++++++++

Внешний отступ от нижней границы

.. code-block:: css

    div {
        margin-bottom: 20px;
    }


margin-left
+++++++++++

Внешний отступ от левой границы

.. code-block:: css

    div {
        margin-left: 20px;
    }


margin-right
++++++++++++

Внешний отступ от правой границы

.. code-block:: css

    div {
        margin-right: 20px;
    }


margin-top
++++++++++

Внешний отступ от верхней границы

.. code-block:: css

    div {
        margin-top: 20px;
    }


outline
-------

Задает в сокращенном виде свойства границ элемента,
которые не учитываются в размерах элемента.

.. code-block:: css

    div {
        outline: 3px solid #F33;
    }


outline-color
+++++++++++++

Цвет контура

.. code-block:: css

    div {
        outline-color: #F33;
    }


outline-style
+++++++++++++

Тип контура

.. code-block:: css

    div {
        outline-style: dashed;
    }


outline-width
+++++++++++++

Толщина контура

.. code-block:: css

    div {
        outline-width: 3px;
    }


padding
-------

Внутренний отступ от границ

.. code-block:: css

    td {
        padding: 1px 2px 3px 4px;

        /* 1 - верх и низ, 2 - слева и справа*/
        padding: 1px 2px;

        /* 1 - верх, 2 - слева и справа, 3 - низ*/
        padding: 1px 2px 3px;
    }
    

padding-bottom
++++++++++++++

Внутренний отступ от нижней границы

.. code-block:: css

    div {
        padding-bottom: 20px;
    }


padding-left
++++++++++++

Внутренний отступ от левой границы

.. code-block:: css

    div {
        padding-left: 20px;
    }


padding-right
+++++++++++++

Внутренний отступ от правой границы

.. code-block:: css

    div {
        padding-right: 20px;
    }


padding-top
+++++++++++

Внутренний отступ от верхней границы

.. code-block:: css

    div {
        padding-top: 20px;
    }
