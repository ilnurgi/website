.. py:module:: numpy

numpy
=====

.. toctree::
    :maxdepth: 1

    random


.. code-block:: py

    x = array([1, 2, 3, 4])
    # array([1,  2,  3,  4])

    x*1.5
    # array([1.5,  3.,  4.5,  6.])

    x[1:]
    # array([3.,  4.5,  6.])

    x[1]
    # 3.

    array([1, 2, 3]) + array([1, 2, 3])
    # array([2, 4, 6])

    M = array([[1,2,3],[4,5,6]])
    # M = array([[1, 2, 3], [4, 5, 6]])

    M[1,2]
    # 6



arange
------

.. py:function:: arange(start, end, step)

    Возвращает массив чисел в указанном проежутке с указанным шагом

    .. code-block:: py

        arange(1, 2, 0.1)
        # array([ 1. ,  1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9])


array
-----

.. py:function:: array()

    Возвращает массив

    .. code-block:: py

        array([1, 2, 3])
        # array([1, 2, 3])

