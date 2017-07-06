.. py:module:: numpy

numpy
=====

http://docs.scipy.org

.. toctree::
    :maxdepth: 1

    arithmetic
    dtype
    examples
    random


.. code-block:: sh

    pip install numpy


.. code-block:: py

    import numpy
    print(numpy.__version__)
    # '1.11.1'


.. code-block:: py

    a = array([1, 2, 3])
    # array([1,  2,  3])
    b = array([4, 5, 6])
    # array([4, 5, 6])

    a*1.5
    # array([1.5,  3.,  4.5])

    a[1:]
    # array([2,  3])

    a[0]
    # 1

    a + b
    # array([5, 7, 9])

    c = array([
        [1,2,3], 
        [4,5,6]
    ])

    c[1,2]
    # 6

    array([2]) * array([[1, 2], [3, 4]])
    # array([[2, 4], [6, 8]])

.. code-block:: py

    x = array(
        [
            [2, 4, 6, 8],
            [3, 3, 2, 1],
            [2, 6, 3, 4],
            [5, 2, 3, 5]
        ]
    )

    x.shape
    # (4, 4)

    x[0:1, :]
    # array([[2, 4, 6, 8]])

    x[:, 0:1]
    # array([[2], [3], [2], [5]])

    x[0:2, 0:2]
    # array([[2,4], [3, 3]])


ndarray
-------

.. py:class:: ndarray

    Экземпляры данного класса возвращают методы модуля

    .. code-block:: py

        a = array([10])


    .. py:attribute:: dtype

        Тип значений массива

        .. code-block:: py

            array([10]).dtype
            # int64


    .. py:attribute:: itemsize

        Возвращает число, размер одного элемента массива

        .. code-block:: py

            numpy.random.randint(10, size=(3, 4, 5)).itemsize
            # 8


    .. py:attribute:: nbytes

        Возвращает число, размер всех значений массива

        .. code-block:: py

            numpy.random.randint(10, size=(3, 4, 5)).nbytes
            # 480


    .. py:attribute:: ndim

        .. code-block:: py

            array([
                [4, 8], 
                [10, 20]
            ]).ndim
            # 2


    .. py:attribute:: shape

        Размерность массива

        .. code-block:: py

            array(
                [
                    [2, 4, 6, 8],
                    [3, 3, 2, 1],
                    [2, 6, 3, 4],
                    [5, 2, 3, 5]
                ]
            ).shape
            # (4, 4)


    .. py:attribute:: size

        Количесвто элементов в массиве

        .. code-block:: py

            numpy.random.randint(10, size=(3, 4, 5)).size
            # 60


    .. py:method:: dot(array)

        .. code-block:: py

            array([2, 4]).dot(array([2, 4]))
            # 20


    .. py:method:: reshape(size: tuple)

        Изменяет размерность массива

        .. code-block:: py

            arange(1, 10).reshape((3, 3))
            """
            array([
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ])
            """

            array([1, 2, 3]).reshape((1, 3))
            # array([[1, 2, 3]])


    .. py:method:: to_list()

        Возвращает содержимое в виде объекта :py:class:`list`

        .. code-block:: py

            a.to_list()
            # [10]


arange()
--------

.. py:function:: arange(start, end, step)

    Возвращает массив :py:class:`ndarray`, в указанном проежутке с указанным шагом

    .. code-block:: py

        arange(1, 2, 0.1)
        # array([ 1. ,  1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9])


array()
-------

.. py:function:: array(items: list [, dtype: str])

    Возвращает массив :py:class:`ndarray`

    .. code-block:: py

        array([1, 4, 2, 5, 3])
        # array([1, 4, 2, 5, 3])

        array([1, 2, 3, 4], dtype='float32')
        # array([ 1., 2., 3., 4.], dtype=float32)


concatenate()
-------------

.. py:function:: concatenate(list_arrays: list [, axis])

    Соединяет массивы и возвращает новый, результат объелдинения

    .. code-block:: py

        concatenate([
            array([1, 2, 3]),
            array([4, 5, 6]),
        ])
        # array([1, 2, 3, 4, 5, 6])

        concatenate([
            array([
                [1, 2, 3],
                [4, 5, 6],
            ]),
            array([
                [6, 7, 8],
                [7, 8, 9]
            ]),
        ])
        """
        array([
            [1, 2, 3], 
            [4, 5, 6],
            [6, 7, 8],
            [7, 8, 9],
        ])
        """

        concatenate([
            array([
                [1, 2, 3],
                [4, 5, 6],
            ]),
            array([
                [6, 7, 8],
                [7, 8, 9]
            ]),
        ], axis=1)
        """
        array([
            [1, 2, 3, 6, 7, 8], 
            [4, 5, 6, 7, 8, 9],
        ])
        """


