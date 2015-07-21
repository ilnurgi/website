Транзакции
==========


BEGIN
-----

инструкция явного запуска транзакции

::

    BEGIN [DEFFERED | IMMEDIATE | EXCLUSIVE] [TRANSACTION]


COMMIT
------

инструкция применения изменений

::

    COMMIT [TRANSACTION]


END
---

инструкция завершения транзакции

::

    END [TRANSACTION]


ROLLBACK
--------

инструкция отката изменений

::

    ROLLBACK [TRANSACTION] [TO [SAVEPOINT] <Название метки>]


SAVEPOINT
---------

инструкция для создания метки 

::

    SAVEPOINT <название метки>


RELEASE
-------

инструкция нормльного завершения транзакции и сохранения всех изменении

::

    RELEASE [SAVEPOINT] <название метки>