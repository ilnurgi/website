.. py:module:: itertools

itertools
=========

Модуль содержит функции, создающие эффективные итераторы, 
которые позволяют выполнять итерации по данным различными способами. 

Все функции в этом модуле возвращают итераторы, 
которые можно использовать в инструкции for и в других функциях, 
где применяются итераторы, 
например в функциях-генераторах и в выражениях-генераторах.


accumulate
----------

.. py:method:: accumulate(iterable[ , function])

    на каждой итерации возвращает сумму предыду­щих элементов последовательности. 
    
    Начальное значение равно 0

    .. warning:: Добавлено в 3.2

    .. code-block:: py
    
        list(accumulate([1, 2, 3, 4, 5, 6]))
        # [1, 3, 6, 10, 15, 21]

        list(accumulate([1, 2, 3, 4, 5, 6], lambda a,b: a*b))
        # [1, 2, 6, 24, 120, 720]


chain 
-----

.. py:method:: chain(iterable...)

    Возвращает генератор,
    на каждой итерации возвращает элементы сначала из первой последовательности,
    затем из второй последовательности и т.д.

    .. code-block:: py
        
        list(itertools.chain([1,2,3], [4,5,6], [7,8,9]))
        # [1, 2, 3, 4, 5, 6, 7, 8, 9]


chain.from_iterable
-------------------

.. py:method:: chain.from_iterable(iterable)

    аналогична функции :py:meth:`chain`,
    но прини­мает одну последовательность.

    каждый элемент которой считается отдельной последо­вательностью.

    .. code-block:: py

        list(itertools.chain.from_iterable(['abc', 'def']))
        # ['a', 'b', 'c', 'd', 'e', 'f']


.. py:method:: combinations(iterable, r)
    
    Создает итератор, который возвращает все возможные последовательности из r элементов, взятых из итерируемого объекта iterable. Элементы в возвращаемых последовательностях располагаются в том же порядке, в каком они встречаются в исходном объекте iterable. 

    >>> list(itertools.combinations([1,2,3,4], 2))
    [[1,2], [1,3], [1,4], [2,3], [2, 4], [3,4]]


.. py:method:: combinations_with_replacement(<Последовательность>, <Количество комбинации>)
    
    Создает итератор, который возвращает кортеж, содержащий комбинацию из указанного количества элементов.

    >>> list(itertools.combinations([1,2,3,4], 2))
    [[1, 1], [1,2], [1,3], [1,4], [2, 2], [2,3], [2, 4], [3, 3], [3,4], [4, 4]]


.. py:method:: compress(<Фильтруемая последовательность>, <Последовательность логических значений>)

    производит фильтрацию последовательности, указанной в первом пара­метре. Элемент возвращается, только если соответствующий элемент (с таким же индек­сом) из второй последовательности трактуется как истина. Сравнение заканчивается, когда достигнут конец одной из последовательностей.

    >>> list(itertools.compress('абвгде', [1,0,0,0,1,1]))
    ['а', 'д', 'е']


.. py:method:: count(start=0, step=1)

    Создает итератор, который воспроизводит упорядоченную и непрерывную последовательность целых чисел, начиная с n. Если аргумент n опущен, в качестве первого значения возвращается число 0. (Обратите внимание, что этот итератор не поддерживает длинные целые числа. По достижении значения sys.maxint счетчик переполнится и итератор продолжит воспроизводить значения, начиная с -sys.maxint - 1.)

    >>> for i in itertools.count():
            if i > 5:
                break
            print i,
    0, 1, 2, 3, 4


cycle
-----

.. py:method:: cycle(iterable)
    
    Создает итератор,
    который в цикле многократно выполняет обход элементов в объекте iterable.

    За кулисами создает копию элементов в объекте iterable.

    Эта копия затем используется для многократного обхода элементов в цикле.

    .. code-block:: py

        for i in cycle([1, 2]):
            print(i)
        # 1
        # 2
        # 1
        # ...


.. py:method:: dropwhile(<Функция>, <Последовательность>)
    
    возвращает объект итератор, который в каждой итерации возвращает элемент последовательности, начиная с элемента, дляч которого функция, указанная в первом параметре вернет False

    >>> def func():
            return x > 3
    >>> list(itertools.dropwhile(func, [4, 5, 6, 0, 7, 2, 3]))
    [0, 7, 2, 3]


