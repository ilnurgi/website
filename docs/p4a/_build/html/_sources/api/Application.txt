Application
===========

Результат работы всех методов :py:class:`Result`

.. py:method:: forceStopPackage(str packageName)

    останавливает указанное приложение


.. py:method:: getLaunchableApplications()

    возвращает данные о приложениях, которые можно запустить, в виде словаря

    >>> droid.getLaunchableApplications().result
    {
        u'SL4A': u'com.googlecode.android_scripting.activity.ScriptManager', 
        u'Clock': u'com.android.deskclock.DeskClock',
        ...
    }


.. py:method:: getRunningPackages()

    возвращает список строк, запущенных пакетов

    >>> droid.getRunningPackages().result
    [u'com.android.calendar', u'com.android.browser', ...]


.. py:method:: launch(str className)

    запускает приложение