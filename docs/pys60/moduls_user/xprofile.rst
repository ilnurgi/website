.. py:module:: xprofile

xprofile
========

Питоновский модуль для работы с режимами смартфона.

.. warning:: Только для pys60 1.4.x

.. py:attribute:: version 
    
    Версию модуля
    
    xprofile.version
    (1,0,0)
    
.. py:method:: ap_is_default(ap)
    
    Устанавливает режим стандартным
    
    >>> xprofiles.ap_is_default(1)

.. py:method:: ap_is_silent()
    
    >>> xprofiles.ap_is_silent()

.. py:method:: get_ap() 
    
    Возвращает активный режим
    
    >>> xprofile.get_ap()
    (1, u'\u0411\u0435\u0437 \u0437\u0432\u0443\u043a\u0430', u'\u0411\u0435\u0437 \u0437\u0432\u0443\u043a\u0430')

.. py:method:: profiles_dict() 
    
    Возвращает словарь режимов
    
    >>> xprofile.profiles_dict()
    
    { ..., 32: (u'\u041d\u043e\u0432\u044b\u0439 \u0440\u0435\u0436\u0438\u043c(02)', u'\u041d\u043e\u0432\u044b\u0439 \u0440\u0435\u0436\u0438\u043c(02)'), ...}

.. py:method:: profiles_list() 
    
    Возвращает список режимов
    
    >>> xprofile.profiles_list()
    [ ..., (2, u'\u0412\u0441\u0442\u0440\u0435\u0447\u0430', u'\u0412\u0441\u0442\u0440\u0435\u0447\u0430'), ...]

.. py:method:: set_ap(ap) 
    
    Устанавливает активный режим

    >>> xprofile.set_ap(0)

.. py:method:: set_profile_name(old, new) 
    
    Переименовывает название режима

    >>> xprofile.set_profile_name(u'')