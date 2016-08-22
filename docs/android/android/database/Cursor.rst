android.database.Cursor
=======================

.. py:class:: android.database.Cursor()

    Для использования курсор адаптера, таблица должно иметь поле `_id`

    .. py:method:: getColumnIndex(String columnName)

        Возвращает int, номер колонки по наименованию

        .. code-block:: java

            int columnIdIndex = cursor.getColumnIndex("id");


    .. py:method:: getColumnNames()

        Возвращает String[] названия колонок

        .. code-block:: java

            String[] columnNames = cursor.getColumnNames();


    .. py:method:: getInt(int columnIndex)

        Возвращает int, значение поля

        .. code-block:: java

            int id = cursor.getInt(columnIdIndex);


    .. py:method:: getString(int columnIndex)

        Возвращает String, значение поля

        .. code-block:: java

            String name = cursor.getString(columnNameIndex);


    .. py:method:: moveToFirst()

        Ставит курсор на первую позицию и возвращает статус

        Если данных нет, вернет false

        .. code-block:: java

            cursor.moveToFirst();


    .. py:method:: moveToNext()

        Ставит курсор на следующую позицию и возвращает статус

        Если данных нет, вернет false

        .. code-block:: java

            cursor.moveToNext();

