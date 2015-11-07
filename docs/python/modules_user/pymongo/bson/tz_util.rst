.. py:module:: bson.tz_util

tz_util – Utilities for dealing with timezones in Python
========================================================

Timezone related utilities for BSON.

.. py:class:: FixedOffset(offset, name)
		
	Fixed offset timezone, in minutes east from UTC.

	Implementation based from the Python standard library documentation. Defining __getinitargs__ enables pickling / copying.


bson.tz_util.utc = <bson.tz_util.FixedOffset object at 0x7fdc52897ed0>

	Fixed offset timezone representing UTC.