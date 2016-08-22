android.widget.FrameLayout
==========================

Контейнер, прикрепляет каждый элемент к верхнему левому углу экрана.

Каждый новый элемент накладывается на предыдущий, заслоняя его.

XML
---

.. code-block:: xml

    <FrameLayout

        android:layout_width="match_parent"
        android:layout_height="match_parent"

        android:id="@+id/frameLayout1" >

        <Button

            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="top|left"

            android:text="gravity = top left"
            android:id="@+id/button1" />

    </FrameLayout>

Свойства, которыми могут обладать дочерние элементы
+++++++++++++++++++++++++++++++++++++++++++++++++++

* layout_height - высота элемента

    * match_parent - заполнить родителя

    * wrap_content - по содержимому

* layout_width - ширина элемента

    * match_parent - заполнить родителя

    * wrap_content - по содержимому

FrameLayout
-----------

.. py:class:: android.widget.FrameLayout

    Наследник :ref:`android.view.ViewGroup`


FrameLayout.LayoutParams
------------------------

.. py:class:: android.widget.FrameLayout.LayoutParams

    Настройки слоя

    Наследник :py:class:`android.view.ViewGroup.LayoutParams`