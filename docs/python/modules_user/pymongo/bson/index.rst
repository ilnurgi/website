.. py:module:: bson

bson - бинарный json
====================


BSON
----

.. py:class:: class BSON()
	
	BSON (Binary JSON) data.


	.. py:method:: encode(document, check_keys=False, codec_options=CodecOptions(document_class=dict, tz_aware=False, uuid_representation=PYTHON_LEGACY))
		
		Кодирует данные, словарь, в BSON формат

		* `document` - данные для кодирования
		* `check_keys` - опционально, проверка ключей на валидность
		* `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`, настройка кодирования

	
	.. py:method:: decode(codec_options=CodecOptions(document_class=dict, tz_aware=False, uuid_representation=PYTHON_LEGACY))
		
		Вовзвращает декодированный json, словарь

		* `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`, настройка кодека декодирования

		>>> import collections
		>>> import bson
		>>> from bson.codec_options import CodecOptions
		>>> data = bson.BSON.encode({'a': 1})
		>>> decoded_doc = bson.BSON.decode(data)
		<type 'dict'>
		>>> options = CodecOptions(document_class=collections.OrderedDict)
		>>> decoded_doc = bson.BSON.decode(data, codec_options=options)
		>>> type(decoded_doc)
		<class 'collections.OrderedDict'>


	.. py:method:: decode_all(data, codec_options=CodecOptions(document_class=dict, tz_aware=False, uuid_representation=PYTHON_LEGACY))
		
		Декодирует несколько данных

		* `data` - BSON данные
		* `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`, настройка кодека декодирования


	.. py:method:: decode_file_iter(file_obj, codec_options=CodecOptions(document_class=dict, tz_aware=False, uuid_representation=PYTHON_LEGACY))
		
		Декодирует bson данные из файла кусками

		* `file_obj` - файловый объект
		* `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`, настройка кодека декодирования


	.. py:method:: decode_iter(data, codec_options=CodecOptions(document_class=dict, tz_aware=False, uuid_representation=PYTHON_LEGACY))

		Декодирует BSON данные из файла

		* `data` - BSON данные
		* `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`, настройка кодека декодирования


	.. py:method:: gen_list_name()
		
		Генерирует ключи для кодированного списка

	
	.. py:method:: has_c()
		
		Расширение на С


	.. py:method:: is_valid(bson)
		
		Проверяет bson данные на валидность


Содержание модуля
-----------------

.. toctree::
   :maxdepth: 1

   binary
   code
   codec_options
   dbref
   errors
   int64
   json_util
   max_key
   min_key
   objectid
   regex
   son
   timestamp
   tz_util