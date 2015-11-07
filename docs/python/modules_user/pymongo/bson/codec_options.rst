.. py:module:: bson.codec_options

codec_options - инструменты для настройки представления BSON
============================================================


.. py:class:: CodecOptions

    Содержит BSON опции использеумые в CRUD операциях


    * `document_class` - BSON documents returned in queries will be decoded to an instance of this class. Must be a subclass of MutableMapping. Defaults to dict.
    * `tz_aware` - Истина/ложь, даты с учтеом таймзоны
	* `uuid_representation` - Представление уникального идентификатора. По умолчанию :py:attr:`bson.binary.PYTHON_LEGACY`
	* `unicode_decode_error_handler` - The error handler to use when decoding an invalid BSON string. Valid options include ‘strict’, ‘replace’, and ‘ignore’. Defaults to ‘strict’.
	* `tzinfo` - A tzinfo subclass that specifies the timezone to/from which datetime objects should be encoded/decoded.
