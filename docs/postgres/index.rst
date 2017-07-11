в постгрес форейгн кей не создает автоматом индекс

.. code-block::

	CREATE [UNIQUE] INDEX [CONCURRENTLY]
		[[IF NOT EXISTS] имя] ON имя_таблицы [USING метод]
		(
			{имя_столбца | (выражение)}
			[COLLATE правило_сортировки][класс_операторов]
			[ASC|DESC][NULLS {FIRST|LAST}]
			[, ...]
		)
		[WITH (параметр_хранения=значение [, ...])]
		[TABLESPACE табл_пространство]
		[WHERE предикат]

	CREATE INDEX test_index ON test_table (col varchar_pattern_ops);
		
	-- класс_операторов
	-- -text_pattern_ops
	-- -varchar_pattern_ops
	-- -bpchar_pattern_ops

.. code-block:: sql

	-- индекс для текстового поля с поиском через лайк
	CREATE INDEX idx_movie_title ON movie (lower(title) text_pattern_ops)

	-- like('abcd%') будет поиск в индексе
	-- like('%abcd%') НЕ будет поиск в индексе

btree индекс

можно

- поиск по полному значению
- поиск по самому левому префиксу
- поиск по префиксу столбца
- поиск по диапазону значений
- поиск по полному совпадению одной части и диапазону в другой части
запросы только по индексу

нельзя

- поиск без использования левой части ключа
- нельзя пропускать столбцы
- оптимизация после поиска в диапазоне

.. code-block::

	CREATE TABLE people (
		last name TEXT NOT NULL
		, first name TEXT NOT NULL
		, date_of_birth TIMESTAMP NOT NULL
		, gender INT NOT NULL
	);

	CREATE INDEX idx_people_name
		ON 
			people USING btree
				(lst_name, first_name, date_of_birth;

hash - индекс 

данный индекс необходимо использовать только для временных таблиц

- нельзя использовать данные в индексе, чтобы избежать чтения строк
- нельзя использовать для сортировки
- нет поиска по частичному ключю
- поддерживают сравнение только на равенство
- операции обслуживания индекса могут быть медленными, если количесвто коллизи в индекса большое
- хеш индекс не записывается в wal-лог, он не транзакционен

.. code-block::

	CREATE TEMPORARY TABLE testhash (
		fname TEXT NOT NULL
		, lname TEXT NOT NULL
	);

	CREATE INDEX idx_testhash_fname
		ON 
			testhash USING hash
				(fname);



gist индекс

.. code-block::

	CREATE TABLE city (
		id SERIAL PRIMARY KEY
		, name TEXT NOT NULL
		, area polygon
	);

	CREATE INDEX idx_city_area
		ON
			city USING gist
				(area);


gin индекс, инвертированный индекс

- для полнотекстового поиска
- для жсон
- для массива


битовый индекс

частичный индекс

.. code-block::

	CREATE INDEX idx_items_avatar_id
		ON
			items (avatar_id)
		WHERE
			avatar_id IS NOT NULL;

функциональный индекс

.. code-block::

	CREATE INDEX idx_movies_title
		ON movies
			(LOWER(title));


кластерный индекс

.. code-block::
	
	CREATE TABLE movies (
		id SERIAL PRIMARY KEY
		, title TEXT NOT NULL
	);

	-- кластеризация для таблицы
	CLUSTER movies USING movies_pkey;
	-- повтроное кластеризация для таблицы
	CLUSTER movies;
	-- повторное кластеризация всей бд
	CLUSTER;


покрывающий индекс

	содержит все данные для запроса



explain

обратить внимание
- операции с cost
- seq sqan
- eows removed by filter
- sort для больших данных дорогая операция

без параметров, explain просто строит план запроса 
.. code-block:: sql

	explain [(param [, ...])] оператор
	explain [analyze] [verbose] оператор

	-- param
	analyze [boolean] - выполнить запрос
	verbose [boolean] - больше инфы
	costs [boolean] - стоимость операции
	buffers [boolean] - буферы, кеши
	timing [boolean] - стоимость операции
	foramt {text | xml | json | yaml} - формат текста




