android.widget.LinerLayout
==========================

Контейнер, который распологает элементы внутри себя в линию по горизонтали или по вертикали.

XML
---

.. code-block:: xml

    <LinerLayout
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:layout_width="wrap_content"
        android:layout_height="wrap_content"

        android:orientation="vertical"
        android:id="@+id/layout"/>

* background - фон

    * @drawable/rect

* id - идентификатор элемента

    * @+id/identifier

* orientation - порядок заполнения виджетами контейнера

    * vertical
    * horizontal

Свойства, которыми могут обладать дочерние элементы
+++++++++++++++++++++++++++++++++++++++++++++++++++

* layout_gravity - выравнивание элемента в родителе

    * top
    * bottom
    * left
    * right
    * center

* layout_height - высота элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому
    * 10dp

* layout_margin... - внешние отступы элемента

    * layout_marginLeft
    * layout_marginRight
    * layout_marginBottom
    * layout_marginTop

* layout_weight - вес элемента, для заполнения родителя

* layout_width - ширина элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому
    * 20 dp


LinerLayout
-----------

.. py:class:: android.widget.LinerLayout

    Наследник :py:class:`android.view.ViewGroup`


    .. py:attribute:: VERTICAL

        Статическая константа, вертикальный лейаут


    .. py:method:: addView(View view)

        Добавляет вью в слой

        .. code-block:: java

            linearLayout.addView(someView);
            linearLayout.addView(someView, viewLayoutParams);


    .. py:method:: removeAllViews()

        Удаляет все элементы со слоя

        .. code-block:: java

            linearLayout.removeAllViews()


    .. py:method:: setOrientation(orientation)

        Устанавливает ориентацию для слоя

        * LinearLayout.VERTICAL
        * LinearLayout.HORIZONTAL

        .. code-block:: java

            linearLayout.setOrientation(LinearLayout.VERTICAL);


LinerLayout.LayoutParams
------------------------

.. py:class:: android.widget.LinerLayout.LayoutParams

    Настройки слоя

    Наследник :py:class:`android.view.ViewGroup.MarginLayoutParams`

    .. code-block:: java

        LinerLayout.LayoutParams linearLayout = new LinerLayout.LayoutParams(
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT);
        linearLayout.leftMargin = 50;

    .. py:attribute:: gravity
    .. py:attribute:: weight
