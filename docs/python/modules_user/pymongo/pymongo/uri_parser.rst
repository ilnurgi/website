.. py:module:: pymongo.uri_parser

uri_parser – Tools to parse and validate a MongoDB URI
======================================================

Tools to parse and validate a MongoDB URI.

.. py:method:: parse_host(entity, default_port=27017)
	
	Validates a host string

	Returns a 2-tuple of host followed by port where port is default_port if it wasn’t specified in the string.

	* `entity` - A host or host:port string where host could be a hostname or IP address.
	* `default_port` - The port number to use when one wasn’t specified in entity.


.. py:method:: parse_ipv6_literal_host(entity, default_port)
	
	Validates an IPv6 literal host:port string.

	Returns a 2-tuple of IPv6 literal followed by port where port is default_port if it wasn’t specified in entity.

	* `entity` - A string that represents an IPv6 literal enclosed in braces (e.g. ‘[::1]’ or ‘[::1]:27017’).
	* `default_port` - The port number to use when one wasn’t specified in entity.


.. py:method:: parse_uri(uri, default_port=27017, validate=True)
	
	Parse and validate a MongoDB URI.
	
	Returns a dict of the form::

		{
		    'nodelist': <list of (host, port) tuples>,
		    'username': <username> or None,
		    'password': <password> or None,
		    'database': <database name> or None,
		    'collection': <collection name> or None,
		    'options': <dict of MongoDB URI options>
		}

	* `uri` - The MongoDB URI to parse.
	* `default_port` - The port number to use when one wasn’t specified for a host in the URI.
	* `validate` - If True (the default), validate and normalize all options.


.. py:method:: parse_userinfo(userinfo)
	
	Validates the format of user information in a MongoDB URI. Reserved characters like ‘:’, ‘/’, ‘+’ and ‘@’ must be escaped following RFC 2396.

	Returns a 2-tuple containing the unescaped username followed by the unescaped password.

	* `userinfo` - A string of the form <username>:<password>


.. py:method:: split_hosts(hosts, default_port=27017)
	
	Takes a string of the form host1[:port],host2[:port]... and splits it into (host, port) tuples. If [:port] isn’t present the default_port is used.

	Returns a set of 2-tuples containing the host name (or IP) followed by port number.

	* `hosts` - A string of the form host1[:port],host2[:port],...
	* `default_port` - The port number to use when one wasn’t specified for a host.


.. py:method:: split_options(opts, validate=True)
	
	Takes the options portion of a MongoDB URI, validates each option and returns the options in a dictionary.

	* `opt` - A string representing MongoDB URI options.
	* `validate` - If True (the default), validate and normalize all options.


.. py:method:: validate_options(opts)

	Validates and normalizes options passed in a MongoDB URI.

	Returns a new dictionary of validated and normalized options.

	* `opts` - A dict of MongoDB URI options.
