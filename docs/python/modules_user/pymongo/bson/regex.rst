.. py:module:: bson.regex

regex - инструмент для представления регулярок MongoDb
======================================================

.. py:class:: Regex(pattern, flags=0)

	BSON регулярное выражение хранения и извлечения регулярных выражений, которые не совместимы с питонячими регулярками
	
	* `pattern` - string
	* `flags` - опционально, битовая маска или строка “im” for IGNORECASE and MULTILINE

	.. py:classmethod:: from_native(regex)
		
		Возвращает ткласс регулярки, из полученной

		>>> pattern = re.compile('.*')
		>>> regex = Regex.from_native(pattern)
		>>> regex.flags ^= re.UNICODE
		>>> db.collection.insert({'pattern': regex})

	.. py:method:: try_compile()
		
		Возвращает питонячье регулярное выражение