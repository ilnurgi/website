android.widget.EditText
=======================

XML
---

.. code-block:: xml

    <EditText
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:layout_marginRight="5pt"
        android:layout_width="match_parent"

        android:inputType="numberDecimal"
        android:id="@+id/etNum1" />

* id - идентификатор элемента

* inputType - тип вводимых символов

    * numberDecimal - только цифры и запятая

EditText
--------

.. py:class:: android.widget.EditText

    Редактируемое поле для ввода текста.

    Поддерживает многострочный ввод, перенос слов на новую строку и текст подсказки.

    Наследник :ref:`android.view.View`.