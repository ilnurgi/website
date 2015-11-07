.. py:module:: database

database - БД
=============


Database
--------

.. py:class:: Database(**kwargs)

    База данных

    Возбуждает исключения:

        * `TypeError` - если имя не строка

        * `InvalidName` - :py:class:`pymongo.errors.InvalidName`

    Принимаемые параметры:

        * `client` - :py:class:`pymongo.mongo_client.MongoClient`

        * `name` - название БД

        * `codec_options` - :py:class:`bson.codec_options.CodecOptions`, необязательный

        * `read_preference` - необязательный, настройка чтения

        * `write_concern` - :py:class:`pymongo.write_concern.WriteConcern`, необязательный


    >>> import pymongo
    >>> connection = pymongo.MongoClient()
    >>> db = connection.my_db
    >>> db2 = connection['my_db']


    .. py:attribute:: client

        Возвращает клиента БД


    .. py:attribute:: codec_options

        Соотвествующее значение, только для чтения


    .. py:attribute:: incoming_copying_manipulators

        All incoming SON copying manipulators installed on this instance.


    .. py:attribute:: incoming_manipulators

        All incoming SON manipulators installed on this instance.


    .. py:attribute:: name

        Название БД


    .. py:attribute:: outgoing_copying_manipulators

        List all outgoing SON copying manipulators installed on this instance.


    .. py:attribute:: outgoing_manipulators

        List all outgoing SON manipulators installed on this instance.


    .. py:attribute:: read_preference

        Соотвествующее значение, только для чтения


    .. py:attribute:: system_js

        :py:class:`pymongo.database.SystemJS`, хелпер для БД


    .. py:attribute:: write_concern

        Соотвествующее значение, только для чтения



    .. py:method:: add_user(**kwargs)

        Добавляет нового пользователя.

        http://docs.mongodb.org/manual/reference/privilege-documents

        * `name` - имя пользователя
        * `password` - необязательно, пароль. Не используется с userSource
        * `read_only`- необязательно, пользователь может только читать
        * `userSource` -
        * `otherDBRoles`
        * `roles`


        .. note:: есили пользователь существует, меняет ему пароль


    .. py:method:: authenticate(kwargs)

        Авторизация

        * `name` - имя пользователя

        * `password` - необязательно, пароль пользователя. Не используется с GSSAPI или MONGODB-X509 авторизации.

        * `source` - необязательно, БД на которой происходит авторизация

        * `mechanism` - необязательно, механизмы авторизации, :py:attr:`pymongo.auth.MECHANISMS`

        * `authMechanismProperties` - необязательно, специфичные параметры для механизма авторизации

        Возбуждает исключения:

            * :py:class::`pymongo.errors.PyMongoError`


    .. py:method:: collection_names(include_system_collections=True)

        Возвращает список, коллекции БД.


    .. py:method:: command(kwargs)

        Вызывает команду MongoDB. Отправляет запрос в MongoDB и возвращает ответ.

        * `command` - команда.

            Может быть представлена строкой

            >>> db.command('buildinfo')
            # {buildinfo: 1}
            >>> db.command('collstats', collection_name)
            # {collstats: collection_name}
            >>> db.command('filemd5', object_id, root=file_root)
            # {filemd5: object_id, root: file_root}

            Или словарем, тогда она уйдет такой какая есть

            >>> db.command({'collstats': 'collection_name'})

        * `value` - необязательно, значение используемой командой

        * `check` - необязательно, проверить ответ на ошибки

        * `allowable_errors` - если `check=True` то ошибки из этого списка игнорируются

        * `read_preference` - читает предпочтения для текущего операции

        * `codec_options`


    .. py:method:: create_collection(kwargs)

        Возвращает коллекцию :py:class:`pymongo.collection.Collection`

        * `name` - название коллекции

        * `codec_options` - необязательное, :py:class:`bson.codec_options.CodecOptions`

        * `read_preference` - необязательное, настрйока чтения

        * `write_concern` - необязательное, :py:class:`pymongo.write_concern.WriteConcern`

        * `size` - начальный размер коллекции в байтах.

        * `capped` - булево, ограниченная коллекция

        * `max` - максимальное количество объектов в коллекции

        Возбуждает исключения:

        * :py:class::`pymongo.errors.CollectionInvalid`


    .. py:method:: current_op(include_all=False)

        Возвращает информацию о текущих операциях


    .. py:method:: dereference(kwargs)

        Разименовывает ссылку

        * `dbref` - :py:class:`bson.dbref.DBRef`


    .. py:method:: drop_collections(collection_name)

        Очищает коллекцию

        >>> db.drop_collections('users')


    .. py:method:: eval(code, *args)

        Исполняет JS код в БД

        Возбуждает исключения:

        * :py:class::`pymongo.errors.OperationFailure`


    .. py:method:: get_collection(name, codec_options=None, read_preference=None, write_concern=None)

        Возвращает коллекцию :py:class:`pymongo.collection.Collection` с указанными настройками.

        * `name` - название коллекции

        * `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`, если None то используется значение из БД

        * `read_preference` - опционально, настройки чтения, если None то используется значение из БД

        * `write_concern` - опционально, :py:class:`pymongo.write_concern.WriteConcern`, правила записи, если None то используется значение из БД

        >>> db.read_preference
        Primary()
        >>> coll1 = db.test
        >>> coll1.read_preference
        Primary()
        >>> from pymongo import ReadPreference
        >>> coll2 = db.get_collection(
        ...     'test', read_preference=ReadPreference.SECONDARY)
        >>> coll2.read_preference
        Secondary(tag_sets=None)


    .. py:method:: logout()

        Разавторизация.


    .. py:method:: profiling_info()

        Возвращает список с информацией о профилировщике


    .. py:method:: profiling_level()

        Возвращает уровень логирования БД:

            * :py:attr:`pymongo.OFF`
            * :py:attr:`pymongo.SLOW_ONY`
            * :py:attr:`pymongo.ALL`


    .. py:method:: remove_user(user_name)

        Удаляет пользователя из БД


    .. py:method:: set_profiling_level(level, slow_ms=None)

        Устанавливает уровень профилирования БД.

            * `level` - уровень

                * :py:attr:`pymongo.OFF`
                * :py:attr:`pymongo.SLOW_ONY`
                * :py:attr:`pymongo.ALL`

            * `slow_ms` - время работы запроса, по истечении которого он все равно запишется в журнал


    .. py:method:: validate_collection(name_or_collection, scandata=False, full=False)

        Валидация коллекции.

        Возвращает словарь, с информацией по валидации

        * `name_or_collection` - название или сама коллекция

        * `scandata` - выполнить доп проверки

        * `full` - более полная валидация


SystemJS
--------

.. py:class:: SystemJS(database)

    Позволяет манипулировать серверным JS кодом.

    Создавать экземпляр класса нет необходимости,
    т.к. он уже существует в самой БД
    :py:attr:`pymongo.database.Database.system_js`

    >>> db.system_js.add1 = "function (x) { return x + 1; }"
    >>> db.system.js.find({"_id": "add1"}).count()
    1
    >>> db.system_js.add1(5)
    6.0
    >>> del db.system_js.add1
    >>> db.system.js.find({"_id": "add1"}).count()
    0


    .. py:method:: list()

        Вовзращает список имен функции БД










