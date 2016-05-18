Списки
======

list-style
----------

Задает в сокращенном виде: тип списка, расположение маркеров, изображение маркеров

.. code-block:: css

    ul {
        list-style: disc url (images/bullet.gif) inside;
    }


list-style-image
----------------

URL файла изображения маркера

* none - по умолчанию

* URL

.. code-block:: css

    ul {
        list-style-image: url (images/bullet.gif);
    }


list-style-position
-------------------

Расположение маркеров относительно элемента в списке

* outside - по умолчанию

* inside

.. code-block:: css

    ul {
        list-style-position: inside;
    }


list-style-type
---------------

Маркер для списка

* disc

* circle

* square

* decimal

* lower-roman

* upper-roman

* lower-alpha

* upper-alpha

* none

.. code-block:: css

    ul {
        list-style-type: square;
    }
