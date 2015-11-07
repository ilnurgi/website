.. py:module:: pymongo.son_manipulator

son_manipulator – Manipulators that can edit SON documents as they are saved or retrieved
=========================================================================================

Manipulators that can edit SON objects as they enter and exit a database.

New manipulators should be defined as subclasses of SONManipulator and can be installed on a database by calling pymongo.database.Database.add_son_manipulator.


AutoReference
-------------

.. py:class:: AutoReference(db)
	
	Transparently reference and de-reference already saved embedded objects.

	This manipulator should probably only be used when the NamespaceInjector is also being used, otherwise it doesn’t make too much sense - documents can only be auto-referenced if they have an _ns field.

	.. note:

		1. this will behave poorly if you have a circular reference.
		2. this only works for documents that are in the same database. To fix this we’ll need to add a DatabaseInjector that adds _db and then make use of the optional database support for DBRefs.


	.. py:method:: transform_incoming(son, collection)
	
		Replace embedded documents with DBRefs.


	.. py:method:: transform_outgoing(son, collection)
		
		Replace DBRefs with embedded documents.

	
	.. py:method:: will_copy()
	
		We need to copy so the user’s document doesn’t get transformed refs.


NamespaceInjector
-----------------

.. py:class:: NamespaceInjector

	A son manipulator that adds the _ns field.

	
	.. py:method:: transform_incoming(son, collection)
		
		Add the _ns field to the incoming object


ObjectIdInjector
----------------

.. py:class:: ObjectIdInjector
	
	A son manipulator that adds the _id field if it is missing.


	.. py:method:: transform_incoming(son, collection)
		
		Add an _id field if it is missing.


ObjectIdShuffler
----------------

.. py:class:: ObjectIdShuffler
	
	A son manipulator that moves _id to the first position.

	
	.. py:method:: transform_incoming(son, collection)
		
		Move _id to the front if it’s there.

	
	.. py:method:: will_copy()
		
		We need to copy to be sure that we are dealing with SON, not a dict.


SONManipulator
--------------

.. py:class:: SONManipulator
	
	A base son manipulator.

	This manipulator just saves and restores objects without changing them.

	
	.. py:method:: transform_incoming(son, collection)
		
		Manipulate an incoming SON object.

		* `son` - the SON object to be inserted into the database
		* `collection` - the collection the object is being inserted into


	.. py:method:: transform_outgoing(son, collection)
		
		Manipulate an outgoing SON object.

		* `son` - the SON object being retrieved from the database
		* `collection` - the collection this object was stored in


	.. py:method:: will_copy()
		
		Will this SON manipulator make a copy of the incoming document?

		Derived classes that do need to make a copy should override this method, returning True instead of False. All non-copying manipulators will be applied first (so that the user’s document will be updated appropriately), followed by copying manipulators.