dot()
-----

.. py:function:: dot(*arrays)

    .. code-block:: py

        dot(
            array([
                [1, 1], 
                [2, 2]
            ]), 
            array([
                [4, 4], 
                [6, 6]
            ]),
        )
        # array([[10, 10], [20, 20]])


dsplit()
--------

.. py:function:: dsplit()


dstack()
--------

.. py:function:: dstack()

    Аналогично встроенной функции :py:meth:`zip`

    .. code-block:: py

        ndstack((
            array([1, 2, 3]), 
            array([10, 20, 30])
        ))
        """
        array([
            [
                [1, 10], 
                [2, 20], 
                [3, 30]
            ]
        ])


einsum()
--------

.. py:function:: einsum()

    .. code-block:: py

        einsum(
            'i,i', 
            array([2, 2]), 
            array([4, 4])
        )
        # 16

        einsum(
            'ij,jk', 
            array([[1,1], [2, 2]]), 
            array([[4,4], [6, 6]])
        )
        """
        array([
            [10, 10], 
            [20, 20]
        ])


empty()
-------

.. py:function:: empty(size: int)

    Возвращает массив указанной размерности

    .. code-block: py

        empty(3)
        # array([1., 1., 1.])


eye()
-----

.. py:function:: eye(size: int)

    Возвращает единичную матрицу указанной размерности

    .. code-block:: py

        eye(2)
        """
        array([
            [1., 0.], 
            [0., 1.]
        ])


full()
------

.. py:method:: full(size, defualt)

    Возвращает массив указанного размера, заполненного дефолтными значениями

    .. code-block:: py

        full((2, 3), 3.14)
        """
        array([
            [3.14., 3.14, 3.14], 
            [3.14, 3.14, 3.14]
        ])


hsplit()
--------

.. py:function:: hsplit(array: ndarray, size: tuple)

    .. code-block:: py

        hsplit(
            arange(16).reshape((4, 4)),
            [2]
        )
        """
        [
            [0, 1],
            [4, 5],
            [8, 9],
            [12, 13]
        ]
        [
            [2, 3],
            [6, 7],
            [10, 11],
            [14, 15]
        ]
        """


hstack()
--------

.. py:function:: hstack(array_list: list)

    .. code-block:: py

        hstack([
            array([
                [9, 8, 7],
                [6, 5, 4],
            ]),
            array([
                [99],
                [99]
            ])
        ])
        """
        array([
            [9, 8, 7, 99],
            [6, 5, 4, 99]
        ])
        """


inner()
-------

.. py:function:: inner(*arrays)

    .. code-block:: py

        inner(
            array([2, 2]), 
            array([4, 4])
        )
        # 16


linspace
--------

.. py:method:: linspace(start, stop, step)

    Возвращает массив из указанного промежукта, с равномерным распределнием значений

    .. code-block:: py

        numpy.linspace(0, 1, 5)
        # array([0., 0.25, 0.5, 0.75, 1.])


ones
----

.. py:method:: ones(size: tuple, dtype: int)

    Создает многомерный массив заполненный единицами

    .. code-block:: py

        numpy.ones((2, 3), dtype=int)
        """
        array([
            [1., 1., 1.], 
            [1., 1., 1.]
        ])


reshape
-------

.. py:method:: reshape(array, new_shape)

    .. code-block:: py

        reshape(arange(9), (3, 3))
        """
        array([
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8]
        ])
        """

        reshape(arange(9), (3, 2))
        # ValueError: cannot reshape array of size 9 into shape (3,2)


split()
-------

.. py:function:: split(items: list, size: tuple)

    .. code-block:: py

        x1, x2, x3 = split(
            [1, 2, 3, 99, 99, 3, 2, 1], 
            (3, 5)
        )
        """
        x1 = [1, 2, 3]
        x2 = [99, 99]
        x3 = [3, 2, 1]
        """


vsplit()
--------

.. py:function:: vsplit(array: ndarray, size: tuple)

    .. code-block:: py

        vsplit(
            arange(16).reshape((4, 4)),
            [2]
        )
        """
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7]
        ]
        [
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ]
        """


vstack()
--------

.. py:function:: vstack()

    .. code-block:: py

        vstack([
            array(1, 2, 3),
            array([
                [9, 8, 7],
                [6, 5, 4],
            ])
        ])
        """
        array([
            [1, 2, 3],
            [9, 8, 7],
            [6, 5, 4],            
        ])
        """


zeros()
-------

.. py:method:: zeros(count: int [, dtype])

    Создает массив из нулей

    .. code-block:: py

        zeros(10, dtype=int)
        # array[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]