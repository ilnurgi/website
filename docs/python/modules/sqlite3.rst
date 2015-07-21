.. py:module:: sqlite3

sqlite3
=======

Модуль, позволяющий работать с базой данных SQLite3

Согласно спецификации DB-API 2.0 последовательность работы с базой данных выглядит следующим образом:

1. Производится подключение к базе данных с помощью функции :py:meth:`connect`. Функция воз­вращает объект соединения, с помощью которого осуществляется дальнейшая работа с базой данных.

2. Создается объект-курсор.

3. Выnолняются SQL-зanpocы и обрабатываются результаты. Перед выnолнением nервого заnроса. который изменяет заnиси (INSERT, REPIACE, UPDATE и DELETE), автоматически за­пускается транзакция.

4. Завершается транзакция или отменяются все изменения в рамках транзакции.

5. Закрывается объект-курсор.

6. Закрывается соединение с базой данных.


Атрибуты модуля
---------------


.. py:attribute:: apilevel

    возвращает строку, номер спецификации DB-API

    >>> sqlite3.apilevel
    '2.0'


.. py:attribute:: sqlite_version

    возвращает строку, номер версии моудля

    >>> sqlite3.sqlite_version
    '3.7.4'


.. py:attribute:: sqlite_version_info

    возвращает кортеж, номер версии модуля

    >>> sqlite3.sqlite_version_info
    (3, 7, 4)


Методы модуля
-------------

.. py:method:: complete_statement(sql)

    проверка завершенности запроса

    >>> sqlite3.complete_statement('SELECT 10 >5;')
    True

    
.. py:method:: connect(database[, timeout=5] [, lsolatlon_level] [, detect_types] [, factory] [, check_same_thread] [, cached_statements])

    возвращает объект :py:class:`Connection` для работы с БД

    :param str database: путь к БД, если БД не существует она автоматический создастся. Также можно указать значение `:memory:`, которая означает что БД создается в памяти.
    :param int timeout: время ожидания снятия блокировки с открываемой БД, в секундах


.. py:method:: register_adapter(<тип данных или класс>, <ссылка на функцию>)

    регистрирует пользовательскую функцию, которая будети вызываться при попытке вставки объекта в запросе.

    >>> class Car(object):

            def __init__(self, model, color):
                self.model, self.color = model, color
    >>> def my_adapter(car):
            return '{0}|{1}'.format(car.model, car.color)
    >>> sqlite3.register_adapter(Car, my_adapter)
    >>> car = Car('car1', 'red')
    >>> cur.execute('INSERT INTO cars VALUES (?)', (car, ))

    Вместо регистрации функции преобразования типа можно внутри класса определить метод __conform__(self, <Протокол>), где протокол соответсввует PrepareProtokol.

    >>> class Car(object):

            def __init__(self, model, color):
                self.model, self.color = model, color   

            def __conform__(self, protokol):
                if protokol is sqlite3.PrepareProtokol:
                    return '{0}|{1}'.format(car.model, car.color)


.. py:method:: register_converter(<тип данных>, <ссылка на функцию>)

    регистрирует пользовательскую функцию преобразования типа данных 

    Чтобы интерпретатор смог определить, какую функцию необходимо вызвать для преобразования типа данных, следует явно указать местоположение метки с помощью параметра `detect_types` функции :py:meth:`connect`. Параметр может принимать следующие значения (или их комбинацию через |):

        * sqlite3.PARSE_COLNAMES - тип данных указывается в запросе в псевдониме поля внутри квадратных скобок 

            >>> 'SELECT model as "c [mycar]" FROM mycars'

        * sqlite3.PARSE_DECLTYPES - тип данных определяется по значению, указанному после названия поля в инструкции CREATE TABLE.

            >>> 'CREATE TABLE cars (model mycar)'

    >>> class Car(object):
            def __init__(self, model, color):
                self.model, self.color = model, color
            def __repr__(self):
                return '{0} {1}'.format(self.model, self.color)
    >>> def myconverter(value):
            value = str(value, 'utf-8')
            model, color = value.split('|')
            return Car(model, color)
    >>> sqlite3.register_converter('mycar', myconverter)
    >>> cur.execute('SELECT model as "c [mycar]" FROM cars')


Классы модуля
-------------

