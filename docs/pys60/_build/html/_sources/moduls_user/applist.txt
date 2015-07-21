.. py:module:: applist

applist
=======

Модуль для работы с приложениями 

.. py:method:: applaunch(uid)

    :param uid: uid запускаемого приложения
    :type uid: int

    .. versionadded:: 2.0 

    Запускает приложение

    >>> applist.applaunch(0x10008d39)
    
.. py:method:: applist() 
    
    Возвращает список кортежей установленных приложений.

    >>> applist.applist()
    [..., (536871485, u'Zip manager', u'Z:\\sys\\bin\\ZipManager.exe'), ...]

.. py:method:: fetchicon(uid, size, 1|2)

    .. versionadded:: 2.0

    :param uid: uid запускаемого приложения
    :type uid: int
    :param size: размер
    :type size: tuple
    :param 1|2: иконка или маска

    Возвращает bitmap иконку приложения

    >>> bitmap_icon = applist.fetchicon(0x10008d39, size, 1)
    >>> img = graphics.Image.from_cfbsbitmap(bitmap_icon)

.. py:method:: launchinbox([arg])

    :param args: 0x1002 - входящие, 0x1003 - исходящие, 0x1004 - черновики, 0x1005 - переданные
    :type args: int

    .. versionadded:: 2.0

    Открывает приложение "Сообщения"

.. py:method:: launchinbox()

.. py:method:: launchsms(recipient, alias)

    .. versionadded:: 2.0

    :param recipient: номер адрессата
    :type recipient: str
    :param alias: имя адрессата
    :type alias: unicode

    Запускает стандартное окно ввода сообщения.

    >>> applist.launchsms(u'89271234', u'Name')