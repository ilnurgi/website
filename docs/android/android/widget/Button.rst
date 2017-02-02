android.widget.Button
=====================

XML
---

.. code-block:: xml

    <Button

        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="top|left"

        android:text="@string/btn1"
        android:textSize="8pt"
        android:id="@+id/btn1" />

    <Button

        android:layout_width="100dp"
        android:layout_height="200dp"

        android:text="@string/btn2"
        android:id="@+id/btn2" />

* id - идентификатор элемента

* onClick - название метода активити, который обработает клик по элементу.
  Метод принимает один аргумент c типом :py:class:`android.view.View`
  и должен быть public void.

* text - текст

    * обычная строка, текст
    * ссылка на идентификатор из ресурса строк, :ref:`res_values_string`

* textSize - размер шрифта текст

    * 8pt


Button
------

.. py:class:: android.widget.Button

    Наследник :py:class:`android.widget.TextView`

    .. code-block:: java

        Button myBtn = (Button)findViewById(R.id.myBtn);


    .. py:method:: getLayoutParams()

        Возвращает параметры кнопки :py:class:`android.view.ViewGroup.LayoutParams`

        .. code-block:: java

            LayoutParams lparams = (LayoutParams) myBtn.getLayoutParams()


    .. py:method:: requestLayout()

        Перерисовывает элемент

        .. code-block:: java

            myBtn.requestLayout()


    .. py:method:: setText(str)
    .. py:method:: setText(R.string.name)

        устанавливает текст для объекта

        .. code-block:: java

            myBtn.setText("Some text");
            myBtn.setText(R.string.btnText);


    .. py:method:: setEnabled(bool)

        активность кнопки

        .. code-block:: java

            myBtn.setEnabled(false);


    .. py:method:: setOnClickListener(OnClickListener)

        Устанавливает обработчик клика по элементу

        * OnClickListener - :py:class:`android.view.View.OnClickListener`

        .. code-block:: java

            myBtn.setOnClickListener(new OnClickListener(){

                @Override
                public void onClick(View v){
                    ...
                }

            });
