Примеры
=======

Задача 1
--------

Посчитаем расстояние от центра (0, 0) до какойто точки (0, 2)

.. code-block:: py

    point = array([0, 2])
    center = array([0, 0])

    distance = point - center
    # array([0, 2])

    einsum('i,i', distance, distance)
    # 4


Задача 2
--------

Посчитаем квадраты рсстояний до точек

.. code-block:: py

    points = array([[0, 2], [0, 4], [2, 2], [4, 4]])
    center = array([0, 0])

    diffs = points - center
    # array([[0, 2], [0, 4], [2, 2], [4, 4]])

    diffs.shape
    # (4, 2)

    einsum('...i,...i', diffs, diffs)
    # array([4, 16, 8, 32])

    einsum('ij,ij->i', diffs, diffs)
    # array([4, 16, 8, 32])