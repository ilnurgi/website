.. py:module:: QtCore

QThread - поток
===============

.. py:class:: QThread([parent=None])

    Поток

    Наследник :py:class:`QtCore.QObject`. 

    Для использования потоков, необходимо отнаследоваться от данного класса и определить в нем метод `run`, который выполнится в отдельном потоке.


    .. py:staticmethod:: msleep(millisec)
    .. py:staticmethod:: sleep(sec)
    .. py:staticmethod:: usleep(microsec)

        временно прерывает выполнение потока

        ::

            self.msleep(3000)
            self.sleep(3)
            self.usleep(3000000)


    .. py:method:: emit(signal, data)

        генерирует сигнал и передает данные

        ::

            self.emit(QtCore.SIGNAL('mysignal(QString)'), 'i={0}'.format(i))

    .. py:method:: isFinished()

        возвращает истину или ложь, поток завершен

    .. py:method:: isRunning()

        возвращает истину или ложь, поток запущен

    .. py:method:: priority()

        возвращает текущий приоритет потока

    .. py:method:: setPriority(<приоритет>)

        задает приоритет потока

    .. py:method:: start([priority=QThread.InheritPriority])

        запускает поток, с определенным приоритетом, по отношению к другим потокам потокам.
        Приоритеты в порядке увеличения:

        0. IdlePriority - самый низкий приоритет         
        1. LowestPriority
        2. LowPriority
        3. NormalPriority
        4. HightPriority
        5. HighestPriority
        6. TimeCriticalPriority - самый высокий приоритет
        7. InheritPriority - автоматический выбор приоритета

    .. py:method:: terminate()

        прерывает выполенение потока, не рекомендуется использовать


    .. py:method:: finished()

        сигнал, генерируется после завершения потока

    .. py:method:: started()

        сигнал, генерируется при запуске потока






