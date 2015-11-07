.. py:module:: QtCore

QObject - базовый класс для всех объектов модуля
================================================


.. py:class:: QObject()

  базовый класс для всех объектов модуля


    .. py:method:: blockSignals(block)

      :param bool block: 

      Возвращает предыдущее состояние и временно блокирует/разблокирует прием сигналов.


    .. py:method:: connect(qobject, signal, callback[, <ConnectionType>])
    .. py:method:: connect(qobject, signal, qobject2, slot[, <ConnectionType>])
    .. py:method:: connect(qobject, signal, qobject2, signal2[, <ConnectionType>])

      Вешает обработчик на какой то сигнал, и возвращает логический статус работы.

      * qobject - :py:class:`QtCore.QObject`, объект, сигнал которого мы слушаем

      * qobject2 - :py:class:`QtCore.QObject`, объект, сигал которого мы вызываем при обработке сигнала первого объекта

      * signal - :py:class:`QtCore.SIGNAL`, сигнал объекта, который мы слушаем

      * signal2 - :py:class:`QtCore.SIGNAL`, сигнал второго объекта, который мы слушаем

      * slot - :py:class:`QtCore.SLOT`, слот второго бъекта, который мы вызываем

      * callback - обработчик сигнала. В качестве обработчиков можно использовать функции, экземпляры класса, которые должны иметь метод `__call__`

      * ConnectionType - определяет тип соединения между сигналом и обработчиком. Используется при использовании нескольких потоков в приложении, т.к. изменять гуи поток из другого потока нельзя. 

        * QtCore.Qt.AutoConnection - по умолчанию. Если источник сигнала и обработчик находятся в одном потоке, то эквивалентно значению DirectConnection, а если в разных - то QueuedConnection

        * QtCore.Qt.DirectConnection - обработчик вызывается сразу после генерации сигнала

        * QtCore.Qt.QueuedConnection - сигнал помещается в очередь обработки событий

        * QtCore.Qt.BlockingQueuedConnection - аналогично QueuedConnection, но пока сигнал не обработан, поток будет заблокирован. Источник сигнала и обработчик должны быть в разных потоках

        * QtCore.Qt.UniqueConnection - аналогично AutoConnection, но обработчик можно назначить только если он не был назначен ранее.

        * QtCore.Qt.Autocornpatconnection - значение используется в Qt3

      .. code-block:: py

          QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), on clicked)

          widget.connect(button, QtCore.SIGNAL('clicked()'), widget, QtCore.SLOT('func()'))

          widget.connect(button, QtCore.SIGNAL('clicked()'), callback)

          # ======================================
          # другой способ навешивания обработчиков
          # ======================================
          button.clicked.connect(func)

          # обработчик - класс, которому мы передаем какие то доп параметры
          button.clicked.connect(MyClass(10))

          self.button2.clicked["bool"] .connect(self.on_clicked_button2)
          
          # через декоратор
          @button.clicked.connect
          def func(): pass


    .. py:method:: disconnect(qobject, signal, callback)
    .. py:method:: disconnect(qobject, signal, qobject2, slot)

      Удаляет обработчик сигнала, и возвращает логический статус работы.

      * qobject - :py:class:`QtCore.QObject`, объект, сигнал которого мы слушали

      * qobject2 - :py:class:`QtCore.QObject`, объект, сигал которого мы вызывали при обработке сигнала первого объекта

      * signal - :py:class:`QtCore.SIGNAL`, сигнал объекта, который мы слушали

      * signal2 - :py:class:`QtCore.SIGNAL`, сигнал второго объекта, который мы слушали

      * slot - :py:class:`QtCore.SLOT`, слот второго бъекта, который мы вызывали

      * callback - обработчик сигнала. 

      .. code-block:: py

          # ======================================
          # другой способ удаления обработчиков
          # ======================================

          self.buttonl.clicked.disconnect()
          self.button2.clicked["bool"].disconnect(self.on_clicked_button2)


    .. py:method:: emit(signal[, args])

      Генерирует сигнал в системе

      .. code-block:: py

        self.button2.emit(QtCore.SIGNAL("c1icked(boo1)"), False)

        # ======================================
        # другой способ генерации сигналов
        # ======================================
        self.button2.clicked.emit(False)
        self.button2.clicked["bool"].emit(False)


    .. killTimer(idi)

      Останавливает таймер


    .. py:method:: signalBlocked()

      Возвращает логическое предтсаление состояни блокировки приема сигналов


    .. py:method:: startTimer(interval)

      Возваращает идентификатор таймера, с помощью которого можно стартовать таймер.

      * `interval` - задает промежуток времени в миллисекундах, по истечении которого выполняется метод :py:meth:`timerEvent()`. Если равен нуля, то таймер выполняется бесконечное количество раз


  .. py:method:: timerEvent(qtimerevent)

    Обработчик таймера



.. py:class:: QTimerEvent()

  Объект, ивент таймера

  .. py:method:: timerId()

    Возвращает число, идентификатор таймера

