.. py:module:: QtCore

QTimer - объект, таймер
=======================


.. py:class:: QTimer((parent=None))

    Таймер


    .. py:staticmethod:: singleShot(interval, callback)
    .. py:staticmethod:: singleShot(interval, object, slot)

        Предназначен для вызова указанной функции, метода или слота через определенный промежуток времени.

        .. code-block: py

            QtCore.QTimer.singleShot(lOOO, self.on_timeout)
            QtCore.QTimer.singleShot(lOOO, QtGui.qApp, QtCore.SLOТ("quit()"))
            

    .. py:method:: interval()
        
        возвращает установленный интервал

    
    .. py:method:: isActive ()

        Возвращает значение `True`, если таймер генерирует сигналы и `False` в противном случае.


    .. py:method:: isSing1eShot()
        
        Возвращает значение `True`, если таймер будет срабатывать только один раз, и `False` - в противном случае


    .. py:method:: setInterval(interval)

        Задает промежуток времени в миллисекундах, по истечении которого генерируется сигнал :py:meth:`timeout()`. Минимальное значение интервала зависит от операционной системы. Если в параметре `interval` указать значение 0, то таймер бу­дет срабатывать много раз при отсутствии других необработанных сигналов.


    .. py:method:: setSingleShot(flag)

        Если в параметре указано значение `True`, то таймер будет срабатывать только один раз, в противном случае - многократно


    .. py:method:: start([interval])
        
        Запускает таймер. В необязательном параметре можно указать промежуток времени в миллисекундах. Если параметр не указан, то используется значе­ние, возвращаемое методом :py:meth:`interval()`
    

    .. py:method:: stop ()

        Останавливает таймер


    .. py:method:: timerid()

        Возвращает идентификатор таймера или значение -1