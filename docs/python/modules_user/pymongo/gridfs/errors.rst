.. py:module:: gridfs.errors

errors - ошибки, возбуждаемые в модуле
======================================

CorruptGridFile
---------------

.. py:class:: CorruptGridFile
	
	Возбуждается когда :py:class:`gridfs.GridFS` поврежден


FileExists
----------

.. py:class:: FileExists
	
	Возбуждается при создании уже существующего файла


GridFSError
-----------

.. py:class:: GridFSError
	
	Базовый класс для всех исключении моудля


NoFile
------

.. py:class:: NoFile
	
	Возбуждается когда файл не найден