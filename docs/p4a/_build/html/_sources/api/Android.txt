Android
=======

Результат работы всех методов :py:class:`Result`

>>> droid = android.Android()


.. py:method:: environment()
    
    текущие переменные окружения

    >>> droid.environment().result
    {
        u'download': u'/mnt/sdcard/Download', 
        u'sdcard': {
            u'availblocks': 509407, 
            u'blocksize': 2048, 
            u'blockcount': 522236
        }, 
        u'TZ': {
            u'display': u'GMT+00:00', 
            u'id': u'GMT', 
            u'offset': 0
        }, 
        u'appcache': u'/data/data/com.dummy.fooforandroid/cache', 
        u'SDK': u'14'
    }


.. py:method:: getClipboard()

    возвращает текст из буфера обмена

    >>> droid.getClipboard().result
    u'Привет МИР'


.. py:method:: getConstants(str classname)

    возвращает константы (static final fields) класса в ввиде словаря

    >>> droid.getConstants('com.dummy.fooforandroid.DialogActivity').result
    {
        u'SIP_SERVICE': u'sip', 
        u'MODE_APPEND': 32768, 
        ...
    }


.. py:method:: getIntent()

    возвращает текущий Intent/действие


.. py:method:: getPackageVersion(str packageName)

    возвращает версию пакета

    >>> droid.getPackageVersion('com.dummy.fooforandroid').result
    1.0

.. py:method:: getPackageVersionCode(str packageName)

    возвращает версию пакета

    >>> droid.getPackageVersionCode('com.dummy.fooforandroid').result
    1


.. py:method:: log(str message)

    записывает сообщение в лог (logcat)

    >>> droid.log(u'Привет МИР')


.. py:method:: makeIntent(**kwargs)

    создает и возвращает Intent/действие

    :param str action:
    :param str uri: не обязательный
    :param str type: не обязательный, MIME type/subtype of the URI
    :param dict extras: не обязательный, дополнительные параметры действия
    :param list categories: не обязательный, список категории, добавляемых в действие
    :param str packagename: не обязательный, название пакета 
    :param str classname: не обязательный, название класса
    :param int flags: не обязательный, флаги действия


.. py:method:: requiredVersion(int requiredVersion)

    проверяет версию sl4a


.. py:method:: sendBroadcast(**kwargs)

    запускает службу

    :param str action,
    :param str uri: не обязательный
    :param str type: не обязательный, MIME type/subtype of the URI,
    :param dict extras: не обязательный, дополнительные параметры действия
    :param str packagename: не обязательный, название пакета
    :param str classname: не обязательный, название класса


.. py:method:: sendBroadcast(Intent intent)

    запускает службу по действию, который вернул :py:meth:`makeIntent`


.. py:method:: sendEmail(**kwargs)

    запускает активити ждя отправки электронной почты

    :param str to: емайлы для отправки, разделенные через запятые
    :param str subject: от кого
    :param str body: текст сообщения
    :param str attachmentUri: не обязательный, вложения


.. py:method:: setClipboard(str text)

    записывает текст в буфер обмена

    >>> droid.setClipboard(u'Привет МИР')


.. py:method:: startActivity(**kwargs)

    запускает активити

    :param str action:,
    :param str uri: не обязательный, 
    :param str type: не обязательный, MIME type/subtype of the URI,
    :param dict extras: не обязательный, дополнительные сведения для активити
    :param bool wait: не обязательный, блокировать, пока пользователь выходит из начатого активити
    :param str packagename: не обязательный, название пакета
    :param str classname: не обязательный, название класса


.. py:method:: startActivityForResult(**kwargs)

    запускает активити, возвращает словарь (Intent) статуса результата работы

    :param str action:,
    :param str uri: не обязательный, 
    :param str type: не обязательный, MIME type/subtype of the URI,
    :param dict extras: не обязательный, дополнительные сведения для активити
    :param str packagename: не обязательный, название пакета
    :param str classname: не обязательный, название класса


.. py:method:: startActivityForResultIntent(Intent intent)

    запускает активити, возвращает словарь (Intent) статуса результата работы


.. py:method:: startActivityIntent(Intent intent [, bool wait])

    запускает активити, через Intent


.. py:method:: vibrate([int duration=300])

    запускает вибрацию на указанное время в миллисекундах

    >>> droid.vibrate()