android.widget.RelativeLayout
=============================

Контейнер, позволяет задавать позицию каждого дочернего элемента
относительного других элементов и границ экрана.


XML
---

.. code-block:: xml

    <RelativeLayout
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:layout_width="wrap_content"
        android:layout_height="wrap_content">

        <TextView
            android:id="@+id/label" />

        <TextView
            android:layout_below="@id/label"
            android:layout_alignParent="true"

            android:id="@+id/label2" />

    </RelativeLayout>

Свойства, которыми могут обладать дочерние элементы
+++++++++++++++++++++++++++++++++++++++++++++++++++

* layout_align... - выравнивание элемента относительно указанного

    * layout_alignBottom - снизу
    * layout_alignLeft - слева
    * layout_alignRight - справа
    * layout_alignTop - сверху

* layout_alignParent... - выравнивание элемента относительно родителя

    * layout_alignParentBottom -  снизу
    * layout_alignParentLeft - слева
    * layout_alignParentRight - справа
    * layout_alignParentTop - сверху

* layout_center... - выравниваение элемента по центру относительно родителя

    * layout_centerVertical - вертикально
    * layout_centerHorizontal - горизонтально
    * layout_centerInParent - по центру вертикально и горизонтально относительно родителя

* layout_height - высота элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому

* layout_to... - расположить элемент относительно указанного

    * layout_above - сверху
    * layout_below - снизу
    * layout_toLeftOf - слева
    * layout_toRightOf - справа

* layout_width - ширина элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому


RelativeLayout
--------------

.. py:class:: android.widget.RelativeLayout()

    Наследник :py:class:`android.view.ViewGroup`


RelativeLayout.LayoutParams
---------------------------

.. py:class:: android.widget.RelativeLayout.LayoutParams

    Настройки слоя

    Наследник :py:class:`android.view.ViewGroup.LayoutParams`