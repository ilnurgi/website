.. py:module:: numpy.random

random
======

normal()
--------

.. py:function:: normal(mean: int, deviation: int, size: tuple)

    Возвращает массив, со средним значением mean и отклонением deviation 

    .. code-block:: py

        normal(0, 1, (2, 2))
        # array([[0.47, 0.94], [-0.27, -0.15]])


randint()
---------

.. py:function:: randint(start: int, end: int, size: tuple or int)

    Возвращает массив указнного размера со значениями из указанного промежутка

    .. code-block:: py

        randint(0, 10, (2, 2))
        # array([[2, 3], [0, 5]])

        randint(10, size=6)
        randint(10, size=(3, 4))
        randint(10, size=(3, 4, 5))


randn()
-------

.. py:function:: randn(count)

    Возвращает массив случайных чисел в указанном количестве

    .. code-block:: py

        randn(3)
        # array([-1.7, 0.04, -1.7])


random()
--------

.. py:function:: random(size: tuple)

    Возвращает массив указанной размерности, с заполненными различными значениями от 0 до 1

    .. code-block:: py

        random((2, 2))
        # array([[0.99, 0.67], [0.14, 0.23]])

     
seed()
------

.. py:function:: seed()   

    .. code-block:: py

        seed(0)


uniform()
---------

.. py:function:: uniform(start, end, size)

    .. code-block::

        uniform(0.0, 2.0, size=3)
        # array([0.14, 0.56, 1.66])

        uniform(0.0, 2.0, size=4)
        # array([0.145, 0.156, 1.66, 1.99])

        uniform(0.0, 2.0, size=(2, 2))
        # array([0.145, 0.156], [1.66, 1.99])