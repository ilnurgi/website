android.widget.RadioGroup
=========================

Контейнер для радио-кнопок

XML
---

.. code-block:: xml

    <RadioGroup

        android:layout_height="wrap_content"
        android:layout_width="match_parent"

        android:orientation="horizontal"
        android:id="@+id/rgGravity">

    </RadioGroup>

RadioGroup
----------

.. py:class: android.widget.RadioGroup()

    Наследник :py:class:`android.widget.LinearLayout`

    .. code-block:: java

        RadioGroup radioGroup = (RadioGroup) findViewById(R.id.radioGroup);


    .. py:method:: getCheckedRadioButtonId()

        Возвращает идентификатор активной радиокнопки

        .. code-block:: java

            switch (radioGroup.getCheckedRadioButtonId()){
                case R.id.someRb:

            }