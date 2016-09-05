android.widget.TextView
=======================

XML
---

.. code-block:: xml

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"

        android:gravity="center_horizontal"
        android:text="some_text"
        android:id="@+id/textView1" />

* clickable

    * true

* id - идентификатор элемента

* gravity - как будет расположен текст внутри элемента

    * center_horizontal

* minHeight

* onClick - обработчик клика

* text - текст

    * обычная строка, текст

    * ссылка на идентификатор из ресурса строк, :ref:`res_values_string`

* textSize - размер текста

    * 26sp

Свойства, которыми могут обладать дочерние элементы
+++++++++++++++++++++++++++++++++++++++++++++++++++

* layout_height - высота элемента

    * match_parent - заполнить родителя

    * wrap_content - по содержимому

* layout_width - ширина элемента

    * match_parent - заполнить родителя

    * wrap_content - по содержимому

TextView
--------

.. py:class:: android.widget.TextView([context[, attrs, [defStyle]]])

    Поддерживает многострочное отображение,
    форматирование и автоматический перенос слов и символов.

    Наследник :py:class:`android.view.View`

    * context - :py:class:`android.content.Context`

    * attrs - :py:class:`android.util.AttributeSet`

    * defStyle - int

    .. code-block:: java

        TextView textView = (TextView)findViewById(R.id.textView);


    .. py:method:: getText()
    
        Возвращает текст виджета


    .. py:method:: onDraw(Canvas canvas)

        * canvas - :py:class:`android.graphics.Canvas`


    .. py:method:: onKeyDown(int keyCode, KeyEvent keyEvent)


    .. py:method:: setGravity(gravity)

        Устанавливает выравнивание текста внутри элемента

        .. code-block:: java

            textView.setGravity(gravity)


    .. py:method:: setLayoutParams(layoutParams)

        Задает параметры для вьюхи

        .. code-block:: java

            textView.setLayoutParams(
                new LayoutParams(
                    LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));


    .. py:method:: setText(String text)
    .. py:method:: setText(int id)

        Устанавливает текст виджета

        .. code-block:: java

            textView.setText(textView.getText());
            textView.setText(R.string.name);
            textView.setText("Some text");


    .. py:method:: setTextSize(size)

        устанавливает размер текст для объекта


    .. py:method:: setTextColor(color)

        устанавливает цвет текст для объекта

        .. code-block:: java

            textView.setTextColor("red");


    .. py:method:: startAnimation(Animation anim)

        Запускается анимацию элемента

        * anim - :py:class:`android.view.animation.Animation`

        .. code-block:: java

            textView.startAnimation(anim);


    .. py:method:: requestFocus()

        устанавливает фокус на виджет