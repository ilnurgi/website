.. py:module:: shutil

shutil
======

Модуль для копирования и перемещения файлов


.. py:method:: copy(path1, path2)

    :param str path1: исходный путь
    :param str path2: путь назначения
    :raises IOError: если файл не удалось скопировать 

    копирует содержимое файла из исходной пути в путь назначения. копируются также права доступа


.. py:method:: copyfile(path1, path2)
    
    :param str path1: исходный путь
    :param str path2: путь назначения
    :raises IOError: если файл не удалось скопировать 

    копирует содержимое файла из исходной пути в путь назначения. никакие метаданные не копируются


.. py:method:: copy2(path1, path2)

    :param str path1: исходный путь
    :param str path2: путь назначения
    :raises IOError: если файл не удалось скопировать 

    копирует содержимое файла из исходной пути в путь назначения, вместе с метаданными 


.. py:method:: move(path1, path2)

    :param str path1: исходный путь
    :param str path2: путь назначения
    :raises IOError: если файл не удалось переместить
    :raises WindowsError: если файл удалить нельзя

    копирует содержимое файла из исходной пути в путь назначения, а затем удаляет исходный файл


.. py:method:: rmtree(path[, errors=False][, errors_callback])

    :param str path: путь к папке
    :param bool errors: игнорировать ошибки
    :param errors_callback: обработчик ошибок, если ошибки не игнорируются