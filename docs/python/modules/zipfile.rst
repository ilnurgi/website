.. py:module:: zipfile

zipfile
=======


.. py:class:: ZipFile(file, mode)
    
    объект архив


    .. py:method:: write(src, localpath)

        добавляет в архив файл

        :param str src: путь к файлу
        :param str localpath: путь файла в архиве


    .. py:method:: read(path)

        читает файл из архива, возвращает данные в бинарном формате

        :param str path: путь к файлу


    .. py:method:: namelist()

        возвращает список строк, путей к файлам архива