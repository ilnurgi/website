.. py:module:: pymongo.operations

operations - классы для операции
================================


DeleteOne
---------

.. py:class:: DeleteOne(filter)

	Операция удаления одного документа по фильтру. Для использования :py:meth:`pymongo.collection.Collection.bulk_write()`


DeleteMany
----------

.. py:class:: DeleteMany(filter)

	Операция удаления документов по фильтру. Для использования :py:meth:`pymongo.collection.Collection.bulk_write()`
	

IndexModel
----------

.. py:class:: IndexModel(**kwargs)

	Операция создания индекса. Для использования :py:meth:`pymongo.collection.Collection.create_indexes()`

	* `keys` - ключ или ключи (ключ, сортировка)

	* `name` -  имя индекса, если не задан будет автосгенерировано

	* `unique` - булево, создать уникальные индексы

	* `background` - булево, создать индекс в фоне

	* `sparse` - булево, исключить из индекса документы, которые не имею индексируемое поле

	* `bucketSize` - для geoHaystack индексов. Number of documents to group together within a certain proximity to a given longitude and latitude.

	* `min` -  минимальное значение ключей GEO2D индексов.

	* `max` -  максимальное значение ключей GEO2D индексов.

	* `expireAfterSeconds` - число,  <int> Used to create an expiring (TTL) collection. MongoDB will automatically delete documents from this collection after <int> seconds. The indexed field must be a UTC datetime or the data will not expire.


	.. py:attribute:: document

		An index document suitable for passing to the createIndexes command.


InsertOne
---------

.. py:class:: InsertOne(document)
	
	Операция вставки одного документа. Для использования :py:meth:`pymongo.collection.Collection.bulk_write()`


	* `document` - документ для вставки


ReplaceOne
----------

.. py:class:: ReplaceOne(filter, replacement, upsert=False)
	
	Операция замены одного документа. Для использования :py:meth:`pymongo.collection.Collection.bulk_write()`

	* `filter` - запрос для выборки документов для замены

	* `replacement` - новый документ для замены

	* `upsert` - опционально, булево, создавать документ если ничего не найдено


UpdateMany
----------

.. py:class:: UpdateMany(filter, update, upsert=False)
	
	Операция замены документов. Для использования :py:meth:`pymongo.collection.Collection.bulk_write()`

	* `filter` - запрос для выборки обновляемых документов

	* `update` - запрос на изменение документо

	* `upsert` - опционально, булево, создавать документ если не найден


UpdateOne
---------

.. py:class:: UpdateOne(filter, update, upsert=False)

	Операция обновления одного документа. Для использования :py:meth:`pymongo.collection.Collection.bulk_write()`

	* `filter` - запрос для выборки обновляемого документа

	* `update` - запрос на изменение документо

	* `upsert` - опционально, булево, создавать документ если не найден
