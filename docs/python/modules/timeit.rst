.. py:module:: timeit

timeit
======

Модуль позволяет измерить время выполнения небольших фрагментов кода
с целью оптимизации программы.


.. code-block:: sh

    python -m timeit "x = 2 * 3"
    # 100000000 loops, best of 3: 0.0153 usec per loop

    python -m timeit "x = 2 * 3" --number 10
    # 10 loops, best of 3: 0.0133 usec per loop

Timer
-----

.. py:class:: Timer([stmt='pass'][, setup='pass'][, timer=<timer function>])

    * stmt - строка кода, для которого измеряется время выполнения
    * setup - строка кода, которая должна выполниться перед измерением времени
    * timer


    .. py:method:: repeat(repeat=3, number=1000000)

        Вызывает :py:class:`Timer.timeit` указанное количесвто раз и
        возвращает список результатов

        
    .. py:method:: timeit(number=1000000)

        * number - количесвто повторений

        Возвращает время выполнения кода