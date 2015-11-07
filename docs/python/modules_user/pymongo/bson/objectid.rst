.. py:module:: bson.objectid

objectid – инструмент для работы с ObjectId
===========================================

.. py:class:: ObjectId(oid=None)

	ObjectId это 12-байтовый уникальный идентификатор, содержащий:

		* 4-byte value representing the seconds since the Unix epoch,
		* 3-byte machine identifier,
		* 2-byte process id, and
		* 3-byte counter, starting with a random value.
	
	>>> ObjectId(b'foo-bar-quux')
	ObjectId('666f6f2d6261722d71757578')
	>>> ObjectId('0123456789ab0123456789ab')
	ObjectId('0123456789ab0123456789ab')
	>>> ObjectId(u'0123456789ab0123456789ab')
	ObjectId('0123456789ab0123456789ab')
	>>> o = ObjectId()
	>>> o == ObjectId(str(o))
	True


	.. py:attribute:: binary
		
		12-байтовое бинарное представление объекта

	
	.. py:classmethod:: from_datetime(generation_time)
		
		Create a dummy ObjectId instance with a specific generation time.

		This method is useful for doing range queries on a field containing ObjectId instances.

		generation_time will be converted to UTC. Naive datetime instances will be treated as though they already contain UTC.
		
		.. warning::

			It is not safe to insert a document containing an ObjectId generated using this method. This method deliberately eliminates the uniqueness guarantee that ObjectIds generally provide. ObjectIds generated with this method should be used exclusively in queries.

		>>> gen_time = datetime.datetime(2010, 1, 1)
		>>> dummy_id = ObjectId.from_datetime(gen_time)
		>>> result = collection.find({"_id": {"$lt": dummy_id}})


	.. py:attribute:: generation_time
		
		A datetime.datetime instance representing the time of generation for this ObjectId.

		The datetime.datetime is timezone aware, and represents the generation time in UTC. It is precise to the second.

	
	.. py:classmethod:: is_valid(oid)
		
		Checks if a oid string is valid or not.
