.. py:module:: bson.errors

errors – Исключения, возбуждаемые в модуле
==========================================


BSONError
---------

.. py:class:: BSONError
	
	Базовый класс для всех BSON исключении


InvalidBSON
-----------

.. py:class:: InvalidBSON
	
	Возбуждается при создании BSON объекта из невалидных данных


InvalidDocument
---------------

.. py:class:: InvalidDocument
	
	Возбуждается при создании BSON объекта из невалидного документа


InvalidId
---------

.. py:class:: InvalidId
	
	Возбуждается при создании ObjectId из невалидных данных


InvalidStringData
-----------------

.. py:class:: InvalidStringData
	
	Возбуждается при декодировании строки содержащий не UTF8 данные