.. py:module:: datetime

datetime
========

Модуль для работы с датой и временем


.. py:class:: date(<Год>, <Месяц>, <День>)

	дата


	.. py:attribute:: yaer

		возвращает год


	.. py:attribute:: month

		возвращает месяц


	.. py:attribute:: day

		возвращает день


	.. py:staticmethod:: today()

		возвращает текущую дату :py:class:`date`


	.. py:staticmethod:: fromordinal(<Количество дней с 1 года>)

		возвращает дату :py:class:`date`, соответствующую количеству дней, прошедших с 1 года

		>> datetime.date.max.toordinal()
		3652059
		>>> datetime.date.fromordinal(3652059)
		datetime.date(9999, 12, 31)
		>>> datetime.date.fromordinal(1)
		datetime.date(1, 1, 1)


	.. py:staticmethod:: fromtimestamp(<Количество секунд>)

		возвращает дату :py:class:`date`, соответствующую количеству секунд, прошедших с начала эпохи

		>>> datetime.date.fromtimestamp(time.time()) # Текущая дата
		datetime.date(2014, 8, 24)
		>>> datetime.date.fromtimestamp(1233368623.0) # Дата 31-01-2009
		datetime.date(2009, 1, 31)


	.. py:method:: ctime()

		возвращает строку специального формата

		>>> datetime.date().ctime()
		'Sun Jun 5 00:00:00 2011'


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


.. py:class:: timedelta([days=0][, seconds=0][, microseconds=0][, milliseconds=0][, minutes=0][, hours=0][, weeks=0])

	дата  в виде количесвта дней, секунд и микросекунд

	>>> d1 = datetime.timedelta(days=2)
	>>> d2 = datetime.timedelta(days=7)
	>>> d1 + d2, d2 - d1
	datetime.timedelta(9), datetime.timedelta(5)
	>>> d2 / d1
	3.5
	>>> d1 / 2, d2 / 2.5
	datetime.timedelta(1), datetime.timedelta(2, 69120)
	>>> d2 // d1
	3
	>>> d1 // 2, d2 // 2
	datetime.timedelta(1), datetime.timedelta(3, 43200)
	>>> d2 % d1
	datetime.timedelta(1)
	>>> d1 * 2, d2 * 2
	datetime.timedelta(4), datetime.timedelta(14)
	>>> 2 * d1, 2 * d2
	datetime.timede1ta(4), datetime.timede1ta(14)
	>>> dЗ = -d1
	>>> dЗ, abs(d3)
	(datetime.timede1ta(-2), datetime.timede1ta(2))
	>>> d1 = datetime.timede1ta(days=2)
	>>> d2 = datetime.timede1ta(days=7)
	>>> dЗ = datetime.timede1ta(weeks=1)
	>>> d1 == d2, d2 == dЗ
	(Fa1se, True)
	>>> d1 != d2, d2 != dЗ
	(True, Fa1se)
	>>> d1 < d2, d2 <= dЗ
	(True, True)
	>>> d1 > d2, d2 >= dЗ
	(Fa1se, True)


	.. py:attribute:: days

		количество дней


	.. py:attribute:: microseconds

		количесвто микросекунд


	.. py:attribute:: seconds

		количесвто секунд


	.. py:method:: total_seconds()

		возвращает результат в секундах 

		.. versionadded:: 3.2


.. py:class:: time([hour][ , minute][ , second][ , microsecond][ , tzinfo])

	время

	
	.. py:attribute:: hour

		часы


	.. py:attribute:: minute

		минуты


	.. py:attribute:: second

		секунды


	.. py:microsecond

		микросекунды


	.. py:tzinfo

		информаиця о временной зоне


	.. py:method:: isoformat()

		возвращает время в формате ISO 8601

		>>> datetime.time(23, 12, 38, 375000).isoformat()
		'23:12:38.375000'


	.. py:method:: replace([hour][ , minute][ , second][ , microsecond][ , tzinfo])

		возвращает время с обновленными значениями


	.. py:method:: strftime(<Строка формата>)

		возвращает отформатированную строку



.. py:class:: tzinfo

	зона времени


.. py:attribute:: MAXYEAR

	максимальный год


.. py:attribute:: MINYEAR

	минимальный год