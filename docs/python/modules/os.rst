.. py:module:: os

os
==

Модуль позволяет работать с файлами и папками. Русские названия файлов и папок возвращаются и принимаются всеми функциями этого модуля в кодировке UTF-8, поэтому необходимо использовать функции для перекодирования строк - методы decode и encode. 


Атрибуты модуля
---------------

.. py:attribute:: name

    название версии модуля, зависит от операционной системы

    * `nt` - windows xp


Методы модуля
-------------


.. py:method:: access(<путь>, <режим>)

    проверка прав доступа к файлу или папке. 

    В параметре режим могут быть указаны следующие константы:

    * os.F_OK - проверка наличия пути
    * os.R_OK - проверка на возможность чтения
    * os.W_OK - проверка на возможность записи
    * os.X_OK - проверка на возможность выполнения


.. py:method:: chdir(path) 

    :param str path: путь к каталогу

    Изменяет текущий рабочий каталог приложения на указанный 


.. py:method:: chmod(<путь>, <права доступа>) 
    
    Изменяет права доступа файла.

    >>> os.chmod('file.txt', 0o777)
    

.. py:method:: getcwd() 
    
    Возвращает рабочий путь приложения 


.. py:method:: listdir(path) 

    :param str path: путь к папке

    Возвращает список имен файлов и папок в указанной папке


.. py:method:: mkdir(path[, access=0o777])

    :param str path: путь к каталогу
    :param access: права доступа 
    
    Создает папку по указанному пути


.. py:method:: makedirs(path) 

    Аналогичен функции .. py:method::'mkdir', но автоматический создает промежуточные папки 


.. py:method:: remove(path) 
    
    :param str path: путь к файлу
    :raises WindowsError: если файл удалить нельзя

    Удаляет файл


.. py:method:: rmdir(path) 
    
    :param str path: путь к каталогу

    Удаляет папку по указанному пути


.. py:method:: removedirs(path) 
    
    Аналогичен функции rmdir, но автоматический удаляет все родительские пустые папки 


.. py:method:: rename(path1, path2)

    :param str path1: исходный путь
    :param str path2: путь назначения
    :raises WindowsError: если файл не удалось найти или новый файл уже существует  
    
    Переименовывает файл


.. py:method:: stat(path) 
    
    :param str path: путь к файлу

    Возвращает состояние о файле, объект stat_result, который в зависимости от типа операционной системы содержит разные атрибуты.


.. py:method:: tempname([path, [prefix]]) 
    
    Возвращает уникальный путь для создания временных файлов.


.. py:method:: unlink(path)

    :param path: путь к файлу
    :raises WindowsError: если файл удалить не удалось

    удаляет файл


.. py:method:: utime(path[, (atime=now, mtime=now)])

    :param str path: путь к файлу
    :param int atime: время последнего доступа в секндах
    :path int mtime: время изменения в секундах
    :raises WindowsError: если файл не найден

    обновляет время последнего достпуа и время изменения


.. py:method:: walk(path[, topdown=True][, onerror=None][, followlinks=False]) 
    
    :param str path: путь к начальному каталогу
    :param bool topdown: задает последовательность обхода каталогов

    Возвращает итератор, на каждой итерации возвращает кортеж (текущий каталог, список каталогов и список файлов) 



Методы для работы с файлами, файловыми дексрипторами
----------------------------------------------------

.. py:method:: close(<дескриптор>)

    закрывает файл


.. py:method:: dup(<дескриптор>)

    возвращает дубликат дескриптора


.. py:method:: fdopen(<дескриптор>[, <режим>[, <размер буфера>]])

    возвращает файловый объект по указанному дескриптору

    
.. py:method:: lseek(<дескриптор>, <смещение>, <позиция>)

    устанавливает указатель в позицию, имеюущий указанное смещение относительной указанной позиции

    в параметре позици могут быть указаны следующие значения:

    * os.SEEK_SET или 0 - начало файла
    * os.SEEK_CUR или 1 - текущая позиция укзаталея
    * os.SEEK_END или 2 - конец файла


.. py:method:: open(<путь к файлу>, <режим>[, mode=0o777])

    Открывает файл и возвращает целочисленный дескриптор

    В параметре <режим> в операционной системе windows могут быть указаны следующие флаги (или их комбинации через символ |):

    * os.O_RDONLY - чтение 
    * os.O_WRONLY - запись
    * os.O_RDWR - чтение и запись
    * os.O_APPEND - добавление в конец файла
    * os.O_CREATE - создать файл, если он не существует
    * os.O_TRUNC - очистить содержимое файла
    * os.O_BINARY - файл будет открыт в бинарном режиме
    * os.O_TEXT - файл будет открыт в текстовом режиме


.. py:method:: read(<дескриптор>, <количество байтов>)

    читает из файла указанное количество байтов


.. py:method:: write(<дескриптор>, <последовательность байтов>)

    записывает последовательность байтов в файл