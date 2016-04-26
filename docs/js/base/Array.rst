Array - массивы
===============


.. js:class:: Array()
.. js:class:: Array(размер)
.. js:class:: Array(элемент0, элемент1, ...)

    Массив 

    Наследник :js:class:`Object`
    

    .. code-block:: js

        var array = [];

        var cities = ['moscow', 'kazan'];
        cities[0];
        // 'moscow'

        cities[3] = 'abakan';
        cities.length;
        // 4
        
        cities;
        //['moscow', 'kazan', '', 'abakan']

        cities.length = 2;
        cities;
        // ['moscow', 'kazan']

        cities['city'] = 45;
        cities.length;
        // 2

        var a = new Array();

        var b = new Array('hey', 'you');

        var c = new Array(3);

        var a = [];
        a[5] = 5;
        for (var x in a){ 
            // выведет только 5
        }
        for (var i=0; i<a.length; i++){
            // выведет все 5 элементов
        }


    .. js:attribute:: length

        Возвращает число, количество элементов в массиве
        
        .. code-block:: js

            ['moscow', 'kazan'].length; 
            // 2  


    .. js:function:: concat(значение, ...)

        Возвращает новый массив, расширенный значениями из аргумента

        .. code-block:: js

            var a = [1, 2, 3];

            a.concat([4, 5], 'end'); 
            // [1, 2, 3, 4, 5, 'end']  

            a.concat([4, 5])
            // [1, 2, 3, 4, 5]


    .. js:function:: every(callback[, this])

        Возвращает булево, соответсвие всех элементов массива условию обработчика.

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].every(function(item, index, array){
                return x < 5
            });
            // true

            [1, 2, 3].every(function(item, index, array){
                return x < 3
            });
            // false



    .. js:function:: filter(callback[, filter])

        Возвращает массив элементов, удовлетворяющих требованиям обработчика

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].filter(function(item, index, array) {
                return item > 1;
            });
            // [2, 3]


    .. js:function:: forEach(callback[, this])

        Вызывает функцию-обработчик для каждого элемента массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].forEach(function(item, index, array){
                ...
            }); 


    .. js:function:: from(args)

        .. versionadded:: ECMAScript6

        .. code-block:: js

            var arr = Array.from(arguments);            


    .. js:function:: join([str splitter=','])

        Возвращает строку, полученную преобразованием всех элементов массива в строки и сконкатенированные

        .. versionadded:: ECMAScript5
        
        .. code-block:: js

            [1,2,3].join('');
            // '123'


    .. js:function:: indexOf(значение[, int pos=0])

        Возвращает число, позиция элемента в массиве

        .. versionadded:: ECMAScript5

        .. code-block:: js

            ['a','b','c'].indexOf('b');   
            // 1
            
            ['a','b','c'].indexOf('d');   
            // -1

            ['a','b','c'].indexOf('a', 1); 
            // -1



    .. js:function:: lastIndexOf(значение[, int pos=array.length])

        Возвращает число, позиция элемента в массиве в обратном порядке

        .. versionadded:: ECMAScript5


    .. js:function:: map(callback[, this])

        Возвращает массив, вычисленный по функции-обработчику

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].map(function(item, index, array) {
                return item * item;
            }); 
            // [1, 4, 9]

            
    .. js:function:: pop()

        Возвращает последний элемент и удаляет его из массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            var c = [1,2,3];
            c.pop();
            // 3
            c;
            // [1,2]

            
    .. js:function:: push(значение1, ...)

        Добавление объекта в массив в конец

        .. code-block:: js

            var c = [1,2,3];
            c.push(4);
            c;
            // [1,2,3,4]


    .. js:function:: reduce(callback[, int start=0])

        Вычисляет значение на основе элементов данного массива, свертка массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].reduce(function(a, b){
                return a + b;
            });
            // 6


    .. js:function:: reduceRight(callback[, int start=0])

        Вычисляет значение на основе элементов данного массива,
        спарва налево, свертка массива

        .. versionadded:: ECMAScript5


    .. js:function:: reverse(func, start)

        Разворачивание массива

        .. code-block:: js

            var a = [1, 2, 3];
            a.reverse();
            // [3, 2, 1]


    .. js:function:: shift()

        Возвращает первый элемент массива, и удалеят его из массива

        .. code-block:: js

            var a = [1, [2, 3], 4];
            var b = a.shift();
            // 1
            a;
            // [[2, 3], 4]


    .. js:function:: slice(start, end)

        Возвращает фрагмент массива

        .. code-block:: js

            [1, 2, 3, 4, 5].slice(0, 3);
            // [1, 2, 3]

            [1, 2, 3, 4, 5].slice(3);
            // [4, 5]

            [1, 2, 3, 4, 5].slice(1, -1);
            // [2, 3, 4]

            [1, 2, 3, 4, 5].slice(-3, -2);
            // [3]


    .. js:function:: some(callback[, this])

        Проверяет, возвращает ли предикат значение true хотя бы для одного элемента массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].some(function(item, index, array) {
                return x > 5;
            })
            // => false: нет эле­мен­тов > 5

            [1,2,3].some(function(item, index, array) {
                return x > 2;
            })
            // => true: не­ко­то­рые > 3

            [].some(function(item, index, array) {
                return true;
            });
            // => false: все­гда false для []


    .. js:function:: sort([sorter_func])

        Сортирует массив, принимает функцию сравнения,
        которая может вернуть -1, 0, 1

        .. code-block:: js

            var a = [1, 2, 15];
            a.sort();
            a;
            // [1, 15, 2]


    .. js:function:: splice(start, count, value1, value2, ...)

        Возвращает массив. Вставляет, удаляет или заменят элементы массива

        .. code-block:: js

            var c = [1, 2, 3, 4, 5];
            
            c.splice(1,2);
            // [2, 3]

            c;
            // [1, 4, 5];

            c.splice(1, 2, 33, 44);
            // [4, 5]

            c;
            // [1, 33, 44]


    .. js:function:: unshift(var1, var2 ...)

        Добавляет в начало массива элементы

        .. code-block:: js

            var a = [];
            a.unshift(1);
            a;
            // [1]