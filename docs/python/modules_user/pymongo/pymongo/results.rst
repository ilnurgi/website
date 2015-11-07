.. py:module:: pymongo.results

results - объекты результатов операции
======================================


BulkWriteResult
---------------

.. py:class:: BulkWriteResult(bulk_api_result, acknowledged)

    Результат выполнения массовой записи

    * `bulk_api_result` - данные записи

    * `acknowledged` - результат записи, если False, значит все операции записи возбудили ошибку :py:class:`pymongo.errors.InvalidOperation`


	.. py:attribute:: acknowledged
			
		Результат записи

		Данный атрибут будет иметь значение False при использовании WriteConcern(w=0), иначе True.

		.. note:: Если данный атрибут равен False, то все остальные атрибуты при чтении, будут возбуждать ошибку :py:class:`pymongo.errors.InvalidOperation`


	.. py:attribute:: bulk_api_result
			
		Данные записи


	.. py:attribute:: deleted_count
		
		Количесвто удаленных документов


	.. py:attribute:: inserted_count
		
		Количесвто добавленных документов


	.. py:attribute:: matched_count
		
		Количесвто документов, которые совпали при обновлении


	.. py:attribute:: modified_count
		
		Количесвто измененных документов


	.. py:attribute:: upserted_count
		
		Количество upserted документов


	.. py:attribute:: upserted_ids
		
		Список идентификатор upserted документов.


DeleteResult
------------

.. py:class:: DeleteResult(raw_result, acknowledged)
	
	Результат удаления, возвращается :py:class:`pymongo.collection.Collection.delete_one()` и :py:class:`pymongo.collection.Collection.delete_many()`


	.. py:attribute:: acknowledged
	
		Результат выполнения операции

		Данный атрибут будет иметь значение False при использовании WriteConcern(w=0), иначе True.

		.. note:: Если данный атрибут равен False, то все остальные атрибуты при чтении, будут возбуждать ошибку :py:class:`pymongo.errors.InvalidOperation`


	.. py:attribute:: deleted_count
	
		Количесвто удаленных документов


	.. py:attribute:: raw_result
	
		Результат выполнения опреации в сыром виде


InsertManyResult
----------------

.. py:class:: InsertManyResult(inserted_ids, acknowledged)
		
	Результат множественной вставки документов в БД. Возвращается :py:class:`pymongo.collection.Collection.insert_many()`.


	.. py:attribute:: acknowledged
		
		Результат выполнения операции

		Данный атрибут будет иметь значение False при использовании WriteConcern(w=0), иначе True.

		.. note:: Если данный атрибут равен False, то все остальные атрибуты при чтении, будут возбуждать ошибку :py:class:`pymongo.errors.InvalidOperation`


	.. py:attribute:: inserted_ids

		Список идентификатор вставленных документов


InsertOneResult
---------------

.. py:class:: InsertOneResult(inserted_id, acknowledged)
	
	Результат вставки одного документа в БД. Возвращается :py:class:`pymongo.collection.Collection.insert_one()`.


	.. py:attribute:: acknowledged
		
		Результат выполнения операции

		Данный атрибут будет иметь значение False при использовании WriteConcern(w=0), иначе True.

		.. note:: Если данный атрибут равен False, то все остальные атрибуты при чтении, будут возбуждать ошибку :py:class:`pymongo.errors.InvalidOperation`


	.. py:attribute:: inserted_id
		
		Идентификатор добавленного документа


UpdateResult
------------

.. py:class:: UpdateResult(raw_result, acknowledged)

	Результат обновления документов в БД. Возвращается :py:class:`pymongo.collection.Collection.update_one()`, :py:class:`pymongo.collection.Collection.update_many()`, и  :py:class:`pymongo.collection.Collection.replace_one()`.


	.. py:attribute:: acknowledged
		
		Результат выполнения операции

		Данный атрибут будет иметь значение False при использовании WriteConcern(w=0), иначе True.

		.. note:: Если данный атрибут равен False, то все остальные атрибуты при чтении, будут возбуждать ошибку :py:class:`pymongo.errors.InvalidOperation`


	.. py:attribute:: matched_count
		
		Количество документов, которое совпало с уловиями обновления


	.. py:attribute:: modified_count
		
		Количество измененных документов


	.. py:attribute:: raw_result
		
		Результат работы в сыром виде


	.. py:attribute:: upserted_id
		
		Идентификатор добавленного документа