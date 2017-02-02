.. py:module:: matplotlib.ticker

ticker
======


Локаторы
--------

AutoDateLocator
+++++++++++++++

.. py:class:: AutoDateLocator(**kwargs)

    Динамический подбор метки для дат

    * maxticks

    * minticks


DayLocator
++++++++++

.. py:class:: DayLocator()

    Метки привязаны к дням


FixedLocator
++++++++++++

.. py:class:: FixedLocator()

    Локатор для явных меток

    .. code-block:: py

        locator = matplotlib.ticker.FixedLocator([-5, -4, -3, 0, 3, 4, 5])
        axes.xaxis.set_major_locator(locator)


HourLocator
+++++++++++

.. py:class:: HourLocator()

    Метки привязаны к часам


IndexLocator
++++++++++++

.. py:class:: IndexLocator()

    Локатор для меток через определнный интервал от наименьшего значения

    .. code-block:: py

        locator = matplotlib.ticker.IndexLocator(1, 0)
        axes.xaxis.set_major_locator(locator)


LinearLocator
+++++++++++++

.. py:class:: LinearLocator()

    Локатор для фиксированного количества меток

    .. code-block:: py

        locator = matplotlib.ticker.LinearLocator(10)
        axes.xaxis.set_major_locator(locator)


LogLocator
++++++++++

.. py:class:: LogLocator(base, subs)

    Локатор для логарифметических меток

    .. code-block:: py

        locator = matplotlib.ticker.LogLocator(base=2, subs=[1, 5])
        axes.xaxis.set_major_locator(locator)


MaxNLocator
+++++++++++

.. py:class:: MaxNLocator([nbinx, steps])

    Локатор делит ось на указанное количество интервалов интелектуально

    .. code-block:: py

        locator = matplotlib.ticker.MaxNLocator()
        axes.xaxis.set_major_locator(locator)


MinuteLocator
+++++++++++++

.. py:class:: MinuteLocator()

    Метки привязаны к минутам


MonthLocator
++++++++++++

.. py:class:: MonthLocator()

    Метки привязаны к месяцам


MultipleLocator
+++++++++++++++

.. py:class:: MultipleLocator()

    Локатор для меток через определнный интервал от нуля

    .. code-block:: py

        locator = matplotlib.ticker.MultipleLocator(base=2)
        axes.xaxis.set_major_locator(locator)


NullLocator
+++++++++++

.. py:class:: NullLocator()

    Локатор для отключения всех меток

    .. code-block:: py

        locator = matplotlib.ticker.NullLocator()
        axes.xaxis.set_major_locator(locator)


RRuleLocator
++++++++++++

.. py:class:: RRuleLocator()


SecondLocator
+++++++++++++

.. py:class:: SecondLocator()

    Метки привязаны к секундам


WeekdayLocator
++++++++++++++

.. py:class:: WeekdayLocator()

    Метки привязаны к неделям


YearLocator
+++++++++++

.. py:class:: YearLocator(base=1, month=1, day=1, tz=None)

    Метки привязаны к годам

    * baze - расстояние, в годах между рисками


Форматеры
---------

DateFormatter
+++++++++++++

.. py:class:: DateFormatter()

    Даты

    .. code-block:: py

        formatter = matplotlib.ticker.DateFormatter("%Y")
        axes.xaxis.set_major_formatter(formatter)


FixedFormatter
++++++++++++++

.. py:class:: FixedFormatter()

    Фиксированные метки на оси

    .. code-block:: py

        formatter = matplotlib.ticker.FixedFormatter(
            [u"Раз", u"Два", u"Три", u"Четыре", u"Пять"])
        axes.xaxis.set_major_formatter(formatter)


FormatStrFormatter
++++++++++++++++++

.. py:class:: FormatStrFormatter()

    Строковый

    .. code-block:: py

        formatter = matplotlib.ticker.FormatStrFormatter("%.3f")
        axes.xaxis.set_major_formatter(formatter)


FuncFormatter
+++++++++++++

.. py:class:: FuncFormatter()

    Функциональный

    .. code-block:: py

        formatter = matplotlib.ticker.FuncFormatter(lambda x, pos: pass)
        axes.xaxis.set_major_formatter(formatter)


LogFormatter
++++++++++++

.. py:class:: LogFormatter()

    Логарифметический


LogFormatterExponent
++++++++++++++++++++

.. py:class:: LogFormatterExponent()


LogFormatterMathtext
++++++++++++++++++++

.. py:class:: LogFormatterMathtext()


ScalarFormatter
+++++++++++++++

.. py:class:: ScalarFormatter()

    Выод чисел

    .. code-block:: py

        formatter = matplotlib.ticker.ScalarFormatter(lambda x, pos: pass)
        axes.xaxis.set_major_formatter(formatter)


    .. py:attribute:: useOffset

        Аналог :py:meth:`matplotlib.ticker.ScalarFormatter.set_useOffset`


    .. py:method:: set_power_limits((max, min))

        Устаналивает границы для упрозения оси

        .. code-block:: py

            formatter.set_power_limits((-3, 2))


    .. py:method:: set_useOffset()

        Задает константу, которую необходимо прибавить ко всем значения

        .. code-block:: py

            formatter.set_useOffset(1e5)