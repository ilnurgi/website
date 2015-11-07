.. py:module:: pymongo.read_preferences

read_preferences – Utilities for choosing which member of a replica set to read from.
=====================================================================================

Utilities for choosing which member of a replica set to read from.


Primary
-------

.. py:class:: Primary
	
	Primary read preference.

	* When directly connected to one mongod queries are allowed if the server is standalone or a replica set primary.
	* When connected to a mongos queries are sent to the primary of a shard.
	* When connected to a replica set queries are sent to the primary of the replica set.

	
	.. py:attribute:: document
		
		Read preference as a document.


	.. py:attribute:: mode
		
		The mode of this read preference instance.


	.. py:attribute:: name
		
		The name of this read preference.


	.. py:attribute:: tag_sets

		Set tag_sets to a list of dictionaries like [{‘dc’: ‘ny’}] to read only from members whose dc tag has the value "ny". To specify a priority-order for tag sets, provide a list of tag sets: [{'dc': 'ny'}, {'dc': 'la'}, {}]. A final, empty tag set, {}, means “read from any member that matches the mode, ignoring tags.” MongoReplicaSetClient tries each set of tags in turn until it finds a set of tags with at least one matching member.


PrimaryPreferred
----------------

.. py:class:: PrimaryPreferred(tag_sets=None)
	
	PrimaryPreferred read preference.

	* When directly connected to one mongod queries are allowed to standalone servers, to a replica set primary, or to replica set secondaries.
	* When connected to a mongos queries are sent to the primary of a shard if available, otherwise a shard secondary.
	* When connected to a replica set queries are sent to the primary if available, otherwise a secondary.

	* `tag_sets` - The tag_sets to use if the primary is not available.


	.. py:attribute:: document
			
		Read preference as a document.

	
	.. py:attribute:: mode
	
		The mode of this read preference instance.

	
	.. py:attribute:: name
		
		The name of this read preference.


	.. py:attribute:: tag_sets
		
		Set tag_sets to a list of dictionaries like [{‘dc’: ‘ny’}] to read only from members whose dc tag has the value "ny". To specify a priority-order for tag sets, provide a list of tag sets: [{'dc': 'ny'}, {'dc': 'la'}, {}]. A final, empty tag set, {}, means “read from any member that matches the mode, ignoring tags.” MongoReplicaSetClient tries each set of tags in turn until it finds a set of tags with at least one matching member.


Secondary
---------

.. py:class:: Secondary(tag_sets=None)
		
	Secondary read preference.

	* When directly connected to one mongod queries are allowed to standalone servers, to a replica set primary, or to replica set secondaries.
	* When connected to a mongos queries are distributed among shard secondaries. An error is raised if no secondaries are available.
	* When connected to a replica set queries are distributed among secondaries. An error is raised if no secondaries are available.

	* `tag_sets` - The tag_sets to use with this read_preference

	.. py:attribute:: document
		
		Read preference as a document.


	.. py:attribute:: mode
		
		The mode of this read preference instance.

	
	.. py:attribute:: name
		
		The name of this read preference.


	.. py:attribute:: tag_sets
		
		Set tag_sets to a list of dictionaries like [{‘dc’: ‘ny’}] to read only from members whose dc tag has the value "ny". To specify a priority-order for tag sets, provide a list of tag sets: [{'dc': 'ny'}, {'dc': 'la'}, {}]. A final, empty tag set, {}, means “read from any member that matches the mode, ignoring tags.” MongoReplicaSetClient tries each set of tags in turn until it finds a set of tags with at least one matching member.


SecondaryPreferred
------------------

