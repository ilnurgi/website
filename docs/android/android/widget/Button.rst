.. py:module:: android.widget

Button - кнопка
===============

.. py:class:: Button

    Наследник :py:class:`android.widget.TextView`

    .. code-block:: java

        Button btnLogin = (Button)findViewById(R.id.btnLogin);

    .. code-block:: html

        <Button
            android:id="@+id/btnHome"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/btnHome" />


    .. py:method:: setText(str)
    .. py:method:: setText(R.string.name)

        устанавливает текст для объекта

    .. py:method:: setEnabled(bool)

        активность кнопки


.. code-block:: java

    button.setOnClickListener(new View.OnClickListener(){

        @Override
        public void onClick(View v){
            ...
        }
    });
