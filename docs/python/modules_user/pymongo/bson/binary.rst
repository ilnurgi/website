.. py:module:: bson.binary

binary
======

.. py:attribute:: BINARY_SUBTYPE = 0
	
	BSON формат стандартный


.. py:attribute:: FUNCTION_SUBTYPE = 1
	
	BSON формат для функции


.. py:attribute:: OLD_BINARY_SUBTYPE = 2
	
	Старый BSON формат


.. py:attribute:: OLD_UUID_SUBTYPE = 3
	
	Старый BSON формат для UUID.


.. py:attribute:: UUID_SUBTYPE = 4
	
	BSON формат для UUID.


.. py:attribute:: STANDARD = 4
	
	Стандартный UUID представление


.. py:attribute:: PYTHON_LEGACY = 3
	
	Старое Python UUID представление


.. py:attribute:: JAVA_LEGACY = 5
	
	Старое Java UUID представление


.. py:attribute:: CSHARP_LEGACY = 6
	
	Старое C#/.net UUID представление


.. py:attribute:: MD5_SUBTYPE = 5
	
	BSON формат для MD5


.. py:attribute:: USER_DEFINED_SUBTYPE = 128
	
	BSON формат для пользоватлеьских данных


Binary
------

.. py:class:: Binary(data, subtype=BINARY_SUBTYPE)
	
	Наследние str

	BSON представление данных

	* `data` - бинарное представление данных
	* `subtype` - опционально, формат представление данных


	.. py:attribute:: subtype

		Формат представления данных


UUIDLegacy
----------

.. py:class:: UUIDLegacy(obj)
	
	Наследник :py:class:`bson.binary.Binary`

	UUID враппер для поддержки работы с UUID хранящий PYTHON_LEGACY.

	>>> import uuid
	>>> from bson.binary import Binary, UUIDLegacy, STANDARD
	>>> from bson.codec_options import CodecOptions
	>>> my_uuid = uuid.uuid4()
	>>> coll = db.get_collection('test',
	...                          CodecOptions(uuid_representation=STANDARD))
	>>> coll.insert_one({'uuid': Binary(my_uuid.bytes, 3)}).inserted_id
	ObjectId('...')
	>>> coll.find({'uuid': my_uuid}).count()
	0
	>>> coll.find({'uuid': UUIDLegacy(my_uuid)}).count()
	1
	>>> coll.find({'uuid': UUIDLegacy(my_uuid)})[0]['uuid']
	UUID('...')
	>>>
	>>> # Convert from subtype 3 to subtype 4
	>>> doc = coll.find_one({'uuid': UUIDLegacy(my_uuid)})
	>>> coll.replace_one({"_id": doc["_id"]}, doc).matched_count
	1
	>>> coll.find({'uuid': UUIDLegacy(my_uuid)}).count()
	0
	>>> coll.find({'uuid': {'$in': [UUIDLegacy(my_uuid), my_uuid]}}).count()
	1
	>>> coll.find_one({'uuid': my_uuid})['uuid']
	UUID('...')

	.. py:attribute:: uuid
		
		UUID экземпляр обернутый
		