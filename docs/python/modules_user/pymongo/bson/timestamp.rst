.. py:module:: bson.timestamp

timestamp – Tools for representing MongoDB internal Timestamps
==============================================================


.. py:class:: Timestamp(time, inc)
	
	Create a new Timestamp.

	This class is only for use with the MongoDB opLog. If you need to store a regular timestamp, please use a datetime.

	Raises TypeError if time is not an instance of :class: int or datetime, or inc is not an instance of int. Raises ValueError if time or inc is not in [0, 2**32).

	* `time` - time in seconds since epoch UTC, or a naive UTC datetime, or an aware datetime
	* `inc` - the incrementing counter

	.. py:method:: as_datetime()
		
		Return a datetime instance corresponding to the time portion of this Timestamp.

		The returned datetime’s timezone is UTC.

	.. py:attribute:: inc
		
		Get the inc portion of this Timestamp.


	.. py:attribute:: time
		
		Get the time portion of this Timestamp.