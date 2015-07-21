.. py:module:: traceback

traceback
=========

Модуль используется для сбора и вывода трассировочной информации о программе после появления исключения. Функции в этом модуле оперируют объектами с трассировочной информацией, такими как в третьем элементе возвращаемого значения функции sys.exc_info(). В основном этот модуль может использоваться для реализации нестандартного способа вывода сообщений об ошибках, например когда программы на языке Python выполняются глубоко в недрах сетевого сервера и необходимо организовать вывод трассировочной информации в файл журнала.


.. py:method:: print_tb(traceback [, limit [, file]])
    
    :param traceback: трассировочный объект
    :param limit: количество выводимой информации
    :param file: файл вывода, по дефолту sys.stderr

    Выводит трассировочную информацию. 


.. py:method:: print_exception(type, value, traceback [, limit [, file]])

    :param type: тип исключения
    :param value: значение исключения
    :param traceback: трассировочный объект
    :param limit: количество выводимой информации
    :param file: файл вывода, по дефолту sys.stderr


    Выводит в файл информацию об исключении и трассировочную информацию. 


.. py:method:: print_exc([limit [, file]])

    :param limit: количество выводимой информации
    :param file: файл вывода, по дефолту sys.stderr

    То же, что и :py:meth:`print_exception()`, но применяется к информации, возвращаемой функцией `sys.exc_info()`.


.. py:method:: format_exc([limit [, file]])

    :param limit: количество выводимой информации
    :param file: файл вывода, по дефолту sys.stderr

    Возвращает строку, содержащую ту же информацию, которую выводит функция :py:meth:`print_exc()`.


.. py:method:: print_last([limit [, file]])

    :param limit: количество выводимой информации
    :param file: файл вывода, по дефолту sys.stderr
    
    То же, что и print_exception(sys.last_type, sys.last_value, sys.last_traceback, limit, file).


.. py:method:: print_stack([frame [, limit [, file]]])
    
    :param frame: начальный кадр стека
    :param limit: количество выводимой информации
    :param file: файл вывода, по дефолту sys.stderr

    Выводит трассировочную информацию для точки, откуда был сделан вызов функции. 


.. py:method:: extract_tb(traceback [, limit])

    :param traceback: трассировочный объект
    :param limit: количество выводимой информации

    Извлекает ту же трассировочную информацию, что и функция print_tb(). Возвращает список кортежей вида (filename, line, funcname, text), содержащих информацию, которая обычно выводится в сообщениях об ошибках. 


.. py:method:: extract_stack([frame [, limit]])

    :param frame: кадр стека
    :param limit: количество выводимой информации

    Извлекает ту же трассировочную информацию, что и функция print_stack(), но извлекает ее из кадра стека frame. 


.. py:method:: format_list(list)

    :param list: список кортежей, возвращаемый функцией extract_tb() или extract_stack()

    Форматирует трассировочную информацию перед выводом.


.. py:method:: format_exception_only(type, value)

    :param type: тип исключения
    :param value: значение исключения

    Форматирует информацию об исключении перед выводом.


.. py:method:: format_exception(type, value, traceback [, limit])

    :param type: тип исключения
    :param value: значение исключения
    :param traceback: трассировочный объект
    :param limit: количество выводимой информации

    Форматирует трассировочную информацию и информацию об исключении перед выводом.


.. py:method:: format_tb(traceback [, limit])

    :param traceback: трассировочный объект
    :param limit: количество выводимой информации

    То же, что и format_list(extract_tb(traceback, limit)).


.. py:method:: format_stack([frame [, limit]])

    :param frame: кадр стека
    :param limit: количество выводимой информации

    То же, что и format_list(extract_stack(frame, limit)).


.. py:method:: tb_lineno(traceback)

    :param traceback: трассировочный объект

    Возвращает номер строки, установленной в объекте с трассировочной информацией.