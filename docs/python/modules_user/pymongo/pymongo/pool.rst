.. py:module:: pymongo.pool

pool - Pool module for use with a MongoDB client.
=================================================

.. py:class:: SocketInfo(sock, pool, ismaster, address)
	
	Store a socket with some metadata.

	* `sock` - a raw socket object

	* `pool` - a Pool instance

	* `ismaster` - optional IsMaster instance, response to ismaster on sock

	* `address` - the server’s (host, port)

	
	.. py:method:: authenticate(credentials)
		
		Log in to the server and store these credentials in authset.

		Can raise ConnectionFailure or OperationFailure.

		* `credentials` - A MongoCredential.


	.. py:method:: check_auth(all_credentials)
		
		Update this socket’s authentication.

		Log in or out to bring this socket’s credentials up to date with those provided. Can raise ConnectionFailure or OperationFailure.

		* `all_credentials` - dict, maps auth source to MongoCredential.


	.. py:method:: command(dbname, spec, slave_ok=False, read_preference=Primary(), codec_options=CodecOptions(document_class=dict, tz_aware=False, uuid_representation=PYTHON_LEGACY), check=True, allowable_errors=None)
		
		Execute a command or raise ConnectionFailure or OperationFailure.

		* `dbname` - name of the database on which to run the command

		* `spec` - a command document as a dict, SON, or mapping object

		* `slave_ok` - whether to set the SlaveOkay wire protocol bit

		* `read_preference` - a read preference

		* `codec_options` - a CodecOptions instance

		* `check` - raise OperationFailure if there are errors

		* `allowable_errors` - errors to ignore if check is True


	.. py:method:: legacy_write(request_id, msg, max_doc_size, with_last_error)
		
		Send OP_INSERT, etc., optionally returning response as a dict.

		Can raise ConnectionFailure or OperationFailure.

		* `request_id` - an int.

		* `msg` - bytes, an OP_INSERT, OP_UPDATE, or OP_DELETE message, perhaps with a getlasterror command appended.

		* `max_doc_size` - size in bytes of the largest document in msg.

		* `with_last_error` - True if a getlasterror command is appended.

	
	.. py:method:: receive_message(operation, request_id)
		
		Receive a raw BSON message or raise ConnectionFailure.

		If any exception is raised, the socket is closed.


	.. py:method:: send_message(message, max_doc_size)
		
		Send a raw BSON message or raise ConnectionFailure.

		If a network exception is raised, the socket is closed.


	.. py:method:: write_command(request_id, msg)
	
		Send “insert” etc. command, returning response as a dict.

		Can raise ConnectionFailure or OperationFailure.

		* `request_id` - an int.

		* `msg` - bytes, the command message.
