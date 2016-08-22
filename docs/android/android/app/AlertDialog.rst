android.app.AlertDialog
=======================

.. py:class:: android.app.AlertDialog()


AlertDialog.Builder
-------------------

.. py:class:: android.app.AlertDialog.Builder()

    .. code-block:: java

        Builder adb = new Builder(context);


    .. py:method:: create()

        Возвращает готовый к показу диалог


    .. py:method:: setCancelable(boolean mode)

        Закрывать диалог кнопкой назад


    .. py:method:: setIcon(int id)

        Иконка

        * android.R.drawable.ic_dialog_info


    .. py:method:: setMessage(String message)

        Сообщение


    .. py:method:: setNegativeButton(int stringId, OnClickListener listener)

        Добаляем кнопку отрицательного ответа с обработчиком

        * listener - :py:class:`android.content.DialogInterface.OnClickListener`

        .. code-block:: java

            adb.setNegativeButton(R.string.yes, new OnClickListener(){});


    .. py:method:: setNeutralButton(int stringId, OnClickListener listener)

        Добаляем кнопку отрицательного ответа с обработчиком

        * listener - :py:class:`android.content.DialogInterface.OnClickListener`

        .. code-block:: java

            adb.setNeutralButton(R.string.yes, new OnClickListener(){});


    .. py:method:: setPositiveButton(int stringId, OnClickListener listener)

        Добаляем кнопку положительного ответа с обработчиком

        * listener - :py:class:`android.content.DialogInterface.OnClickListener`

        .. code-block:: java

            adb.setPositiveButton(R.string.yes, new OnClickListener(){});


    .. py:method:: setTitle(int id)

        Заголовк