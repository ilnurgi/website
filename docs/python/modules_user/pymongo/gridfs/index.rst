.. py:module:: gridfs

gridfs - спецификация для хранения больших объектов в MongoDB
=============================================================


GridFS
------

.. py:class:: GridFS(database, collection='fs')

   Объект для работы с GridFS
   
   * `database` - :py:class:`pymongo.database.Database`
   * `collection` - опционально, коллекция в БД


   .. py:method:: delete(file_id)
   
      Удаляет файл из бд

      .. warning:: 

         если при удалении, кто-то попытается прочесть файл, то он может прочитать и не весь файл

      .. note:: 

         Удаление не существующего файла не считается ошибкой


   .. py:method:: exists(document_or_id=None, **kwargs)
      
      Булево, файл существует

      >>> fs.exists(file_id)
      >>> fs.exists({"_id": file_id})
      >>> fs.exists(_id=file_id)
      >>> fs.exists({"filename": "mike.txt"})
      >>> fs.exists(filename="mike.txt")
      >>> fs.exists({"foo": {"$gt": 12}})
      >>> fs.exists(foo={"$gt": 12})

   
   .. py:method:: find(*args, **kwargs)

      Возвращает курсор :py:class:`gridfs.grid_file.GridOutCursor` итератор по найденным файлам.

      * `filter` - опционально, фильтр для поиска
      * `skip` - опционально, количесвто файлов которые надо пропустить
      * `limit` - опционально, количесвто документов которые надо вернуть
      * `no_cursor_timeout` - опционально, булево, если ложно (по умолчанию) то курсов закрывается по истечении 10 минут неактивности  сервера БД. 
      * `sort` - опционально, список ключей для сортировки

      .. code-block:: py
          
         for grid_out in fs.find({"filename": "lisa.txt"}, no_cursor_timeout=True):
            data = grid_out.read()

         most_recent_three = fs.find().sort("uploadDate", -1).limit(3)


   .. py:method:: find_one(filter=None, *args, **kwargs)
      
      Возвращает один файл по условию, аргументы аналогичны :py:meth:`find()`

      >>> file = fs.find_one({"filename": "lisa.txt"})


   .. py:method:: get(file_id)
      
      Возвращает файл по идентификатору


   .. py:method:: get_last_version(filename=None, **kwargs)
      
      Возвращает последнюю версию файла


   .. py:method:: get_version(filename=None, version=-1, **kwargs)
   
      Возвращает файл указанной версии

      Возбуждает :py:class:`gridfs.errors.NoFile` если файл не найден


   .. py:method:: list()
      
      Список всех файлов БД


   .. py:method:: new_file(**kwargs)
      
      Возвращает :py:class:`gridfs.grid_file.GridIn`, ново созданный файл в БД

   
   .. py:method:: put(data, **kwargs)
      
      Кладет новую информацю в файл

      * `data` - строка или файлобый объект

      .. code-block:: py
          
         try:
            f = new_file(**kwargs)
            f.write(data)
         finally:
            f.close()

Объекты модуля
--------------

.. toctree::
   :maxdepth: 1

   errors
   grid_file