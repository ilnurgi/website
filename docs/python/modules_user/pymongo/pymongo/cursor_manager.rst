.. py:module:: cursor_manager

cursor_manager – Managers to handle when cursors are killed after being closed
==============================================================================

A manager to handle when cursors are killed after they are closed.

New cursor managers should be defined as subclasses of CursorManager and can be installed on a client by calling set_cursor_manager().


.. py:class:: CursorManager(client)
	
	Instantiate the manager.

	* `client` - :py:class:`pymongo.mongo_client.MongoClient`


	.. py:method:: close(cursor_id, address)
		
		Kill a cursor.

		Raises TypeError if cursor_id is not an instance of (int, long).

		* `cursor_id` - cursor id to close
		* `address` - the cursor’s server’s (host, port) pairs