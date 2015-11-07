.. py:module:: pymongo.errors

errors - исключения пакета pymongo
==================================


AutoReconnect
-------------

.. py:class:: AutoReconnect(message='', errors=None)
    
    Подключение к БД потеряно и будет переподключение

    Наследник :py:class::`pymongo.errors.ConnectionFailure`


BulkWriteError
--------------

.. py:class:: BulkWriteError(results)

    Ошибка порционной записи


BulkWriteError
--------------

.. py:class:: BulkWriteError

    Ошибка валидации коллекции


ConfigurationError
------------------

.. py:class:: ConfigurationError

    Ошибка настройки


ConnectionFailure
-----------------

.. py:class:: ConnectionFailure

    Ошибка подклбчения к БД или потеря подключения к БД


CursorNotFound
--------------

.. py:class:: CursorNotFound(error, code=None, details=None)

    Ошибка с курсором


DocumentTooLarge
----------------

.. py:class:: DocumentTooLarge

    Ошибка, большой документ


DuplicateKeyError
-----------------

.. py:class:: DuplicateKeyError(error, code=None, details=None)

    Ошибка добавления или обновления документа в результате не уникальности идентификатора документа


ExceededMaxWaiters
------------------

.. py:class:: ExceededMaxWaiters

    Ошибка, которая возникает когда поток пытается получить соединение из пула и имеются уже потоки ожидающие соединения
    

ExecutionTimeout
----------------

.. py:method:: ExecutionTimeout(error, code=None, details=None)

    Ошибка возникает при длительном выполнее операции


InvalidName
-----------

.. py:class:: InvalidName

    Ошибка возникает при некорректном имени


InvalidOperation
----------------

.. py:class:: InvalidOperation

    Ошибка возникает при некорректном выполнении операции


InvalidURI
----------

.. py:class:: InvalidURI

    Ошибка возникает при неправильном URI БД


NetworkTimeout
--------------

.. py:class:: NetworkTimeout(message='', errors=None)

    Ошибка возникает при долгом подключении к БД

    Наследние :py:class::`pymongo.errors.AutoReconnect`


NotMasterError
--------------

.. py:class:: NotMasterError(message='', errors=None)

    Ошибка возникает когда сервер на востановлении


OperationFailure
----------------

.. py:class:: OperationFailure(error, code=None, details=None)

    Ошибка выполнения операции


PyMongoError
------------

.. py:class:: PyMongoError

    Базовый класс ошибок


ServerSelectionTimeoutError
---------------------------

.. py:class:: ServerSelectionTimeoutError(message='', errors=None)

    Ошибка возникает когда БД недоступна в течении некоторого времени


WTimeoutError
-------------

.. py:method:: WTimeoutError(error, code=None, details=None)

    Ошибка возникает при выполнении операции, если операция не выполняется определенное время


WriteConcernError
-----------------

.. py:method:: WriteConcernError(error, code=None, details=None)

    Базовый класс для ошибок связанных с правами записи


WriteError
----------
.. py:method:: WriteError(erroe, code=None, details=None)

    Базовый класс для ошибок связанных с записью

