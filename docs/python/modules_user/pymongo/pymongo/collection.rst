.. py:module:: pymongo.collection

collection - коллекции
======================

.. py:attribute:: ASCENDING = 1

    Сортировка по возрастанию


.. py:attribute:: DESCENDING = -1

    Сортировка по убыванию


.. py:attribute:: GEO2D = '2d'

    2d индекс


.. py:attribute:: GEOHAYSTACK = 'geoHaystack'

    geoHaystack индекс


.. py:attribute:: GEOSPHERE = '2dsphere'

    2dsphere индекс


.. py:attribute:: HASHED = 'hashed'

    hashed индекс


.. py:attribute:: TEXT = 'text'

    text индекс


ReturnDocument
--------------

.. py:class:: ReturnDocument

    Enum используемый в :py:meth:`Collection.find_one_and_replace` и :py:meth:`Collection.find_one_and_update`


    .. py:attribute:: AFTER

        Вернуть обновленный/замененый документ


    .. py:attribute:: BEFORE

        Вернуть найденный документ перед обновлением/заменой


Collection
----------

.. py:class:: Collection(**kwargs)

    Коллекция

    * `database` - БД для коллекции

    * `name` - название коллекции

    * `create` - опционно, форсировать создание коллекции

    * `codec_options` - опционально, :py:class:`bson.codec_options.CodecOptions`. Если None, то значение берется из БД

    * `read_preference` - опционально, настройки чтения. Если None, то значение берется из БД

    * `write_concern` - опционально, :py:class:`py,ongo.write_concern.WriteConcern`. Если None, то значение берется из БД

    >>> import pymongo
    >>> client = pymongo.MongoClient()
    >>> db = client.my_db
    >>> users = db.users



    .. py:attribute:: codec_options

        :py:class:`bson.codec_options.CodecOptions`, доступный только для чтения


    .. py:attribute:: database

        :py:class:`pymongo.databaseDatabase`, ссылка на БД коллекции


    .. py:attribute:: full_name

        Возвращает строку, полное имя коллекции: `db_name.collection_name`


    .. py:attribute:: name

        Название коллекции


    .. py:attribute:: read_preference

        Настройки чтения, только для чтения


    .. py:attribute:: write_concern

        :py:class:`pymongo.write_concern.WriteConcern`, доступные только для чтения, настройки записи


    .. py:method:: aggregate(**kwargs)

        Агрегация, возвращает :py:class:`pymongo.command_cursor.CommandCursor`

        * `pipeline` - список этапов агрегации

        * `allowDiskUse=False` - включение записи временных файлов

        * `maxTimeMS` - int, время на выполнение операции

        * `batchSize` - int, количество возвращаемых документо

        * `useCursor` - bool, запросы в БД идут используя курсор

        Данный метод использует настройки read_preference коллекции.

        .. warning::

            При обновлении кластеров до 2.6 `useCursor` должен быть `False`.

        .. note::

            Использование `$out` в `pipeline` требует read preference = PRIMARY

        .. note::

            Данный метод не поддерживает опцию `explain`. Необходимо использовать `command()`.

        >>> from bson.son import SON
        >>> result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
        ...                                 {"x": 2, "tags": ["cat"]},
        ...                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
        ...                                 {"x": 3, "tags": []}])
        >>> pipeline = [
        ...     {"$unwind": "$tags"},
        ...     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
        ...     {"$sort": SON([("count", -1), ("_id", -1)])}
        ... ]
        >>> list(db.things.aggregate(pipeline))
        [{u'count': 3, u'_id': u'cat'}, {u'count': 2, u'_id': u'dog'}, {u'count': 1, u'_id': u'mouse'}]


    .. py:method:: bulk_write(requests, ordered=True)

        Возвращает :py:class:`pymongo.results.BulkWriteResult`, результат сохранения списка операции

        * `requests` - список задании

        * `ordered`

        >>> for doc in db.test.find({}):
        ...     print(doc)
        ...
        {u'x': 1, u'_id': ObjectId('54f62e60fba5226811f634ef')}
        {u'x': 1, u'_id': ObjectId('54f62e60fba5226811f634f0')}
        >>> # DeleteMany, UpdateOne, and UpdateMany are also available.
        ...
        >>> from pymongo import InsertOne, DeleteOne, ReplaceOne
        >>> requests = [InsertOne({'y': 1}), DeleteOne({'x': 1}),
        ...             ReplaceOne({'w': 1}, {'z': 1}, upsert=True)]
        >>> result = db.test.bulk_write(requests)
        >>> result.inserted_count
        1
        >>> result.deleted_count
        1
        >>> result.modified_count
        0
        >>> result.upserted_ids
        {2: ObjectId('54f62ee28891e756a6e1abd5')}
        >>> for doc in db.test.find({}):
        ...     print(doc)
        ...
        {u'x': 1, u'_id': ObjectId('54f62e60fba5226811f634f0')}
        {u'y': 1, u'_id': ObjectId('54f62ee2fba5226811f634f1')}
        {u'z': 1, u'_id': ObjectId('54f62ee28891e756a6e1abd5')}

    .. py:method command

        >>> from bson.son import SON
        >>> result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
        ...                                 {"x": 2, "tags": ["cat"]},
        ...                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
        ...                                 {"x": 3, "tags": []}])
        >>> pipeline = [
        ...     {"$unwind": "$tags"},
        ...     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
        ...     {"$sort": SON([("count", -1), ("_id", -1)])}
        ... ]
        >>> db.command('aggregate', 'things', pipeline=pipeline, explain=True)
        {u'ok': 1.0, u'stages': [...]}


    .. py:method:: delete_one(filter)

        Удаляет один документ из коллкеции, удовлетвоярющий фильтру

        >>> db.test.count({'x': 1})
        3
        >>> result = db.test.delete_one({'x': 1})
        >>> result.deleted_count
        1
        >>> db.test.count({'x': 1})
        2


    .. py:method:: delete_many(filter)

        Удаляет документы из коллекции, удовлетворяющие фильтру

        >>> db.test.count({'x': 1})
        3
        >>> result = db.test.delete_many({'x': 1})
        >>> result.deleted_count
        3
        >>> db.test.count({'x': 1})
        0


    .. py:method:: find(**kwargs)

        Поиск документов в коллекции

        >>> db.test.find({"hello": "world"})

        * `filter` - опционально, фильтр для поиска

        * `projection` - опционно, список полей, которые нужны в результате запроса. `projection={‘_id’: False})`

        * `skip` - the number of documents to omit (from the start of the result set) when returning the results

        * `limit` - опционально, количесвто документов в результате

        * `no_cursor_timeout=False` - опционально, булево, выключить таймаут для курсора. Если True то курсор постоянно будет соединен с БД

        * `cursor_type` - опционально, тип курсора, одно из значение :py:class:`pymongo.cursor.CursorType`

        * `sort` - опционально, список словарей для сортировки

        * `allow_partial_results` - опционально, булево, порционное получение данных

        * `oplog_replay` - опционно,  (optional): If True, set the oplogReplay query flag.

        * `modifiers` - опционно, словарь модификатор фильтра MongoDB

            >>> db.test.find(modifiers={"$maxTimeMS": 500})

        * `batch_size` - опционно, количество документов в порции при порционном поиске


    .. py:method:: find_one(**kwargs)

        Поиск одного документа в коллекции

        Принимает те же аргументы что и :py:meth:`find`

        * `max_time_ms` - опционно, a value for max_time_ms may be specified as part of \**kwargs

        >>> find_one(max_time_ms=100)
        >>> from bson.objectid import ObjectId
        >>> users.find_one({'_id': ObjectId(user['id'])})


    .. py:method:: find_one_and_delete(**kwargs)

        Возвращает найденный документ, удалив его из коллекции

        * `filter` - фильтр для поиска

        * `projection` - опционно, список полей, которые должны быть в рузельтате

        * `sort` - опционно, фильтр для сортировки

        >>> db.test.count({'x': 1})
        2
        >>> db.test.find_one_and_delete({'x': 1})
        {u'x': 1, u'_id': ObjectId('54f4e12bfba5220aa4d6dee8')}
        >>> db.test.count({'x': 1})
        1

        >>> for doc in db.test.find({'x': 1}):
        ...     print(doc)
        ...
        {u'x': 1, u'_id': 0}
        {u'x': 1, u'_id': 1}
        {u'x': 1, u'_id': 2}
        >>> db.test.find_one_and_delete(
        ...     {'x': 1}, sort=[('_id', pymongo.DESCENDING)])
        {u'x': 1, u'_id': 2}

        >>> db.test.find_one_and_delete({'x': 1}, projection={'_id': False})
        {u'x': 1}


    .. py:method:: find_one_and_replace(**kwargs)

        Находит документ и заменяет его. Возвращает найденный или замененный документ

        * `filter` - фильтр для поиска

        * `replacement` - документ для замены

        * `projection` - опционно, список полей которые должны быть в результате

        * `sort` - сортировка

        * `upsert=False` - опционно, булево, создать документ если не найден

        * `return_document` - значение :py:class:`pymongo.collection.ReturmDocument`

        >>> for doc in db.test.find({}):
        ...     print(doc)
        ...
        {u'x': 1, u'_id': 0}
        {u'x': 1, u'_id': 1}
        {u'x': 1, u'_id': 2}
        >>> db.test.find_one_and_replace({'x': 1}, {'y': 1})
        {u'x': 1, u'_id': 0}
        >>> for doc in db.test.find({}):
        ...     print(doc)
        ...
        {u'y': 1, u'_id': 0}
        {u'x': 1, u'_id': 1}
        {u'x': 1, u'_id': 2}


    .. py:method:: find_one_and_update(**kwargs)

        Находит документ и обновляет его. Возвращает найденный или обновленный документ

        * `filter` - фильтр для поиска

        * `update` - операция обновления

        * `projection` - опционно, параметры документа, которые должны быть в результате

        * `sort` - опционно, операция сортировка

        * `upsert` - опционно, булево, создать документ если он не найден

        * `return_document` - значение :py:class:`pymongo.collection.ReturnDocument`. Вернуть найденный документ или обновленный

        >>> db.test.find_one_and_update(
        ...    {'_id': 665}, {'$inc': {'count': 1}, '$set': {'done': True}})
        {u'_id': 665, u'done': False, u'count': 25}}

        >>> db.example.find_one_and_update(
        ...     {'_id': 'userid'},
        ...     {'$inc': {'seq': 1}},
        ...     return_document=ReturnDocument.AFTER)
        {u'_id': u'userid', u'seq': 1}

        >>> db.example.find_one_and_update(
        ...     {'_id': 'userid'},
        ...     {'$inc': {'seq': 1}},
        ...     projection={'seq': True, '_id': False},
        ...     return_document=ReturnDocument.AFTER)
        {u'seq': 2}

        >>> db.example.delete_many({}).deleted_count
        1
        >>> db.example.find_one_and_update(
        ...     {'_id': 'userid'},
        ...     {'$inc': {'seq': 1}},
        ...     projection={'seq': True, '_id': False},
        ...     upsert=True,
        ...     return_document=ReturnDocument.AFTER)
        {u'seq': 1}

        >>> for doc in db.test.find({'done': True}):
        ...     print(doc)
        ...
        {u'_id': 665, u'done': True, u'result': {u'count': 26}}
        {u'_id': 701, u'done': True, u'result': {u'count': 17}}
        >>> db.test.find_one_and_update(
        ...     {'done': True},
        ...     {'$set': {'final': True}},
        ...     sort=[('_id', pymongo.DESCENDING)])
        {u'_id': 701, u'done': True, u'result': {u'count': 17}}


    .. py:method:: count(**kwargs)

        Возвращается количество документов в коллекции

        * `filter` - опционно, фильтр опеределнных документов

        * `hint` - (string or list of tuples): The index to use. Specify either the index name as a string or the index specification as a list of tuples (e.g. [(‘a’, pymongo.ASCENDING), (‘b’, pymongo.ASCENDING)]).

        * `limit` - максимальное количество документов в фильтре

        * `skip` - (int): The number of matching documents to skip before returning results.

        * `maxTimeMS` - (int): The maximum amount of time to allow the count command to run, in milliseconds.


    .. py:method:: create_index(**kwargs)
        
        Создание индекса для коллекции

        * `keys` - ключ или списко ключей, для которых надо создать индексы

        * `name` - имя для индекса

        * `unique` - if True creates a uniqueness constraint on the index.

        * `background` - булево, создать индекс в фоне

        * `sparse` - if True, omit from the index any documents that lack the indexed field.

        * `bucketSize` - for use with geoHaystack indexes. Number of documents to group together within a certain proximity to a given longitude and latitude.

        * `min` - minimum value for keys in a GEO2D index.

        * `max` - maximum value for keys in a GEO2D index.

        * `expireAfterSeconds` - <int> Used to create an expiring (TTL) collection. MongoDB will automatically delete documents from this collection after <int> seconds. The indexed field must be a UTC datetime or the data will not expire.

        >>> my_collection.create_index("mike")
        >>> my_collection.create_index(
        ...    [("mike", pymongo.DESCENDING),
        ...     ("eliot", pymongo.ASCENDING)])

        >>> my_collection.create_index([("mike", pymongo.DESCENDING)],
        ...                            background=True)


    .. py:method:: create_indexes(indexes)

        Создать один или несколько индексов

        * `indexes` - список :py:class::`pymongo.IndexModel`

        >>> from pymongo import IndexModel, ASCENDING, DESCENDING
        >>> index1 = IndexModel([("hello", DESCENDING),
        ...                      ("world", ASCENDING)], name="hello_world")
        >>> index2 = IndexModel([("goodbye", DESCENDING)])
        >>> db.test.create_indexes([index1, index2])
        ["hello_world"]


    .. py:method:: distinct(**kwargs)

        Возвращает уникальные записи

        * `key` - поле, по которому считается уникальность

        * `filter` - опционно, фильтр для получения данных

        * `maxTimeMS` - (int): The maximum amount of time to allow the count command to run, in milliseconds.


    .. py:method:: drop()

        Удаляет коллекцию из БД


    .. py:method:: drop_index(index_or_name)
        
        Удаляет индексы из коллекции

        * `index_or_name` - индекс для удаления


    .. py:method:: drop_indexes()

        Удаление всех индексов


    .. py:method:: group(**kwargs)

        Возвращает список группированных документов

        * `key` - поле или список полей для группировки

        * `condition` - фильтр данных для группировки

        * `initial` - начальные данные для группировки

        * `reduce` - JS строка-функция агрегации

        * `finalize` - функция вызываемая для каждого объекта на выходе

        >>> result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
        ...                                 {"x": 2, "tags": ["cat"]},
        ...                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
        ...                                 {"x": 3, "tags": []}])
        >>> from bson.code import Code
        >>> reducer = Code("""
        ...                function(obj, prev){
        ...                  prev.count++;
        ...                }
        ...                """)
        ...
        >>> results = db.things.group(key={"x":1}, condition={}, initial={"count": 0}, reduce=reducer)
        >>> for doc in results:
        ...   print doc
        {u'count': 1.0, u'x': 1.0}
        {u'count': 2.0, u'x': 2.0}
        {u'count': 1.0, u'x': 3.0}


    .. py:method:: index_information()
        
        Возвращает информацию об индексах коллекции

        >>> db.test.ensure_index("x", unique=True)
        u'x_1'
        >>> db.test.index_information()
        {u'_id_': {u'key': [(u'_id', 1)]},
         u'x_1': {u'unique': True, u'key': [(u'x', 1)]}}


    .. py:method:: initialize_ordered_bulk_op()

        Возвращает :py:class:`pymongo.bulk.BulkOperationBuilder`, для отложенных выполнений операции с коллекцией. Операции будут проводиться по порядку

        >>> from pprint import pprint
        >>>
        >>> bulk = db.test.initialize_ordered_bulk_op()
        >>> # Remove all documents from the previous example.
        ...
        >>> bulk.find({}).remove()
        >>> bulk.insert({'_id': 1})
        >>> bulk.insert({'_id': 2})
        >>> bulk.insert({'_id': 3})
        >>> bulk.find({'_id': 1}).update({'$set': {'foo': 'bar'}})
        >>> bulk.find({'_id': 4}).upsert().update({'$inc': {'j': 1}})
        >>> bulk.find({'j': 1}).replace_one({'j': 2})
        >>> result = bulk.execute()
        >>> pprint(result)
        {'nInserted': 3,
         'nMatched': 2,
         'nModified': 2,
         'nRemoved': 10000,
         'nUpserted': 1,
         'upserted': [{u'_id': 4, u'index': 5}],
         'writeConcernErrors': [],
         'writeErrors': []}
        >>>


    .. py:method:: initialize_unordered_bulk_op()
        
        Возвращает :py:class:`pymongo.bulk.BulkOperationBuilder`, для отложенных выполнений операции с коллекией. Операции будут проводиться не по порядку
        
        >>> bulk = db.test.initialize_unordered_bulk_op()
        >>> bulk.insert({'_id': 1})
        >>> bulk.find({'_id': 2}).remove_one()
        >>> bulk.insert({'_id': 3})
        >>> bulk.find({'_id': 4}).replace_one({'i': 1})
        >>> try:
        ...     bulk.execute()
        ... except BulkWriteError as bwe:
        ...     pprint(bwe.details)
        ...
        {'nInserted': 0,
         'nMatched': 1,
         'nModified': 1,
         'nRemoved': 1,
         'nUpserted': 0,
         'upserted': [],
         'writeConcernErrors': [],
         'writeErrors': [{u'code': 11000,
                          u'errmsg': u'insertDocument :: caused by :: 11000 E11000 duplicate key error index: bulk_example.test.$_id_  dup key: { : 1 }',
                          u'index': 0,
                          u'op': {'_id': 1}},
                         {u'code': 11000,
                          u'errmsg': u'insertDocument :: caused by :: 11000 E11000 duplicate key error index: bulk_example.test.$_id_  dup key: { : 3 }',
                          u'index': 2,
                          u'op': {'_id': 3}}]}


    .. py:method:: inline_map_reduce(**kwargs)

        Выполняет внутренние функции map/reduce

        Perform the map/reduce operation on the server in RAM. A result collection is not created. The result set is returned as a list of documents.

        If full_response is False (default) returns the result documents in a list. Otherwise, returns the full response from the server to the map reduce command.
        
        * `map` - строковое представление JS map функции

        * `reduce` - строковое представление JS reduce функции

        * `out` - имя результирующего объекта

        * `full_response` - опционно, if True, return full response to this command - otherwise just return the result collection

        >>> db.test.inline_map_reduce(map, reduce, limit=2)


    .. py:method:: insert_one(document)

        Возвращает :py:class:`pymongo.results.InsertOneResult`, результат добавления одного документа в коллекцию

        >>> db.test.count({'x': 1})
        0
        >>> result = db.test.insert_one({'x': 1})
        >>> result.inserted_id
        ObjectId('54f112defba522406c9cc208')
        >>> db.test.find_one({'x': 1})
        {u'x': 1, u'_id': ObjectId('54f112defba522406c9cc208')}


    .. py:method:: insert_many(documents, ordered=True)

        Возвращает :py:class:`pymongo.results.InsertManyResult`, результат множественного добавления документов в коллекцию

        * `documents` - список документов

        >>> db.test.count()
        0
        >>> result = db.test.insert_many([{'x': i} for i in range(2)])
        >>> result.inserted_ids
        [ObjectId('54f113fffba522406c9cc20e'), ObjectId('54f113fffba522406c9cc20f')]
        >>> db.test.count()
        2


    .. py:method:: list_indexes()

        Возврашает список индексов коллекции

        >>> for index in db.test.list_indexes():
        ...     print(index)
        ...
        SON([(u'v', 1), (u'key', SON([(u'_id', 1)])),
             (u'name', u'_id_'), (u'ns', u'test.test')])


    .. py:method:: map_reduce(**kwargs)

        Применяет map/reduce функции для коллекции

        * `map` - строковое представление JS map функции

        * `reduce` - строковое представление JS reduce функции

        * `out` - имя результирующего объекта

        >>> result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
        ...                                 {"x": 2, "tags": ["cat"]},
        ...                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
        ...                                 {"x": 3, "tags": []}])
        >>> from bson.code import Code
        >>> mapper = Code("""
        ...               function () {
        ...                 this.tags.forEach(function(z) {
        ...                   emit(z, 1);
        ...                 });
        ...               }
        ...               """)
        >>> reducer = Code("""
        ...                function (key, values) {
        ...                  var total = 0;
        ...                  for (var i = 0; i < values.length; i++) {
        ...                    total += values[i];
        ...                  }
        ...                  return total;
        ...                }
        ...                """)

        >>> result = db.things.map_reduce(mapper, reducer, "myresults")
        >>> for doc in result.find():
        ...   print doc
        ...
        {u'_id': u'cat', u'value': 3.0}
        {u'_id': u'dog', u'value': 2.0}
        {u'_id': u'mouse', u'value': 1.0}
        
        >>> # Получим полную информацию:
        >>> db.things.map_reduce(mapper, reducer, "myresults", full_response=True)
        {u'counts': {u'input': 4, u'reduce': 2, u'emit': 6, u'output': 3}, u'timeMillis': ..., u'ok': ..., u'result': u'...'}

        >>> # Ограничение выборки:
        >>> result = db.things.map_reduce(mapper, reducer, "myresults", query={"x": {"$lt": 2}})
        >>> for doc in result.find():
        ...   print doc
        ...
        {u'_id': u'cat', u'value': 1.0}
        {u'_id': u'dog', u'value': 1.0}

        >>> from bson.son import SON
        >>> db.things.map_reduce(mapper, reducer, out=SON([("replace", "results"), ("db", "outdb")]), full_response=True)
        {u'counts': {u'input': 4, u'reduce': 2, u'emit': 6, u'output': 3}, u'timeMillis': ..., u'ok': ..., u'result': {u'db': ..., u'collection': ...}}


    .. py:method:: options()

        Возвращает свойства коллекции


    .. py:method:: reindex()

        Перестраивает все индексы в коллекции

        .. warning:: 

            Данный метод блокирует все операции


    .. py:method:: parallel_scan(num_cursors)

        Возвращает курсоры для паралельного сканирования коллекции
        
        * `num_cursors` - количесвто возвращаемых курсоров

        >>> def process_cursor(cursor):
        ...     for document in cursor:
        ...     # Some thread-safe processing function:
        ...     process_document(document)
        >>>
        >>> # Get up to 4 cursors.
        ...
        >>> cursors = collection.parallel_scan(4)
        >>> threads = [
        ...     threading.Thread(target=process_cursor, args=(cursor,))
        ...     for cursor in cursors]
        >>>
        >>> for thread in threads:
        ...     thread.start()
        >>>
        >>> for thread in threads:
        ...     thread.join()
        >>>
        >>> # All documents have now been processed.
                

    .. py:method:: rename(**kwargs)

        Переименовывает коллекцию

        * `new_name` -новое название


    .. py:method:: replace_one(filter, replacement, upsert=False)

        Возвращает :py:class:`pymongo.results.UpdateResult`, результат замены найденного документа

        * `filter` - документ, который заменяем

        * `replacement` - новый документ

        * `upsert` - опционно, булево, если искомого документа не существует, то создать новый


        >>> for doc in db.test.find({}):
        ...     print(doc)
        ...
        {u'x': 1, u'_id': ObjectId('54f4c5befba5220aa4d6dee7')}
        >>> result = db.test.replace_one({'x': 1}, {'y': 1})
        >>> result.matched_count
        1
        >>> result.modified_count
        1
        >>> for doc in db.test.find({}):
        ...     print(doc)
        ...
        {u'y': 1, u'_id': ObjectId('54f4c5befba5220aa4d6dee7')}

        >>> result = db.test.replace_one({'x': 1}, {'x': 1}, True)
        >>> result.matched_count
        0
        >>> result.modified_count
        0
        >>> result.upserted_id
        ObjectId('54f11e5c8891e756a6e1abd4')
        >>> db.test.find_one({'x': 1})
        {u'x': 1, u'_id': ObjectId('54f11e5c8891e756a6e1abd4')}


    .. py:method:: update_one(filter, update, upsert=False)

        Возвращает :py:class:`pymongo.results.UpdateResult`, результат обновления найденного документа

        * `filter` - документ, который обновляем

        * `update` - изменение

        * `upsert` - опционно, булево, если искомого документа не существует, то создать новый

        >>> for doc in db.test.find():
        ...     print(doc)
        ...
        {u'x': 1, u'_id': 0}
        {u'x': 1, u'_id': 1}
        {u'x': 1, u'_id': 2}
        >>> result = db.test.update_one({'x': 1}, {'$inc': {'x': 3}})
        >>> result.matched_count
        1
        >>> result.modified_count
        1
        >>> for doc in db.test.find():
        ...     print(doc)
        ...
        {u'x': 4, u'_id': 0}
        {u'x': 1, u'_id': 1}
        {u'x': 1, u'_id': 2}


    .. py:method:: update_many(filter, update, upsert=False)

        Возвращает :py:class:`pymongo.results.UpdateResult`, результат обновления найденных документов

        * `filter` - документ, который обновляем

        * `update` - изменение

        * `upsert` - опционно, булево, если искомого документа не существует, то создать новый

        >>> for doc in db.test.find():
        ...     print(doc)
        ...
        {u'x': 1, u'_id': 0}
        {u'x': 1, u'_id': 1}
        {u'x': 1, u'_id': 2}
        >>> result = db.test.update_many({'x': 1}, {'$inc': {'x': 3}})
        >>> result.matched_count
        3
        >>> result.modified_count
        3
        >>> for doc in db.test.find():
        ...     print(doc)
        ...
        {u'x': 4, u'_id': 0}
        {u'x': 4, u'_id': 1}
        {u'x': 4, u'_id': 2}


    .. py:method:: with_options(codec_options=None, read_preference=None, write_concern=None)

        Возвращает :py:class:`pymongo.collection.Collection`, копию исходной, с измененными параметрами

        * `codec_options` - опционно,  :py:class:`bson.codec_options.CodecOptions`.

        * `read_preference` - опционно,  настройки чтения

        * `write_concern` - опционно,  :py:class:`pymongo.write_concern.WriteConcern`, настройки записи

        >>> from pymongo import ReadPreference
        >>> coll1.read_preference
        Primary()
        >>> coll2 = coll1.with_options(read_preference=ReadPreference.SECONDARY)
        >>> coll1.read_preference
        Primary()
        >>> coll2.read_preference
        Secondary(tag_sets=None)







