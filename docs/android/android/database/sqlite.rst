android.database.sqlite.SQLiteDatabase
======================================

Файл базы данных лежит /data/data/ru.ilnurgi1/databases/


.. py:class:: android.database.sqlite.SQLiteDatabase()


    .. py:method:: beginTransaction()

        Начинает транзакцияю

        Блокирует базу для чтения и записи для других подключений

        .. code-block:: java

            db.beginTransaction();
            // some code
            db.setTransactionSuccessful();
            db.endTransaction();

        .. code-block:: java

            db.beginTransaction();
            try {
                // some code
                db.setTransactionSuccessful();
            } finally {
                db.endTransaction();
            }


    .. py:method:: beginTransactionNonExclusive()

        Начинает транзакцияю

        Блокирует базу для записи для других подключений

        .. code-block:: java

            db.beginTransactionNonExclusive();


    .. py:method:: delete(String tableName, String selection, String[] selectionArgs)

        Удаляет записи из БД и возвращает количесвто удаленных записей

        .. code-block:: java

            int countDelete = db.delete("myTable", null, null);
            int countDelete = db.delete("myTable", "id="+id, null);


    .. py:method:: endTransaction()

        Завершает транзакцияю

        .. code-block:: java

            db.endTransaction();


    .. py:method:: getVersion()

        Возвращает int, версия БД

        .. code-block:: java

            int dbVersion = db.getVersion();


    .. py:method:: insert(String tableName, null, ContentValues cv)

        Добавляет запись в БД и возвращает его уникальный идентификатор

        .. code-block:: java

            ContentValues cv = new ContentValues();
            cv.put("name", "name");

            int createdRowId = db.insert("myTable", null, cv);


    .. py:method:: query(String tableName, String[] columns, String selection, String[] selectionArgs, String groupBy, String having, String orderBy)

        Возвращает курсор :py:class:`android.database.Cursor` выборка данных из БД

        .. code-block:: java

            Cursor c = db.query("mytable", null, null, null, null, null, null);
            Cursor c = db.query(
                "mytable as mt join some table as st on ...",
                null,
                null,
                null,
                null,
                null,
                null);

            if (c.moveToFirst()) {
                int nameColIndex = c.getColumnIndex("name");
                do {
                    String name = c.getString(nameColIndex)
                } while (c.moveToNext());
            }


    .. py:method:: rawQuery(String sqlQuery, String[] selectionArgs)

        Выполняет запрос на SQL, возвращает курсор :py:class:`android.database.Cursor`

        .. code-block:: java

            Cursor c = db.rawQuery("select ... where id = ?", new String[] {1});


    .. py:method:: setTransactionSuccessful()

        Подтверждение успешности транзакции, для комита изменении

        .. code-block:: java

            db.setTransactionSuccessful()


    .. py:method:: update(String tableName, ContentValues cv, String selection, String[] selectionArgs)

        Обновляет записи в БД и возвращает количество обновленных записей

        .. code-block:: java

            int ipdateCount = db.update("myTable", cv, "id=?", new String[] {id});




android.database.sqlite.SQLiteOpenHelper
========================================

.. py:class:: android.database.sqlite.SQLiteOpenHelper(Context context, String dbName, null, int dbVersion)

    Вспомогательный класс, для реализации работы с БД.

    .. code-block:: java

        class DBHelper extends SQLiteOpenHelper {}

        DBHelper helper = new DBHelper();


    .. py:method:: close()

        Закрывает подключение к БД

        .. code-block:: java

            helper.close();


    .. py:method:: getReadableDatabase()

        Подключается к бд и возвращает его :py:class:`android.database.sqlite.SQLiteDatabase`

        БД возвращается только для чтения

        .. code-block:: java

            SQLiteDatabase db = helper.getReadableDatabase()


    .. py:method:: getWritableDatabase()

        Подключается к бд и возвращает его :py:class:`android.database.sqlite.SQLiteDatabase`

        БД возвращается как для чтения так и для записи

        Если нет свободного места на устройстве, то вызовет исключение

        .. code-block:: java

            SQLiteDatabase db = helper.getWritableDatabase()


    .. py:method:: onCreate(SqliteDatabase db)

        Обработчик создания БД, если его нет

        * db - :py:class:`android.database.sqlite.SQLiteDatabase`

        .. code-block:: java

            @Override
            public void onCreate(SQLiteDatabase db) {
                db.execSQL();
            }


    .. py:method:: onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion)

        Обработчик обновления БД, если версия изменилась

        .. code-block:: java

            @Override
            public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
                db.execSQL();
            }




