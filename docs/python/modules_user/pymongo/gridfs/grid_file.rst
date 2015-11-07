.. py:module:: grid_file

grid_file – инстурмент, для представления файлов, хранящихся в GridFS
=====================================================================


GridIn
------

.. py:class:: GridIn(root_collection, **kwargs)
	
	Файл в коллекции

	Данный класс не следуюет инстацировать, он возвращвется методами :py:class:`gridfs.GridFS`

	* `root_collection` - коллекция, в которой находится объект
	* `_id` - уникальный идентификатор объекта
	* `filename` - человеческое имя объекта
	* `contentType, content_type` - mime-type файла
	* `chunkSize, chunk_size` - chank размер, по умолчанию 255 kb
	* `encoding` - кодировка файла

	.. py:attribute:: _id
	
		Возвращает идентификатор объекта


	.. py:attribute:: chunk_size
		
		Возвращает размер chunk'a


	.. py:attribute:: closed
		
		Возвращает булево, файл уже закрыт


	.. py:attribute:: content_type
		
		Возвращает mime-type файла


	.. py:attribute:: filename
		
		Возвращает название файла


	.. py:attribute:: length
		
		Возвращает размер объекта, в байтах. Может быть получен только у закрытого файла.


	.. py:attribute:: md5
		
		Возвращает MD5 хеш файла. Может быть получен только у закрытого файла.

	
	.. py:attribute:: name
		
		Возвращает название файла


	.. py:attribute:: upload_date
	
		Дата добавления файла. Может быть получен только у закрытого файла.


	.. py:method:: close()
		
		Сохраняет все содержимое и закрывает файл


	.. py:method:: write(data)
		
		Записывает данные в файл.

		Данные могут быть представлены как в строковом формате так и в файлобым объектом.

		Из-за буферизации, даные запишутся в БД только после закрытия файла.


	.. py:method:: writelines(sequence)
		
		Записывает список строк в файл


GridOut
-------

.. py:class:: GridOut(root_collection, file_id=None, file_document=None)
	
	Прочтианный файл в :py:class:`gridfs.GridFS`

	Данный класс не следуюет инстацировать, он возвращвется методами :py:class:`gridfs.GridFS`
	
	* `root_collection` - коллекция, в котором находится файл
	* `file_id` - опционально, уникальный идентификатор объекта
	* `file_document` - опционально, сам файл


	.. py:attribute:: _id
		
		Возвращает уникальный идентификатор объекта

		
	.. py:attribute:: aliases
		
		Возвращает список алиасов на файл


	.. py:attribute:: chunk_size
		
		Возвращает размер chunk


	.. py:attribute:: content_type
		
		Возвращает mime-type объекта


	.. py:attribute:: filename
		
		Возвращает название файла


	.. py:attribute:: length
		
		Возвращает размер файла, в байтах


	.. py:attribute:: md5
		
		Возвращает MD5 хеш файла


	.. py:attribute:: metadata
		
		Возвращает метадату файла


	.. py:attribute:: name
		
		Возвращает название файла


	.. py:attribute:: upload_date
		
		Возвращает дату создания файла в БД

	
	.. py:method:: close()
		
		Make GridOut more generically file-like.


	.. py:method:: __iter__()

		Возвращает итератор объекта

	
	.. py:method:: read(size=-1)
		
		Читает дуказанное количесвто байтов из файла


	.. py:method:: readchunk()
		
		Читает данные из файла от укзанной позиции, размером чанка.

	
	.. py:method:: readline(size=-1)
		
		Читает указанное количесвто строк из файлаad


	.. py:method:: seek(pos, whence=0)
		
		Перемещает курсор чтени в указанное положение

		* `pos` - позиция, на которую необходимо переместиться
		* `whence` - опционально, откуда будем перемещаться
			* os.SEEK_SET - 0 - абсолютная позиция
			* os.SEEK_CUR - 1 - относительно текущей позиции
			* os.SEEK_END - 2 - относительно конца

	.. py:method:: tell()
	
		возвращает текущую позицию в файле


GridOutCursor
-------------

.. py:class:: GridOutCursor(collection, filter=None, skip=0, limit=0, no_cursor_timeout=False, sort=None)
		
	Возвращает новый курсор, похожий на :py:class:`pymongo.cursor.Cursor`

	Не должен инстацироватьсся, в получется методом :py:meth:`gridfs.GridFS.find()`


	.. py:method:: next()
		
		Возвращает следующий объект