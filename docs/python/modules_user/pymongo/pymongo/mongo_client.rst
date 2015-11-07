.. py:module:: pymongo.mongo_client

mongo_client - инстурмент для подключения к MongoDB
===================================================


.. py:class:: MongoClient(**kwargs)

	Клиент для монго

	Возбуждает :py:class:`pymongo.errors.ConnectionFailure`
	
	* `host` - опционально, имя хоста или IP адрес машины, на котором запущена БД

	* `port` - опционально, номер порта для подключения к БД

	* `document_class` - опционально, default class to use for documents returned from queries on this client
	
	* `tz_aware` - опционально, if True, datetime instances returned as values in a document by this MongoClient will be timezone aware (otherwise they will be naive)

	* `connect` - опционально, if True (the default), immediately begin connecting to MongoDB in the background. Otherwise connect on the first operation.

	* `maxPoolSize` - опционально, The maximum number of connections that the pool will open simultaneously. If this is set, operations will block if there are maxPoolSize outstanding connections from the pool. Defaults to 100. Cannot be 0.

	* `socketTimeoutMS` - (integer or None) Controls how long (in milliseconds) the driver will wait for a response after sending an ordinary (non-monitoring) database operation before concluding that a network error has occurred. Defaults to None (no timeout).

	* `connectTimeoutMS` - (integer or None) Controls how long (in milliseconds) the driver will wait during server monitoring when connecting a new socket to a server before concluding the server is unavailable. Defaults to 20000 (20 seconds).

	* `serverSelectionTimeoutMS` - (integer) Controls how long (in milliseconds) the driver will wait to find an available, appropriate server to carry out a database operation; while it is waiting, multiple server monitoring operations may be carried out, each controlled by connectTimeoutMS. Defaults to 30000 (30 seconds).
	
	* `waitQueueTimeoutMS` - (integer or None) How long (in milliseconds) a thread will wait for a socket from the pool if the pool has no free sockets. Defaults to None (no timeout).

	* `waitQueueMultiple` - (integer or None) Multiplied by maxPoolSize to give the number of threads allowed to wait for a socket at one time. Defaults to None (no limit).

	* `socketKeepAlive` - (boolean) Whether to send periodic keep-alive packets on connected sockets. Defaults to False (do not send keep-alive packets).

	Write Concern options. (Only set if passed. No default values.)

	* `w` - (integer or string) If this is a replica set, write operations will block until they have been replicated to the specified number or tagged set of servers. w=<int> always includes the replica set primary (e.g. w=3 means write to the primary and wait until replicated to two secondaries). Passing w=0 disables write acknowledgement and all other write concern options.
	
	* `wtimeout` - (integer) Used in conjunction with w. Specify a value in milliseconds to control how long to wait for write propagation to complete. If replication does not complete in the given timeframe, a timeout exception is raised.
	
	* `j` - If True block until write operations have been committed to the journal. Cannot be used in combination with fsync. Prior to MongoDB 2.6 this option was ignored if the server was running without journaling. Starting with MongoDB 2.6 write operations will fail with an exception if this option is used when the server is running without journaling.

	* `fsync` - If True and the server is running without journaling, blocks until the server has synced all data files to disk. If the server is running with journaling, this acts the same as the j option, blocking until write operations have been committed to the journal. Cannot be used in combination with j.

	Replica set keyword arguments for connecting with a replica set - either directly or via a mongos:
	
	* `replicaSet` - (string or None) The name of the replica set to connect to. The driver will verify that all servers it connects to match this name. Implies that the hosts specified are a seed list and the driver should attempt to find all members of the set. Defaults to None.
	
	* `read_preference`  - The read preference for this client. If connecting directly to a secondary then a read preference mode other than PRIMARY is required - otherwise all queries will throw AutoReconnect “not master”. See ReadPreference for all available read preference options. Defaults to PRIMARY.
	
	SSL configuration
	
	* `ssl` - If True, create the connection to the server using SSL. Defaults to False.
	
	* `ssl_keyfile` - The private keyfile used to identify the local connection against mongod. If included with the certfile then only the ssl_certfile is needed. Implies ssl=True. Defaults to None.

	* `ssl_certfile` - The certificate file used to identify the local connection against mongod. Implies ssl=True. Defaults to None.
	
	* `ssl_cert_reqs` - Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided. It must be one of the three values ssl.CERT_NONE (certificates ignored), ssl.CERT_OPTIONAL (not required, but validated if provided), or ssl.CERT_REQUIRED (required and validated). If the value of this parameter is not ssl.CERT_NONE and a value is not provided for ssl_ca_certs PyMongo will attempt to load system provided CA certificates. If the python version in use does not support loading system CA certificates then the ssl_ca_certs parameter must point to a file of CA certificates. Implies ssl=True. Defaults to ssl.CERT_REQUIRED if not provided and ssl=True.
	
	* `ssl_ca_certs` - The ca_certs file contains a set of concatenated “certification authority” certificates, which are used to validate certificates passed from the other end of the connection. Implies ssl=True. Defaults to None.

	* `ssl_match_hostname` - If True (the default), and ssl_cert_reqs is not ssl.CERT_NONE, enables hostname verification using the match_hostname() function from python’s ssl module. Think very carefully before setting this to False as that could make your application vulnerable to man-in-the-middle attacks.


	.. py:attribute:: address

		Адрес машины к которой подключен клиент

	.. py:attribute:: is_locked
		
		Is this server locked? While locked, all write operations are blocked, although read operations may still be allowed. Use unlock() to unlock.


	.. py:attribute:: is_mongos

		If this client is connected to mongos.


	.. py:attribute:: is_primary

		Подключение к БД с поддержкой записи


	.. py:attribute:: max_pool_size

		Максимальное число соединении с базой


	.. py:attribute:: nodes

		Список всех подключенных баз


	.. py:attribute:: max_bson_size
		
		Максимальный размер BSON объекта, по умолчанию 16 Мб


	.. py:attribute:: max_message_size
	
		The largest message the connected server accepts in bytes. Defaults to 32MB if not connected to a server.

	
	.. py:attribute:: local_threshold_ms
	
		The local threshold for this instance.

	
	.. py:attribute:: codec_options
		
		Read only access to the CodecOptions of this instance.

	
	.. py:attribute:: read_preference
	
		Read only access to the read preference of this instance.


	.. py:attribute:: write_concern
		
		Read only access to the WriteConcern of this instance.

	
	.. py:method:: close()

		Закрывает все соединения с базой

	
	.. py:method:: database_names()
		
		Список имен всех баз сервера


	.. py:method:: drop_database(name_or_database)
		
		Удаляет базу с сервера
	

	.. py:method:: get_default_database()
		
		Возвращает название дефолтной БД

		>>> uri = 'mongodb://host/my_database'
		>>> client = MongoClient(uri)
		>>> client.get_default_database()


	.. py:method:: get_database(name, codec_options=None, read_preference=None, write_concern=None)
		
		Возвращает указанную БД

		* `name` - название БД
		
		* `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`
		
		* `read_preference` - опционально, настройки чтения 
		
		* `write_concern` - опционально, :py:class:`pymongo.write_concern.WriteConcern`

		>>> client.read_preference
		Primary()
		>>> db1 = client.test
		>>> db1.read_preference
		Primary()
		>>> from pymongo import ReadPreference
		>>> db2 = client.get_database(
		...     'test', read_preference=ReadPreference.SECONDARY)
		>>> db2.read_preference
		Secondary(tag_sets=None)


	.. py:method:: server_info()
		
		Возвращает информацию о подключенном сервере


	.. py:method:: close_cursor(cursor_id, address=None)
		
		Закрывает указанное соединение с БД

		* `cursor_id` - идентификатор курсора

		* `address` - опционально, (host, port) подеключения курсора


	.. py:method:: kill_cursors(cursor_ids, address=None)
		
		Отправляет сообщение на убитие курсоров

		This method may be called from a Cursor destructor during garbage collection, so it isn’t safe to take a lock or do network I/O. Instead, we schedule the cursor to be closed soon on a background thread.

		* `cursor_id` - идентификатор курсора

		* `address` - опционально, (host, port) подеключения курсора

	
	.. py:method:: set_cursor_manager(manager_class)
		
		Устанавливает новый менеджер для курсора. Менеджер должен быть наследником :py:class:`pymongo.cursor_manager.CursorManager`

	
	.. py:method:: fsync(**kwargs)
		
		Сбрасывает все данные в БД

		* `lock` - блокирует сервер на запись

		* `async` - If True don’t block while synchronizing.

		.. warning::

			1. параметры не используются совместно
			2. MongoDB не поддерживает `async` в Windows

	
	.. py:method:: unlock()
		
		Убирает лок с сервера
