layout - разметка активити
==========================

* res/layout - активити для вертикального экрана
* res/layout-land - активити для шоризонтального экрана

Разметка может содержать такие группирующие элементы:

    * :py:class:`android.widget.AbsoluteLayout`
    * :py:class:`android.widget.LinerLayout`
    * :py:class:`android.widget.RelativeLayout`
    * :py:class:`android.widget.TableLayout`

А также виджеты:

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

.. code-block:: xml

    <view
        android:text="@string/some_text" />


textSize
--------

Размер текста