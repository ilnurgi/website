Конспекты по css
================

.. toctree::
    :maxdepth: 2
    
    background
    border
    font
    list
    marking
    table
    animation
    psevdoclass


content
-------

Текст, который появляется либо до, либо после элемента.

.. code-block:: css

    elem:before {
        content: "Before";
    }

    elem:after {
        content: "After";
    }


cursor
------

Определаяет форму указателя мышки

* auto - по умолчанию

* default

* crosshair

* pointer

* move

* e-resize

* ne-resize

* nw-resize

* resize

* se-resize

* sw-resize

* s-resize

* w-resize

* text

* wait

* help

* progress

.. code-block:: css

    elem {
        cursor: help;
    }

    elem1 {
        cursor: url(images/cursor.cur);
    }


linear-gradient
---------------

Градиентная заливка

.. code-block:: css

    elem {
        linear-gradient(top, #fff, #efefef);
    }


media
-----

Медиазапросы

* width - ширина области просмотра

* height - высота области просмотра

* device-width - ширина экрана

* device-height - высота экрана

* orientation - ориентация экрана

* aspect-ratio - соотношение сторон области просмотра

* device-aspect-ratio - соотношение сторон экрана

* color - количество бит на цвет

* color-index - количесвто записей в таблице подстановки цветов

* monochrome сколько бит на каждый пиксель

* resolution - разрешение экрана или печати

* scan - тип развертки

* grid - устройство с фиксированным размером символов

.. code-block:: css
    
    @media screen and (max-width: 960px){
        body {
            ...
        }
    }   


opacity
-------

Прозрачность элемента

.. code-block:: css

    elem {
        opacity: .5;
    }


.. _orphans:

orphans
-------

Минимальное количество строк текста, которые можно оставить внизу распечатанной страницы

.. code-block:: css

    elem {
        orphans: 3;
    }


page-break-after
----------------

Происходит ли разрыв страницы при печати после определенного элемента

* auto - по умолчанию

* always - элемент, который следует далее, появится вверху отдельной печатной страницы

* avoid - предотвращает обрыв страницы после элмента

* left

* right

.. code-block:: css

    elem {
        page-break-after: always;
    }


page-break-before
-----------------

Происходит ли разрыв страницы при печати перед определенным элементом

* auto - по умолчанию

* always - элемент, который следует перед, появится вверху отдельной печатной страницы

* avoid - предотвращает обрыв страницы перед элментом

* left

* right

.. code-block:: css

    elem {
        page-break-before: always;
    }


page-break-inside
-----------------

Препятствует тому, что элмент будет разбит на две печатные страницы

.. code-block:: css

    elem {
        page-break-inside: avoid;
    }


widows
------

Противоположное :ref:`orphans`, минимальное количество строк, которое должно появиться наверху печатной страницы

.. code-block:: css

    elem {
        widows: 5;
    }