.. py:class:: SecondaryPreferred(tag_sets=None)
		
	SecondaryPreferred read preference.

	* When directly connected to one mongod queries are allowed to standalone servers, to a replica set primary, or to replica set secondaries.
	* When connected to a mongos queries are distributed among shard secondaries, or the shard primary if no secondary is available.
	* When connected to a replica set queries are distributed among secondaries, or the primary if no secondary is available.

	* `tag_sets` - The tag_sets to use with this read_preference

	.. py:attribute:: document
		
		Read preference as a document.


	.. py:attribute:: mode
		
		The mode of this read preference instance.


	.. py:attribute:: name
		
		The name of this read preference.


	.. py:attribute:: tag_sets

		Set tag_sets to a list of dictionaries like [{‘dc’: ‘ny’}] to read only from members whose dc tag has the value "ny". To specify a priority-order for tag sets, provide a list of tag sets: [{'dc': 'ny'}, {'dc': 'la'}, {}]. A final, empty tag set, {}, means “read from any member that matches the mode, ignoring tags.” MongoReplicaSetClient tries each set of tags in turn until it finds a set of tags with at least one matching member.


Nearest
-------

.. py:class:: Nearest(tag_sets=None)
	
	Nearest read preference.

	* When directly connected to one mongod queries are allowed to standalone servers, to a replica set primary, or to replica set secondaries.
	* When connected to a mongos queries are distributed among all members of a shard.
	* When connected to a replica set queries are distributed among all members.

	* `tag_sets` - The tag_sets to use with this read_preference

	.. py:attribute:: document
		
		Read preference as a document.


	.. py:attribute:: mode
		
		The mode of this read preference instance.


	.. py:attribute:: name
		
		The name of this read preference.


	.. py:attribute:: tag_sets
		
		Set tag_sets to a list of dictionaries like [{‘dc’: ‘ny’}] to read only from members whose dc tag has the value "ny". To specify a priority-order for tag sets, provide a list of tag sets: [{'dc': 'ny'}, {'dc': 'la'}, {}]. A final, empty tag set, {}, means “read from any member that matches the mode, ignoring tags.” MongoReplicaSetClient tries each set of tags in turn until it finds a set of tags with at least one matching member.


ReadPreference
--------------

.. py:class:: ReadPreference
	
	An enum that defines the read preference modes supported by PyMongo.

	A read preference is used in three cases:

	:py:class:`pymongo.mongo_client.MongoClient` connected to a single mongod:

		* `PRIMARY` - Queries are allowed if the server is standalone or a replica set primary.
		* All other modes allow queries to standalone servers, to a replica set primary, or to replica set secondaries.

	:py:class:`pymongo.mongo_client.MongoClient` initialized with the replicaSet option:

		* `PRIMARY` - Read from the primary. This is the default, and provides the strongest consistency. If no primary is available, raise AutoReconnect.
		* `PRIMARY_PREFERRED` - Read from the primary if available, or if there is none, read from a secondary.
		* `SECONDARY` - Read from a secondary. If no secondary is available, raise AutoReconnect.
		* `SECONDARY_PREFERRED` - Read from a secondary if available, otherwise from the primary.
		* `NEAREST` - Read from any member.

	MongoClient connected to a mongos, with a sharded cluster of replica sets:

		* `PRIMARY` - Read from the primary of the shard, or raise OperationFailure if there is none. This is the default.
		* `PRIMARY_PREFERRED` - Read from the primary of the shard, or if there is none, read from a secondary of the shard.
		* `SECONDARY` - Read from a secondary of the shard, or raise OperationFailure if there is none.
		* `SECONDARY_PREFERRED` - Read from a secondary of the shard if available, otherwise from the shard primary.
		* `NEAREST` - Read from any shard member.


.. py:attribute:: PRIMARY = Primary()


.. py:attribute:: PRIMARY_PREFERRED = PrimaryPreferred(tag_sets=None)


.. py:attribute:: SECONDARY = Secondary(tag_sets=None)


.. py:attribute:: SECONDARY_PREFERRED = SecondaryPreferred(tag_sets=None)


.. py:attribute:: NEAREST = Nearest(tag_sets=None)