.. py:class:: Connection()

    объект для работы с БД


    .. py:method:: close()

        закрывает соединение с БД


    .. py:method:: commit()

        завершает текущую транзакцию


    .. py:method:: create_aggregation(<название функции>, <количесвто параметров>, <ссылка на класс>)

        связывает название функции в SQL-запросе с пользовательской функцией. 

        Класс должен иметь два метода:

            * `step()` - сюда передаются параметры

            * `finalize()` - возвращает результат


        >>> class MyClass:
                def __init__(self) :
                    self.result = []
                def step(self, value):
                    self.result.append(value)
                def finalize(self):
                    self.result.sort()
                    return " - ".join(self.result)
        >>> con.create_aggregate("myfunc", 1, MyClass)
        >>> cur.execute ( "SELECT myfunc(nаme) FROM table")


    .. py:method:: create_collation(<название функции сортировки>, <ссылка на функцию сортировки>)

        связывает название функции в SQL-запросе с пользовательской функцией. Функция сортировки принимает две строки и должна возвращать: 1 - если первая больше второй, -1 - если вторая больше первой, 0 - если они равны.

        >>> def myfunc (s1, s2):
                s1 = s1.1ower()
                s2 = s2 .1ower ()
                if s1 == s2:
                    return О    
                elif s1 > s2:
                    return 1
                else:
                    return -1
        >>> con.create_collatlon("myfunc", myfunc)
        >>> cur = con.cursor()
        >>> cur.execute("SELECT * FROM words ORDER ВУ word COLLATE myfunc")


    .. py:method:: create_function(<название функции>, <количество параметров>, <ссылка на функцию>)

        связывает название функции в SQL-запросе с пользовательской функцией. Функция сортировки принимает две строки и должна возвращать: 1 - если первая больше второй, -1 - если вторая больше первой, 0 - если они равны.

        >>> def myfunc(s):
                return s .1ower ()
        >>> con.create_function("mylower", 1, myfunc)
        >>> cur = con.cursor()
        >>> cur.execute("SELECT * FROM words WHERE mylower(name) like 'ilnurgi'")


    .. py:method:: cursor()

        возвращает объект :py:class:`Cursor` для выполнения запросов


    .. py:method:: rollback()

        откатывает изменения в текущей транзакции


.. py:class:: Cursor()

    объект для выполнения запросов


    .. py:method:: close()

        закрывает объект курсор


    .. py:method:: execute(sql [, <значения>])

        выполянет один запрос

        :param str sql: строка запроса
        :rasises: sqlite3.DataBaseError

        >>> cur.execute('insert into table (name) values (?)', ('ilnurgi', ))
        >>> cur.execute('insert into table values (?, ?)', (2, 'ilnurgi'))
        >>> cur.execute('insert into table values (:id, :name)', {'id': 2, 'name': ilnurgi'})


    .. py:method:: executemany(sql, args)

        выполняет запрос несколько раз

        >>> cur.execute('insert into table values (?, ?)', [(1, 'ilnurgi'), (2, 'ilnurgi')])


    .. py:method:: exequtescript(sql)

        выполняет несколько запросов за один раз

        :param str sql: строка с несколькими запросами
        :rasises: sqlite3.DataBaseError


    .. py:method:: fetchall()

        возвращает список кортежей всех записей запроса


    .. py:method:: fetchmany([size=cursor.arraysize])

        возвращает список кортежей записей запроса

        >>> cur.fetchmany(3)
        [(1, 'name1'), (2, 'name2'), (3, 'name3')]


    .. py:method:: fetchone()

        возвращает одну запись из результата запроса в виде кортежа. Если записей больше нет, вернет None.


    .. py:method:: __next__()

        возвращает одну запись из результата запроса в виде кортежа. Если записей больше нет, возбуждает исключение StopIteration.



    .. py:attribute:: description

        возвращает кортеж кортежей с именами полей в результате выполнения инструкции SELECT. 


    .. py:attribute:: lastrowid

        возвращает индекс последней добавленной записи с помощью инструкции INSERT и метода `exequte()`. Если индекс не определен то вернет None.


    .. py:attribute:: rowcount

        возвращает количество измененных или удаленных записей. Если количество не определено, возвращает -1.


Иерархия ошибок модуля
----------------------

* Exception - 

    * Warning - важные предупреждения

    * Error - базовый класс для всех ошибок

        * InterfaceError - ошибки с интерфейсом

        * DatabaseError - базовый класс для ошибок БД

            * DataError - ошибка при обработке данных

            * OperationError - ошибка связана с опрецией в БД

            * IntegrityError - ошибка с внешними ключами или индексом

            * InternalError - внутренняя ошибка БД

            * ProgrammingError - ошибка программирования

            * NotSupportedError - ошибка при использовании методов, не поддерживаемых БД