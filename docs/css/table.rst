table - таблицы
===============

.. _border_collapse:

border-collapse
---------------

Определяет, расширены границы вокруг ячеек таблицы или сжаты

* collapse

* separate

.. code-block:: css

    table {
        border-collapse: collapse;
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


caption-side
------------

Позиционирование названия таблицы

* top - по умолчанию

* bottom

* left

* right

.. code-block:: css

    elem {
        caption-side: top;
    }


empty-cells
-----------

Задает отображение рамок вокруг пустых ячеек таблицы

* show - по умолчанию

* hide

.. code-block:: css

    elem {
        empty-cells: show;
    }


table-layout
------------

Управляет тем, как браузер чертит таблицу. 

* fixed - все столбцы к той же ширине, что задана для столбцов из первой строки

* auto - по умолчанию

.. code-block:: css

    elem {
        table-layout: fixed;
    }