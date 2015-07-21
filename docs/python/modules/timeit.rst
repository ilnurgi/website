.. py:module:: timeit

timeit
======

модуль позволяет измерить время выполнения небольших фрагментов кода с целью оптимизации программы.


.. py:class:: Timer([stmt='pass'][, setup='pass'][, timer=<timer function>])

	:param stmt: строка кода, для которого измеряется время выполнения
	:param setup: строка кода, которая должна выполниться перед измерением времени
	:param timer:


	.. py:method:: repeat(repeat=3, number=1000000)

		вызывает :py:class:`timeit` указанное количесвто раз и возвращает список результатов

		
	.. py:method:: timeit(number=1000000)

		:param int number: количесвто повторений

		возвращает время выполнения кода