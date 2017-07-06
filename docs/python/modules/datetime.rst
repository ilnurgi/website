.. py:module:: datetime

datetime
========

Модуль для работы с датой и временем


.. py:attribute:: MAXYEAR

    максимальный год


.. py:attribute:: MINYEAR

    минимальный год


date
----

.. py:class:: date(<Год>, <Месяц>, <День>)

    дата


    .. py:attribute:: yaer

        возвращает год

        .. code-block:: py

            date.today().yaer
            # 2017


    .. py:attribute:: month

        возвращает месяц

        .. code-block:: py

            date.today().month
            # 5


    .. py:attribute:: day

        возвращает день

        .. code-block:: py

            date.today().day
            # 3


    .. py:staticmethod:: fromordinal(<Количество дней с 1 года>)

        возвращает дату :py:class:`date`, соответствующую количеству дней,
        прошедших с 1 года

        .. code-block:: py

            datetime.date.max.toordinal()
            # 3652059

            datetime.date.fromordinal(3652059)
            # datetime.date(9999, 12, 31)

            datetime.date.fromordinal(1)
            # datetime.date(1, 1, 1)


    .. py:staticmethod:: fromtimestamp(<Количество секунд>)

        возвращает дату :py:class:`date`, соответствующую количеству секунд,
        прошедших с начала эпохи

        .. code-block:: py

            datetime.date.fromtimestamp(time.time())
            # datetime.date(2014, 8, 24)

            datetime.date.fromtimestamp(1233368623.0)
            # datetime.date(2009, 1, 31)


    .. py:staticmethod:: isoformat(date)

        Возвращает строку, дату в исо формате

        .. code-block:: py

            datetime.date.isoformat(datetime.date.today())
            # '2017-03-05'


    .. py:staticmethod:: today()

        Возвращает :py:class:`datetime.date`, текущую дату

            .. code-block:: py

                date.today()
                # datetime.date(2017, 5, 3)


    .. py:method:: ctime()

        возвращает строку специального формата

        .. code-block:: py

            datetime.date().ctime()
            # 'Sun Jun 5 00:00:00 2011'


    .. py:method:: isocalendar()

        возвращает кортеж из 3х элементов (год, номер недели и порядковый номер дня в неделе)


    .. py:method:: isoformat()

        возвращает дату в формате ГГГГ-ДД-ММ


    .. py:method:: isoweekday()

        возвращает порядковый номер дня недели (начинается с 1)


    .. py:method:: replace([year][, month][ , day])

        возвращает дату с обновленными значемниями


    .. py:method:: strftime(<Строка формата>)

        возвращает отформатированную строку


    .. py:method:: timetuple()

        возвращает :py:class:`time.struct_time` с датой и временем


    .. py:method:: toordinal()

        возвращает количесвто дней, прошедших с 1 года


    .. py:method:: weekday()

        возвращает порядковый номер дня в недели (начинается с 0)


datetime
--------

.. py:class:: datetime(<Год>, <Месяц>, <День>[ , hour][ , minute][ , second][ , microsecond][ , tzinfo])

    дата и время


    .. py:attribute:: year

        год


    .. py:attribute:: month

        месяц


    .. py:attribute:: day

        день


    .. py:attribute:: hour

        часы


    .. py:attribute:: minute 

        минуты 


    .. py:attribute:: second

        секунды 


    .. py:attribute:: microsecond

        микросекунды


    .. py:attribute:: tzinfo

        временная зона


    .. py:classmethod:: combine(<date>, <time>)

        создает экземпляр класса в соответствии со значениями экземпляров класса date и time


    .. py:classmethod:: fromordinal(<Количесвто дней с 1 года>)

        возвращает дату, соответсвующую количесвту дней, прошедших с 1 года


    .. py:classmethod:: fromtimestamp(<Количество секунд>[ , <Зона>])

        возвращает дату, соотвествующую количесвтоу секунд с начала эпохи


    .. py:classmethod:: now([<Зона>])

        возвращает текущую дату и время


    .. py:classmethod:: strptime(<стркоа с датой>, <Строка формата>)

        разбирает строку с датой в соответсвии со строкой формата


    .. py:classmethod:: today()

        возвращает текущую дату и время

        .. code-block:: py

            datetime.to


    .. py:classmethod:: utcfromtimestamp(<Количество секунд>)

        dозвращает дату, соответствующую количесвту секунд, прошедших с начала эпохи в универсальном времени (UTC)


    .. py:classmethod:: utcnow()

        возвращает текущее универсальное время (UTC) 


    .. py:method:: ctime()

        возвращает строку специального формата


    .. py:method:: date()

        возврашает дату в формате :py:class:`date`


    .. py:method:: isocalendar()

        возвращает кортеж из трех элементов (год, номер недели в году и порядковый номер дня в неделе)


    .. py:method:: isoformat([<Разделитель>='T'])

        dозвращает дату в формате ISO 8601


    .. py:method:: isoweekday()

        возвращает порядковый номер дня недели (начинается с 1)


    .. py:method:: replace([year][ , month][ , day][ , hour][, minute][, second][, microsecond][, tzinfo])

        возвращает дату с обновленными значениями


    .. py:method:: strftime(<строка формата>)

        возвращает отформатированную строку

        
    .. py:method:: time()

        возвращает время в формате :py:class:`time`


    .. py:method:: timetuple()

        возвращает дату и время в формате :py:class:`struct_time`


    .. py:method:: timetz()

        возвращает время в формате :py:class:`time` с учетом временной зоны


    .. py:method:: toordinal()

        возвращает количесвто дней с 1 года


    .. py:method:: utctimetuple()

        возвращает дату и время в формате :py:class:`struct_time` в универсальном времене


    .. py:method:: weekday()

        возвращает порядковый номер дня в недели (начинается с 0)


