.. py:module:: lock

lock
====

Модуль для работы с блокировкой 

.. versionadded:: pys60 2.0.0

.. py:method:: LockStatus() 
    
    Возвращает статус блокировки
    
    >>> lock.LockStatus()
    0

.. py:method:: ask() 
    
    Выводит окно запроса блокировки

    >>> lock.ask()

.. py:method:: lock() 

    Включает блокировку клавиатуры
    
    >>> lock.lock()

.. py:method:: lock_with_pass() 
    
    Включает блокировку смартфона с паролем
    
    >>> lock.lock_with_pass()

.. py:method:: unlock() 
    
    Выключает блокировку смартфона
    
    >>> lock.unlock()