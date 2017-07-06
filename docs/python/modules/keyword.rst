.. py:module:: keyword

keyword
=======


kwlist
------

.. py:attribute:: kwlist 

	Список ключевых слов

	.. code-block:: py

		keyword.kwlist
		"""
		['False',
		 'None',
		 'True',
		 'and',
		 'as',
		 'assert',
		 'break',
		 'class',
		 'continue',
		 'def',
		 'del',
		 'elif',
		 'else',
		 'except',
		 'finally',
		 'for',
		 'from',
		 'global',
		 'if',
		 'import',
		 'in',
		 'is',
		 'lambda',
		 'nonlocal',
		 'not',
		 'or',
		 'pass',
		 'raise',
		 'return',
		 'try',
		 'while',
		 'with',
		 'yield']
		"""


.. py: function:: iskeyword(value)

	Возвращает булево, если значеним является ключевое слово

	.. code-block:: py

		keyword.iskeyword('igi')
		# False
		
		keyword.iskeyword('with')
		# True
