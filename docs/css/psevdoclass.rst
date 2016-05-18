Псевдоклассы
============


after
-----

Вставка контента после элемента

.. code-block:: css

    p:after {
        content: "...";
    }


first-child
-----------

Поиск первого дочернего элемента

.. code-block:: css

    p:first-child{}


first-of-type
-------------

Поиск первого элемента заданного типа

.. code-block:: css

    p:first-of-type{}


last-child
----------

Поиск последнего дочернего элемента

.. code-block:: css

    p:last-child{}


last-of-type
------------

Поиск последнего элемента заданного типа

.. code-block:: css

    p:last-of-type{}


nth-child
---------

Поиск заданного дочернего элемента в прямом направлении

.. code-block:: css

    p:nth-child(2n+1){}


nth-last-child
--------------

Поиск заданного дочернего элемента в обратном напрвлении

.. code-block:: css

    p:nth-last-child(2) {}


nth-of-type
-----------

Поиск всех элементов определенного типа

.. code-block:: css

    p:nth-of-type(2n+1){}