timedelta
---------

.. py:class:: timedelta([days=0][, seconds=0][, microseconds=0][, milliseconds=0][, minutes=0][, hours=0][, weeks=0])

    дата  в виде количесвта дней, секунд и микросекунд

    .. code-block:: py

        d1 = datetime.timedelta(days=2)
        d2 = datetime.timedelta(days=7)

        d1 + d2, d2 - d1
        # datetime.timedelta(9), datetime.timedelta(5)

        d2 / d1
        # 3.5

        d1 / 2, d2 / 2.5
        # datetime.timedelta(1), datetime.timedelta(2, 69120)

        d2 // d1
        # 3

        d1 // 2, d2 // 2
        # datetime.timedelta(1), datetime.timedelta(3, 43200)

        d2 % d1
        # datetime.timedelta(1)

        d1 * 2, d2 * 2
        # datetime.timedelta(4), datetime.timedelta(14)

        2 * d1, 2 * d2
        # datetime.timedelta(4), datetime.timedelta(14)

        d3 = -d1
        d3, abs(d3)
        # (datetime.timedelta(-2), datetime.timedelta(2))

    .. code-block:: py

        d1 = datetime.timedelta(days=2)
        d2 = datetime.timedelta(days=7)
        d3 = datetime.timedelta(weeks=1)

        d1 == d2, d2 == d3
        # (False, True)

        d1 != d2, d2 != d3
        # (True, False)

        d1 < d2, d2 <= d3
        # (True, True)

        d1 > d2, d2 >= d3
        # (False, True)


    .. py:attribute:: days

        количество дней


    .. py:attribute:: microseconds

        количесвто микросекунд


    .. py:attribute:: seconds

        количесвто секунд


    .. py:method:: total_seconds()

        возвращает результат в секундах 

        .. versionadded:: 3.2


time
----

.. py:class:: time([hour][ , minute][ , second][ , microsecond][ , tzinfo])

    время

    
    .. py:attribute:: hour

        часы


    .. py:attribute:: minute

        минуты


    .. py:attribute:: second

        секунды


    .. py:attribute:: microsecond

        микросекунды


    .. py:attribute:: tzinfo

        информаиця о временной зоне


    .. py:method:: isoformat()

        возвращает время в формате ISO 8601

        .. code-block:: py

            datetime.time(23, 12, 38, 375000).isoformat()
            # '23:12:38.375000'


    .. py:method:: replace([hour][ , minute][ , second][ , microsecond][ , tzinfo])

        возвращает время с обновленными значениями


    .. py:method:: strftime(<Строка формата>)

        возвращает отформатированную строку


tzinfo
------

.. py:class:: tzinfo

    зона времени


Форматирование
--------------

======= ========
Литерал Описание
======= ========
j       число без нуля
d       число с нулем
n       месяц без нуля
m       месяц с нулем
E       месяц по локали
F       месяц на английском языке
b       месяц на английском языке, 3х буквенное обозначение: jan, feb, ...
M       месяц на английском языке, 3х буквенное обозначение: Jan, Feb, ...
y       год 2х значный
Y       год 4х значный
z       номер дня в году
w       номер дня недели от 0 до 6
l       день недели на английском
D       день недели на английском, 3х буквенное: Mon, Tue
g       часы в 12х часовом формате без начального 0
G       часы в 24х часовом формате без начального 0
h       часы в 12х часовом формате c начальным 0
H       часы в 24х часовом формате c начальным 0
a       период времени: a.m., p.m.
A       период времени: AM, PM
i       минуты
s       секунды с начальным нулем
u       микросекунды
I       1 - летнее время, 0 - зимнее
L       True - год високосный, False - не високосный
t       количесвто дней в текущем месяце
T       временная зона
r       Дата по RFC 2822
======= ========
