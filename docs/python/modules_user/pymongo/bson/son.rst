.. py:module:: bson.son

son – Tools for working with SON, an ordered mapping
====================================================

Tools for creating and manipulating SON, the Serialized Ocument Notation.

Regular dictionaries can be used instead of SON objects, but not when the order of keys is important. A SON object can be used just like a normal Python dictionary.


.. py:class:: SON(data=None, **kwargs)
 
	SON data.

 	A subclass of dict that maintains ordering of keys and provides a few extra niceties for dealing with SON. SON objects can be converted to and from BSON.

 	The mapping from Python types to BSON types is as follows:

	====================== ============== ===================
	Python Type            BSON Type      Supported Direction
	====================== ============== ===================
	None                   null           both
	bool                   boolean        both
	int                    int32 / int64  py -> bson
	long                   int64          py -> bson
	bson.int64.Int64       int64          both
	float                  number (real)  both
	string                 string         py -> bson
	unicode                string         both
	list                   array          both
	dict / SON             object         both
	datetime.datetime      date           both
	bson.regex.Regex       regex          both
	compiled re            regex          py -> bson
	bson.binary.Binary     binary         both
	bson.objectid.ObjectId oid            both
	bson.dbref.DBRef       dbref          both
	None                   undefined      bson -> py
	unicode                code           bson -> py
	bson.code.Code         code           py -> bson
	unicode                symbol         bson -> py
	bytes (Python 3)       binary         both
	====================== ============== ===================

	Note that to save binary data it must be wrapped as an instance of bson.binary.Binary. Otherwise it will be saved as a BSON string and retrieved as unicode.

	.. py:method:: to_dict()
		
		Convert a SON document to a normal Python dictionary instance.

		This is trickier than just dict(...) because it needs to be recursive.