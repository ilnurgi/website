list
====

list
----

.. py:class:: list(iter_object)

    Список

    .. code-block:: py

        a = [1, 2, 3, 4, 5, 6]

        a[0]
        # 1

        a[0:5:2]
        #[1, 3]

    .. code-block:: py

        x, y = 1, 2
        x, y = y, x

        values = 1, 2
        x, y = values

        x, y, *z = 1, 2, 3, 4
        # z = [3, 4]

        first, *middle, last = 1, 2, 3, 4
        # middle = [2, 3]

        z, *y, z = 1, 2, 3
        # y = [2]

    .. code-block:: py

        s = []

    .. py:method:: append(obj)
        
        Добавляет новый объект в список

        .. code-block:: py

            [1, 2].append('3')
            # [1, 2, '3']


    .. py:method:: clear()

        Очищает список от данных

        .. code-block:: py

            s = [1, 2]
            s.clear()
            # []


    .. py:method:: copy()

        Возвращает копию списка

        .. code-block:: py

            a = [1, 2, 3]
            b = a.copy()
            b.append(4)

            b
            # [1, 2, 3, 4]
            a
            # [1, 2, 3]

            # эквивалентно 
            b = a[:]


    .. py:method:: count(obj)
        
        Возвращает :py:class:`int`, количество вхождений искомого объекта в списке
        
        .. code-block:: py

            [1].count(1)
            # 1


    .. py:method:: extend(iter_obj)

        Добавляет итерируемый объект в конец списка

        .. code-block:: py

            [1, 2].extend('qw')
            # [1, 2, 'q', 'w']


    .. py:method:: index(obj, [start_pos, end_pos])

        Возвращает :py:class:`int`, индекс позиции искомого элемента в списке
        
        .. code-block:: py

            [1].index(1)
            # 0


    .. py:method:: insert(index, obj)
        
        Вставляет в список объект по указаннной позиции

        .. code-block:: py

            [1, 2].insert(2, 3)
            # [1, 2, 3]


    .. py:method:: pop([index])
        
        Возвращает объект, по указанной позиции из списка, удалив объект из списка
        
        .. code-block:: py

            s = [1, 2]
            s.pop(1)
            # 2            
            # s = [1]


    .. py:method:: remove(obj)
        
        Удаляет из списка первый встреченный экземпляр аргумента

        .. code-block:: py

            [1, 2].remove(1)
            # [2]


    .. py:method:: reverse()
        
        Изменяет порядок следования элементов в списке на противоположный

        .. code-block:: py

            [1, 2].reverse()
            # [2, 1]


    .. py:method:: sort([key=None, reverse=False])

        Сортирует список в порядке возрастания

        * key - функция, которая сортирует список

        .. code-block:: py

            [5, 3, 8, 6, 1, 2, 0].sort()
            # [0, 1, 2, 3, 5, 6, 8]

            ['aardvark', 'abalone', 'acme', 'add', 'aerate'].sort(key=len)
            # ['add', 'acme', 'aerate', 'abalone', 'aardvark']

        .. code-block:: py

            from functools import cmp_to_key

            def event_comparator(event_1, event_2) -> dict:
                """
                сравниваем два события
                сначала по одному полю, а если они равны, то по второму полю
                """
                if event_1['importantLevel'] > event_2['importantLevel']:
                    return 1
                elif event_1['importantLevel'] < event_2['importantLevel']:
                    return -1
                elif event_1['beginDate'] > event_2['beginDate']:
                    return 1
                elif event_1['beginDate'] < event_2['beginDate']:
                    return -1
                else:
                    return 0

            events_list.sort(key=cmp_to_key(event_comparator))


Генераторы списка
-----------------

Генератор списка сначала фильтруют, а потом возвращают результат.

[element for variable(s) in list if condition]

* list — любой итерируемый элемент

* variable(s) — переменная или переменные,
  которые приравниваются к текущему элементу списка, аналогично циклу for

* condition — инлайновое выражение:
  если оно равно true, элемент добавляется в результат

* element — инлайновое выражение,
  результат которого используется как элемент списка-результата

.. code-block:: py

    [i for i in [1,2,3,4,5,6] if i > 3]
    #[4, 5, 6]

    arr = [[1, 2], [3, 4], [5, 6]]
    [j * 10 for i in arr for j in i if j % 2 == 0]
    # [20, 40, 60]

Генераторы очень быстрые по скорости работы. 
Допустим, надо возвести в квадрат все элементы списка.

.. code-block:: py

    import timeit
    a = """
        squares = []
        for number in range(20):
            if number < 10:
                squares.append(number*number)
        """
    timeit.repeat(a)
    # [1.3735721111297607, 1.3705899715423584, 1.3692619800567627]

    a = """
        squares = [number*number for number in range(20) if number < 10]
        """
    timeit.repeat(a)
    # [1.0607497692108154, 1.050074815750122, 1.0547380447387695]

    a = """
        squares = []
        for number in range(10):
            squares.append(number*number)
        """
    timeit.repeat(a)
    # [1.0115618705749512, 1.0128450393676758, 1.0099198818206787]

    a = """
        squares = [number*number for number in range(10)]
        """
    timeit.repeat(a)
    # [0.6439402103424072, 0.6230731010437012, 0.6240830421447754]

Выражения-генераторы
--------------------

Существует обратная сторона генератора списков: весь список должен находиться в памяти.
Это не проблема для маленьких списков, как в предыдущих примерах,
и даже на несколько порядков больше.

Но в конце концов это становится неэффективным.

Отличие их от генераторов списков состоит в том,
что они не загружают в память список целиком,
а создают 'generator object',
и в каждый момент загружен только один элемент списка.

Выражения-генераторы имеют такой же синтаксис,
как генераторы списков, но вместо квадратных скобок используются круглые:

.. code-block:: py

    numbers = (1, 2, 3, 4, 5)
    squares_under_10 = (number for number in numbers if number < 4)
    # squares_under_10 = <generator object <genexpr> at 0x175e7d0>
    for square in squares_under_10:
            print square,
    # 1 2 3
