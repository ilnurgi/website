.. py:module:: e32db

e32db
=====

Модуль для работы с базами данных e32db.

.. py:method:: format_rawtime(timevalue) 
    
    Возвращает системную дату в юникоде (Formats timevalue (Symbian time) according to the current system’s date/time formatting rules and returns it as a Unicode string.) 

.. py:method:: format_time(timevalue) 
    
    Returns timevalue as a Unicode string formatted so that it is acceptable as a SQL time. To make a time literal, surround the return value with hash (#) characters.

Dbms() 
------

.. py:class:: Dbms() 
    
    класс для записи в БД 

.. py:method:: Dbms.begin() 
    
    Начинает транзакцую 

.. py:method:: Dbms.close() 
    
    Закрывает БД 

.. py:method:: Dbms.commit() 
    
    Записывает текущую Транзакцию 

.. py:method:: Dbms.compact() 
    
    Удаляет пустые области из БД 

.. py:method:: Dbms.create(path) 
    
    создает файл БД по пути path 

.. py:method:: Dbms.execute(query) 
    
    выполняет sql запрос query 

.. py:method:: Dbms.open(path) 
    
    открывает файл БД по пути path 

.. py:method:: Dbms.rollback() 
    
    Откатывает текущую транзакцию

Db_view()
---------

.. py:class:: Db_view() 

    класс для чтения БД 

.. py:method:: Db_view.col(index) 
    
    возвращает значение строки столбца index 

.. py:method:: Db_view.col_count() 
    
    возвращает номер столбца 

.. py:method:: Db_view.col_length(column) 
    
    возвращает количество значений в колонке 

.. py:method:: Db_view.col_raw(column) 
    
    возвращает значение 

.. py:method:: Db_view.col_rawtime(column) 
    
    возвращает значение 

.. py:method:: Db_view.col_type(column) 

    возвращает тип значение 

.. py:method:: Db_view.count_line() 
    
    возвращает количество строк в БД 

.. py:method:: Db_view.first_line() 
    
    переводит курсор на первую строчку 

.. py:method:: Db_view.get_line() 
    
    подгатавливает строку к выдаче 

.. py:method:: Db_view.is_col_null(column) 
    
    Tests whether column is empty. Empty columns can be accessed like normal columns. Empty numerical columns return a 0 or an equivalent value, and text and binary columns have a zero length. 

.. py:method:: Db_view.next_line() 
    
    переходим на следующую Строку 

.. py:method:: Db_view.prepare(db, query) 

    :param db: база данных
    :type db: :py:class:`Dbms()`
    :param query: запрос
    :type query: str
    
    Выполняет запрос к базе данных

Пример
------

.. code-block:: python

    import e32db
    db_path = u'e:\\data\\python\\test.db'
    db = e32db.Dbms()
    db.create(db_path)
    db.open(db_path)
    db.execute(u'CREATE TABLE users (number CHAR(12), login LONG VARCHAR, password LONG VARCHAR)')
    db.execute(u"""INSERT INTO users VALUES('+79xxxxxxxxx','kAIST','password')""")
    # пyть к бaзe и зaпpocы дoлжны быть в юникoдe 
    db_view=e32db.Db_view()
    db_view.prepare(db,u'SELECT * from users')
    # пpoxoдимcя пo вceм cтpoкaм
    for x in xrange(db_view.count_line()):
        # пoдгoтaвлиeм нoвyю cтpoкy к выдaчe
        db_view.get_line()
        # и cмoтpим, чтo y нac в кoлoнкax
        # cтpaннo, нo нyмepaция нaчиниaeтcя c 1 a нe c 0
        print db_view.col(1), db_view.col(2)
        # пepexoдим нa cлeдyющyю cтpoкy
        db_view.next_line()