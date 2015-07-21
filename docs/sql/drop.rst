DROP
====

DROP INDEX
----------

.. code-block:: c
	
	DROP INDEX indexTableName

DROP TABLE
----------

уничтожает таблицу

:: 
	
	DROP TABLE [IF EXISTS] [<БЮ>.]<название таблицы> [RESTRICT | CASSCADE]
    
* `CASSCADE` - удаляет зависимые записи

* `RESTRICT` - не удаляет

