flex
====

.. code-block:: css

    .some-class {
        display: flex;
        flex: flex-grow flex-shrink flex-basis;
    }


align-content
-------------

Распределение основных осей вродителе

* center

* space-between

* stretch

.. code-block:: css

    .some-class {
        align-content: center;
    }


align-items
-----------

Выравнивание дочерних элементов по второстепенной оси

* baseline

* flex-start - выравнивание по верхнему краю

* flex-end - выравнивание по нижнему краю

* center - по центру

* stretch - по максимальному, по умолчанию

.. code-block:: css

    .some-class {
        align-items: stretch;
    }


align-self
----------

Выравнивание самого дочернего элемента

* auto - по умолчанию, как в родительском

* baseline

* flex-start - выравнивание по верхнему краю

* flex-end - выравнивание по нижнему краю

* center - по центру

* stretch - по максимальному

.. code-block:: css

    .some-child-class {
        align-self: auto;
    }


flex-basis
----------

Задает минимальную ширину дочернего элемента.

Если дочерний элемент находится на основной оси с другими элементами,
то его ширина не будет изменяться при уменьшении ширины родительского элемента,
другие элементы или сам элемент будут переходить на другие оси.

Если дочерний элемент находится на основной оси один,
то его ширина будет уменьшаться при уменьшении ширины родительского элемента.

* auto

.. code-block:: css

    .some-child-class {
        flex-basis: auto;
        flex-basis: 300px;
    }


flex-direction
--------------

Направление основной оси

* column - сверху вних

* column-reverse - снизу вверх

* row - по умолчанию, слева направо

* row-reverse - справа налево

.. code-block:: css

    .some-class {
        display: flex;
        flex-direction: row;
    }


flex-grow
---------

Степень жадности элемента

Если значение отличное от 0,
то по ширине элемент займет все пустое пространство по главной оси.

* 0 - по умолчанию, элемент не жадный

.. code-block:: css

    .some-child-class {
        flex-grow: 0;
    }

flex-shrink
-----------

Степень/скорость сжимаемости элемента

* 0 - элемент не сжимаемый

* 1 - по умолчанию, элемент сжимаемый

.. code-block:: css

    .some-class {
        flex-shrink: 1;
    }


flex-wrap
---------

Перенос элементов в элементе

* no-wrap - по умолчанию, не переносить

* wrap - переносить

* wrap-reverse

.. code-block:: css

    .some-class {
        flex-wrap: wrap;
    }


justify-content
---------------

Заполнение оси

* flex-end - относительно конца

* flex-start - относительно начала

* center - от центра

* space-around - растягивает по оси, оставляя равные промежутки между элементами

* space-between - растягивает по оси, оставляя равные промежутки между элементами

.. code-block:: css

    .some-class {
        justify-content: flex-start;
    }


order
-----

Задает порядковый номер элементу по флекс контейнере

.. code-block:: html

    .some-child-class {
        order: -1;
    }