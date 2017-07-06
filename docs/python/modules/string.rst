.. py:module:: string

string
======

Модуль для работы со строками 


ascii_letters
-------------

.. py:attribute:: ascii_lowercase

    .. code-block:: py

        string.ascii_letters
        # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


ascii_lowercase
---------------

.. py:attribute:: ascii_lowercase

    .. code-block:: py

        string.ascii_lowercase
        # 'abcdefghijklmnopqrstuvwxyz'


ascii_uppercase
---------------

.. py:attribute:: ascii_uppercase

    .. code-block:: py

        string.ascii_uppercase
        # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


digits
------

.. py:attribute:: digits

    Строка, которая содержит числа 0-9

    .. code-block:: py

        string.digits
        # '0123456789'


printable
---------

.. py:attribute:: printable

    Строка, содержит 100 печатаемых символов ASCII

    .. code-block:: py

        string.printable
        # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


punctuation
---------------

.. py:attribute:: punctuation

    .. code-block:: py

        string.punctuation
        # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


atoi()
------

.. py:function:: atoi(s[, base]) 
    
    * base - система исчисления, дефолт десятичная

    Возвращает число, преобразованное из аргумента.
    
    .. code-block:: py 

        string.atoi('1')        
        # 1


atol()
------

.. py:function:: atol(s[, base]) 

    * base - система исчисления, дефолт десятичная

    Возвращает число типа long, преобразованное из аргумента.
    
    .. code-block:: py

        string.atol('1')
        # 1L


atof()
------

.. py:function:: atof(s) 
    
    Возвращает число типа float, преобразованное из аргумента.
    
    .. code-block:: py 

        string.atof('1')
        # 1.0


split()
------

.. py:function:: split(s[, sep=' ' [, maxsplit]]) 

    Возвращает список, полученный разделением строки s, разделителем sep. 
    
    .. code-block:: py

        string.split('ilnur privet kak dela')
        # ['ilnur', 'privet', 'kak', 'dela']


capwords()
----------

.. py:function:: capwords(s: str [, sep: str])

    Вовзаращает строку, с заглавными первыми буквами

    .. code-block:: py
        
        string.capwords('ilnur, ilnur')
        # 'Ilnur, Ilnur'


join()
------

.. py:function:: join(words[, sep=' ']) 
    
    Возвращает строку, объединяет все слова списка в одну строку символов, при этом слова отделяются друг от друга символом, указанным в sep.
    
    .. code-block:: py

        string.join(['ilnur', 'privet', 'kak', 'dela'])
        # 'ilnur privet kak dela'


find()
------

.. py:function:: find(s, sub[, start[, end] } ) 
    
    Возвращает число, позицию вхождения искомой строки sub в строке s.


Template()
----------

.. py:class:: Template(some_string: str)

    Шаблонизатор текста как в UNIX терминалах

    .. code-block:: py

        tmpl = Template('Hello, $who!')


    .. py:method:: substitute(*kwargs)

        Возвращает отфарматированную строку шаблона

        .. code-block:: py

            tmpl.substitute(who='Ilnur')
            # 'Hello, Ilnur!'