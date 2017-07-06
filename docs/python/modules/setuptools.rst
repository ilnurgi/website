.. py:module:: setuptools

setuptools
==========

.. warning::

	Добавлено в python 3.4


.. code-block:: sh

	# создание файла установщика
	# на винде создаст .zip архив
	# в unix системах .tar.gz
	python setup.py sdist


.. py:method:: setup(**kwargs)

	* name - строка, название модуля
	* version - строка, версия модуля
	* description - строка, описание модуля
	* author - строка, автор модуля
	* author_email - строка, почта автора модуля
	* url - строка, домашняя страница модуля
	* py_modules - список скриптов, которые включает модуль
