.. py:module:: bson.json_util

json_util – инструмент для использования Python json модуля с BSON документами
==============================================================================

Данный модуль предоставляет два вспомогательных метода для преобразования json в BSON объекты.

.. code-block:: py
        
	from bson import Binary, Code
	from bson.json_util import dumps

	dumps([{'foo': [1, 2]},
	       {'bar': {'hello': 'world'}},
	       {'code': Code("function x() { return 1; }")},
	       {'bin': Binary("")}])
	# '[{"foo": [1, 2]}, {"bar": {"hello": "world"}}, {"code": {"$code": "function x() { return 1; }", "$scope": {}}}, {"bin": {"$binary": "AQIDBA==", "$type": "00"}}]'

.. code-block:: py

	from bson.json_util import loads
	loads('[{"foo": [1, 2]}, {"bar": {"hello": "world"}}, {"code": {"$scope": {}, "$code": "function x() { return 1; }"}}, {"bin": {"$type": "00", "$binary": "AQIDBA=="}}]')
	# [{u'foo': [1, 2]}, {u'bar': {u'hello': u'world'}}, {u'code': Code('function x() { return 1; }', {})}, {u'bin': Binary('...', 0)}]


.. py:method:: default(obj)


.. py:method:: dumps(obj, *args, **kwargs)
	
	Враппер над json.dumps.


.. py:method:: loads(s, *args, **kwargs)
	
	Враппер json.loads.

	
.. py:method:: object_hook(dct)