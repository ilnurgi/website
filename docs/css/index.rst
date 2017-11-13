Конспекты по css
================


.. code-block:: html

    <link rel='stylesheet' href='main.css'>



.. toctree::
    :maxdepth: 2

    selectors
    background
    border
    font
    list
    marking
    table
    animation
    psevdoclass
    psevdoelements
    faq
    flex


Цвета
-----

.. code-block:: css

    elem {
        color: red,
        color: #ff00ff,
        color: #f0f,
        color: rgb(255, 0, 255),
        color: rgb(100%, 0, 100%),
        color: rgba(255, 0, 255, 1),
        color: rgba(100%, 0, 100%, 1),

        /* тон, насыщенность, яркость */
        color: hsl(300, 100%, 50%),
        color: hsla(300, 100%, 50%, 1),

        /* голубой, пурпурный, желтый, черный */
        color: cmyk(29%, 55%, 0, 0),
    }


Единицы измерения
-----------------

* em - относительный, размера шрифта родительского элемента
* ex - относительный, высоты символа х в нижнем регистре
* ch - относительный, размера символа нуль
* rem - относительный, размера шрифта корневого элемента
* vw - относительный, ширины окна просмотра
* vh - относительный, высоты экрана просмотра
* vmin - наименьшее значение между vw и vh
* vmax - наибольшее значение между vw и vh
* px - относительный, разрешения экрана, 1/72 дюйма
* in - дюйм
* cm - сантиметры
* mm - милиметры
* pt - пункты, 1/72 дюйма
* pc - пика, 1/12 пункта
* % - относительный, родительского элемента
* dpi - разрешение точек на дюйм
* dpc - разрешение точек на сантиметр
* dppx - разрешение точек на пиксель

Угловые, временные и частоты

* deg - градусы
* grad - градиан, 1/400 окружности
* rad - радиан, 180/pi, ~57.3
* turn - оборот
* ms - миллисекунда
* s - секунда
* Hz - герц
* kHz - килогерц


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

Типы устройств:

* all - все устройства
* braille - устройства с тактильной обратной связью
* embossed - брайлевсике принтеры
* handled - портативные устройства
* print - принтеры
* projection - проекторы
* screen - цветные экраны
* speech - речевые синтезаторы
* tty - моноширинная символьная среда
* tv - телевизоры

Другие:

* color - количество бит на цвет
* color-index - количесвто записей в таблице подстановки цветов
* grid - устройство с фиксированным размером символов
* monochrome - сколько бит на каждый пиксель
* orientation - ориентация экрана
* resolution - разрешение экрана или печати
* scan - тип развертки
* width - ширина области просмотра
* height - высота области просмотра
* min-width
* max-width
* min-height
* max-height
* device-width - ширина экрана
* device-height - высота экрана
* min-device-width
* max-device-width
* min-device-height
* max-device-height
* aspect-ratio - соотношение сторон области просмотра
* min-aspect-ratio
* max-aspect-ratio
* device-aspect-ratio - соотношение сторон экрана
* min-device-aspect-ratio
* max-device-aspect-ratio

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