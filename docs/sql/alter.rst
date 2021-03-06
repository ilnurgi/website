ALTER
====================

ALTER TABLE
-----------

изменяет структуру таблицы

.. code-block:: c

	ALTER TABLE 
		[<название БД>.]<таблица> 
		<преобразование>

* `преобразования`
	
	* `RENAME TO <новое имя>` - переименовывает таблицу

		.. code-block:: c

			ALTER TABLE table RENAME TO table1

	* `ADD [COLUMN] <имя нового поля> [<тип данных>] [<опции>]` - добавляет новое поле после всех имеющихся.

		* новое поле должно иметь дефолтное значение или значение `NULL` должно быть допустимым.
		* поле не может быть объявлено как первичный ключ или уникальный

	1. ADD COLUMN <столбец> 

	    добавляет новый столбец в таблицу, описание столбца аналогично как и при CRETAE

	2. ALTER COLUMN <столбец> 

		изменяет солбец

		* ALTER COLUMN <столбец> SET <дефолтноеЗначение> 

			изменяет дефолтное значение

		* ALTER COLUMN <столбец> <тип> 

			изменяет тип значение столбца

	3. DROP COLUMN <столбец>

		удаление столбца из таблицы

	4. ADD
		
		ограничения на таблицу

	5. DROP CONSTRANT <столбец> RESTRICT | CASSCADE