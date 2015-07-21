.. py:module:: appicon

appicon
=======

.. versionadded:: pys60 1.4.5 

Модуль для чтения иконок установленых приложений

.. py:method:: image(uid, x, y) 
    
    :param uid: uid приложения
    :type uid: str
    :param x: ширина
    :type x: int
    :param y: высота
    :param y: int
    
    Возвращает битмап картинки приложения определенного размера.

    >>> img = appicon.image("fca00010", 100, 100)

.. py:method:: mask(uid, x, y) 

    :param uid: uid приложения
    :type uid: str
    :param x: ширина
    :type x: int
    :param y: высота
    :param y: int

    Возвращает битмап маски приложения определенного размера.
    
    >>> img = appicon.mask("fca00010", 100, 100)

Примеры
-------

.. code-block:: python

    import appicon, e32, TopWindow

    img = appicon.image('a0000bcd', 100, 100)
    mask = appicon.mask('a0000bcd', 100, 100)

    screen = TopWindow.TopWindow()
    screen.add_image(img, (0,0,100,100))
    screen.add_image(mask, (0,105,100,205))
    screen.show()

    app_lock = e32.Ao_lock()
    appuifw.app.exit_key_handler = app_lock.signal
    app_lock.wait()

.. image:: appicon.png

Скачать, исходники