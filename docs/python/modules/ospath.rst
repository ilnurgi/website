.. py:module:: os.path

os.path
=======

Модуль встроен в модуль os и позволяет работать с путями к файлам и папкам 


.. py:method:: abspath(path)

    :param str path: путь к файлу или папке

    возвращает полный путь до папки/файла


.. py:method:: basename(path) 

    :param str path: путь к файлу/папке

    Возвращает строку, имя файла или папки.

    >>> os.path.basename('c:\\system\\apps\\Python\\Python.app')
    'Python.app'


.. py:method:: dirname(path) 
    
    :param str path: путь к файлу

    Возвращает строку, путь к родительской папки файла

    >>> os.path.dirname ('c:\\system\\apps\\Python\\Python.app')
    'c:\\system\\apps\\Python'


.. py:method:: exists(path) 

    Возвращает булево, True|False, существует ли указанный путь в системе

    >>> os.path.exists(u'/home/ilnurgi/')
    True


.. py:method:: expanduser(username) 
    
    :param str username: имя пользователя
    
    возвращает путь к пользовательской папке


.. py:method:: getatime(path) 

    :param path: путь к файлу
    :raises WindowsError: если файл не существует
    
    Возвращает время последнего доступа к файлу или папке, в виде количесвта секунд, прошедших с начала эпохи.


.. py:method:: getctime(path)

    :param path: путь к файлу
    :raises WindowsError: если файл не существует

    Возвращает дату создания файла или папки, в виде количества секунд, прошедших с начала эпохи


.. py:method:: getmtime(path) 
    
    :param path: путь к файлу
    :raises WindowsError: если файл не существует

    Возвращает время последнего внесения изменения в файл или папку, в виде количесвта секунд, прошедших с начала эпохи 


.. py:method:: getsize(path) 

    :param path: путь к файлу
    :raises WindowsError: если файл не существует
    
    Возвращает размер файла или папки


.. py:method:: join(path1, path3,...) 
    
    Объединяет пути.
    
    >>> os.path.join('c:\\', 'system\\apps\\Python\\', 'Python.app')
    'c:\\system\\apps\\Python\\Python.app'


.. py:method:: isabs(path)

    :param str path: путь к файлу/папке
    :return: True или False

    проверяет путь на абсолютность


.. py:method:: isdir(path) 
    
    Возвращает булево, True|False, является ли указанный путь катологом

    >>> os.path.isdir(u'/home/ilnurgi/')
    True


.. py:method:: isfile(path) 
    
    :param str path: путь к файлу или каталогу

    проверяет, указывает ли путь к файлу


.. py:method:: islink(path)

    :param str path: путь к файлу или каталогу

    проверяет, указывает ли путь к символической ссылке


.. py:method:: normpath(path)

    :param str path: путь к файлу/папке

    возвращает строку, нормальизованный путь согласно операционной системы

    >>> р = os.path.join(r"C:\\", "book/folder/", "file.txt")
    >>> os.path.normpath(p)
    'C:\\book\\folder\\file.txt'
    

.. py:method:: split(path)

    :param str path: путь к файлу 

    Возвращает кортеж из пары строк - (путь к родителской папке, название файла).
    
    >>> os.path.split('c:\\system\\apps\\Python\\Python.app')
    ('c:\\system\\apps\\Python\\', 'Python.app')


.. py:method:: splitdrive(path) 
    
    :param str path: путь к файлу

    Возвращает кортеж из пары строк - (имя диска, остальная часть пути).
    
    >>> os.path.splitdrive ('c:\\system\\apps\\Python\\Python.app')
    ('c:\\', 'system\\apps\\Python\\Python.app')


.. py:method:: splitext(path) 
    
    :param str path: путь к файлу

    Возвращает кортеж из пары строк - (путь к файлу без расширения, расширение файла)

    >>> os.path.splitext ('c:\\system\\apps\\Python\\Python.app')
    ('c:\\system\\apps\\Python\\Python', '.app')


.. py:method:: walk(path, visit, arg) 
    
    Вызывает функцию .. py:method:: 'visit' передавая ей параметры
    
    >>> def listfiles(arg ,dirname , fnames) :
            print dirname
    >>> os.path.walk('e:\\python\\, listfiles, None)