.. py:method:: filterfalse(<Функция>, <Последовательность>)

    возвращает объект итератор, который в каждой итерации возвращает элемент последовательности, для которой функция, указанная в первом параметре, вернет значение False. Если в первом параметре вместо названия функции указать значение None, то каждый элемент последовательности будет проверен на соответствие значению Fa1se. Если эле­мент в логическом контексте возвращает значение True, то он не будет входить в возвращаемый результат.

    >>> def func(x): 
            return x > 3
    >>> list(itertoo1s.filterfalse(func, [4, 5, 6, 2, 3]
    [0, 2, 3]


.. py:method:: groupby(iterable [, key])
    
    Создает итератор, который группирует одинаковые элементы из итерируемого объекта iterable, следующие друг за другом. Процесс группировки основан на поиске одинаковых элементов. Например, если итерируемый объект iterable возвращает один и тот же элемент несколько раз подряд, этот элемент образует группу. Если функция применяется к отсортированному списку, она образует группы по числу уникальных элементов в списке. В необязательном аргументе key может передаваться функция, которая будет применяться к каждому элементу; в этом случае в сравнивании соседних элементов участвуют возвращаемые значения этой функции, а не значения самих элементов. Итератор, возвращаемый функцией, воспроизводит кортежи (key, group), где элемент key – это значение ключа для группы, а элемент group – это итератор, который возвращает все элементы, попавшие в группу.


.. py:method:: ifilter(predicate, iterable)
    
    Создает итератор, который воспроизводит только те элементы из объекта iterable, для которых функция predicate(item) возвращает True. Если в аргументе predicate передать None, все элементы в объекте iterable будут оцениваться как True и будут возвращаться итератором.


.. py:method:: ifilterfalse(predicate, iterable)
    
    Создает итератор, который воспроизводит только те элементы из объекта iterable, для которых функция predicate(item) возвращает False. Если в аргументе predicate передать None, все элементы в объекте iterable будут оцениваться как False и будут возвращаться итератором.


.. py:method:: imap(function, iter1, iter2, ..., iterN)
    
    Создает итератор, который воспроизводит элементы function(i1,i2, ... iN), где i1, i2,..., iN – это элементы, полученные из итераторов iter1, iter2, ..., iterN соответственно. Если в аргументе function передать None, функция imap() вернет кортежи вида (i1, i2, ..., iN). Итерации прекращаются, когда один из указанных итераторов прекращает воспроизводить значения.


.. py:method:: islice(iterable, [start,] stop [, step])
    
    Создает итератор, воспроизводящий элементы, которые вернула бы операция извлечения среза iterable[start:stop:step]. Первые start элементов пропускаются и итерации прекращаются по достижении позиции, указанной в аргументе stop. В необязательном аргументе step передается шаг выборки элементов. В отличие от срезов, в аргументах start, stop и step не допускается использовать отрицательные значения. Если аргумент start опущен, итерации начинаются с 0. Если аргумент step опущен, по умолчанию используется шаг 1.


.. py:method:: izip(iter1, iter2, ... iterN)
    
    Создает итератор, который воспроизводит кортежи (i1, i2, ..., iN), где значения i1, i2, ..., iN извлекаются из итераторов iter1, iter2, ..., iterN соответственно. Итерации останавливаются, когда какой-либо из исходных итераторов прекращает возвращать значения. Итератор, возвращаемый этой функцией, воспроизводит те же значения, что и встроенная функция zip().


.. py:method:: izip_longest(iter1, iter2, ..., iterN [,fillvalue=None])
    
    То же, что и функция izip(), за исключением того, что возвращаемый итератор продолжает итерации, пока не будут исчерпаны все значения, воспроизводимые итераторами iter1, iter2 и так далее. В качестве недостающих значений для итераторов, которые оказались исчерпаны раньше всех, используется None, если не было указано иное значение в именованном аргументе fillvalue.


.. py:method:: permutations(<Последовательность> [ , <Количество элементов>])

    на каждой итерации возвращает кортеж, содержащий комбинацию из указанного количества элементов. Если количество элементов не указано, то использу­ется длина последовательности.

    >>> ["".join(i) for i in itertools.perrnutations('aбвг')]
    ['абвг', 'абгв', 'авбг', 'авгб', 'агбв', 'агвб', 'бавг', ...'гвба']


.. py:method:: product(<Последовательность1>, <Последовательность2>, ... [, repeat=1])
    
    на каждой итерации возвращает кортеж, содержащий комбинацию из эле­ментов одной или нескольких последовательностей

    >>> list(product('aбвг', repeat=2))
    [('а', 'а')' ('а'' 'б'), ('а', 'в'), ... ('г', 'г')]


.. py:method:: repeat(object [, times])
    
    Создает итератор, который многократно воспроизводит объект object. В необязательном аргументе times передается количество повторений. Если этот аргумент не задан, количество повторений будет бесконечным.


.. py:method:: starmap(<Функция>, <Последовательность>)
    
    передает значение в функцию и возраща­ет результат ее выполнения. Обратите внимание на то, что каждый элемент должен быть последовательностью. При передаче в функцию производится распаковка последова­тельности. Иными словами, в функцию передаются отдельные элементы последовательности, а не последовательность целиком. 

    >>> def func(x, y):
            return x + y
    >>> list(itertools.starmap(func, [(1,2), [3,4]]))
    [3, 7]


.. py:method:: takewhile(<Функция>, <Последовательность>)
    
    возвращает итератор, в каждой итерации возвращает элемент последовательности, пока не встретится элемент, для которой функция, указанная в превом параметре вернет значение False

    >>> def func():
            return x > 3
    >>> list(itertools.takewhile(func, [4, 5, 6, 0, 7, 2, 3]))
    [4, 5, 6]


.. py:method:: tee(<Последовательность> [ , <Количечтво>])
    
    возвращает кортеж, содержащий не­сколько итераторов для последовательности. Если второй параметр не указан, то воз­вращается кортеж из двух итераторов. Эта функция может принимать любые итерируемые объекты. При этом, когда оригинальный итератор клонируется, в кэше сохраняется его копия, которая используется во всех далее создаваемых итераторах. Будьте очень внимательны и не используйте оригинальный итератор iterable после вызова функции tee(). В противном случае механизм кэширования будет работать некорректно.

    >>> itertoo1s.tee([1, 2, 3])
    (<itertoo1s.tee object at Ox00rDB760>, <itertoo1s.tee object at Ox00rDB73B>)


.. py:method:: zip_longest(<Последовательность1> [ , ... <ПоследовательностьN>] [ , fillvalue=None])

    на каждой итерации возвращает кортеж, содержащий элементы после­довательностей, которые расположены на одинаковом смещении. Если последователь­ности имеют разное количество элементов, то вместо отсутствующего элемента вставля­ется объект, указанный в параметре fillva1ue.

    >>> list(itertools.zip_longest((1,2,3), [4]))
    [(1, 4), (2, None), (3, None)]