layout - разметка активити
==========================

Ресурс хранится в папке res/layout и
res/layout_land - для горизонтальной ориентации экрана.

Разметка может содержать такие группирующие элементы, как:

    * :py:class:`android.widget.LinerLayout`

А также виджеты

    * :py:class:`android.widget.Button`

Свойства компонентов:

.. code-block:: xml

    <Button
        android:id="@+id/btnLogin />


background
----------


drawable
--------

* drawablePadding
* drawableRight

.. code-block:: xml

    <view
        android:drawableRight="@drawable/arrow_right"
        android:drawablePadding="4dp" />


fadingEdge
----------


gravity
-------

.. code-block:: xml

    <view
        android:gravity="center" />


id
--

Иденификатор


layout_align...
---------------

Выравнивание элемента относительно указанного

* layout_alignBottom - снизу
* layout_alignLeft - слева
* layout_alignRight - справа
* layout_alignTop - сверху


layout_alignParent...
---------------------

Выравнивание элемента относительно родителя

* layout_alignParentBottom -  снизу
* layout_alignParentLeft - слева
* layout_alignParentRight - справа
* layout_alignParentTop - сверху


layout_center...
----------------

Выравниваение элемента по центру экрана

* layout_centerVertical - вертикально
* layout_centerHorizontal - горизонтально
* layout_centerInParent - по центру вертикально и горизонтально относительно родителя


layout_gravity
--------------

Расположение элемента внутри родителя относительно краев

* top
* left
* right
* bottom
* center
* center_horizontal
* center_vertical

.. code-block:: xml

    <view
        android:layout_gravity="center_horizontal" />

    <view2
        android:layout_gravity="center_horizontal|center_vertical" />



layout_height
-------------

Высота элемента

* wrap_content - по содержимому
* match_parent - по родителю
* dp, ...

.. code-block:: xml

    <view
        android:layout_height="match_parent" />


layout_margin...
----------------

Внешние отступы элемента

* layout_marginLeft
* layout_marginRight
* layout_marginBottom
* layout_marginTop


layout_to...
------------

Расположить элемент относительно указанного

* layout_above - сверху
* layout_below - снизу
* layout_toLeftOf - слева
* layout_toRightOf - справа


layout_weight
-------------

Ширина элемента

* wrap_content - по содержимому
* match_parent - по родителю
* dp, ...

.. code-block:: xml

    <view
        android:layout_width="match_parent" />


layout_x
--------

Абсолютная координата расположения элемента


layout_y
--------

Абсолютная координата расположения элемента


onClick
-------

Обрабочика клика


orientation
-----------

Ориентация выстраивания потомков

* vertical
* horizontal

.. code-block:: xml

    <view
        android:orientation="vertical" />


padding...
----------

Внутренний отступ элемента

* paddingBottom
* paddingLeft
* paddingRight
* paddingTop

.. code-block:: xml

    <view
        android:paddingLeft="@dimen/activity_horizontal_margin"
        android:paddingRight="@dimen/activity_horizontal_margin"
        android:paddingTop="@dimen/activity_vertical_margin"
        android:paddingBottom="@dimen/activity_vertical_margin" />

    <view2
        android:padding="24dp" />


scrollbars
----------


text
----

Текст

.. code-block::

    <view
        android:text="@string/some_text" />


textSize
--------

Размер текста