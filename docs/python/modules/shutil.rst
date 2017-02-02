.. py:module:: shutil

shutil
======

Модуль для копирования и перемещения файлов


.. py:method:: copy(src, dst)

    * src - исходный путь
    * dst - путь назначения

    Копирует содержимое файла из исходной пути в путь назначения.

    Копируются также права доступа

    Возбуждает исключение :py:class:`IOError`, если файл не удалось скопировать

    .. code-block:: py

        shutil.copy("path1/1.txt", "path2/1.txt")


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


.. py:method:: move(src, dst)

    * src - исходный путь
    * dst - путь назначения

    Копирует содержимое файла из исходной пути в путь назначения,
    а затем удаляет исходный файл

    Возбуждает исключения:

        * :py:class:`IOError` - если файл не удалось переместить
        * :py:class:`WindowsError` - если файл удалить нельзя

    .. code-block:: py

        shutil.move("path1/1.txt", "path2/1.txt")


.. py:method:: rmtree(path[, errors=False][, errors_callback])

    :param str path: путь к папке
    :param bool errors: игнорировать ошибки
    :param errors_callback: обработчик ошибок, если ошибки не игнорируются