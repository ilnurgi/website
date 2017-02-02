android.widget.RadioButton
==========================

Переключатель, поддерживающий два состояния и группировку.

Группы таких переключателей пользователь видит как набор двоичных вариантов,
из которых в определенный момент времени может быть выбран только один.

XML
---

.. code-block:: xml

    <RadioGroup

        android:layout_height="wrap_content"
        android:layout_width="match_parent"

        android:orientation="horizontal"
        android:id="@+id/rgGravity">

        <RadioButton

            android:layout_height="wrap_content"
            android:layout_width="wrap_content"

            android:checked="true"
            android:text="Left"
            android:id="@+id/rbLeft" />

    </RadioGroup>


RadioButton
-----------

.. py:class:: android.widget.RadioButton

    Наследник :py:class:`android.view.View`


    .. py:method:: setChecked(bool)

        ставит флажок


    .. py:method:: isChecked()

        возвращает статус флажка