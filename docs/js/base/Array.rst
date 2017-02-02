Array
=====


.. py:class:: Array()
.. py:class:: Array(размер)
.. py:class:: Array(элемент0, элемент1, ...)

    Массив 

    Наследник :py:class:`Object`
    
    .. code-block:: js

        var array = [];

        var cities = ['moscow', 'kazan'];
        cities.length;
        // 2

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

    .. code-block:: js

        var a = new Array();

        var b = new Array('hey', 'you');

        var c = new Array(3);

        var a = [];
        a[5] = 5;
        for (var x in a){ 
            // выведет только 5
            ...
        }
        for (var i=0; i<a.length; i++){
            // выведет все 5 элементов
            ...
        }

    .. note:: EcmsScript6

        .. code-block:: js

            let [a, b, c] = [1, 2, 3];

            let [a, , b] = [1, 2, 3];
            console.log(a, b);
            // 1, 3

            let [a, ...b] = [1, 2, 3, 4];
            console.log(b);
            // [2, 3, 4]

            let [a, , , ...b] = [1, 2, 3, 4, 5, 6];
            console.log(b);
            // [4, 5, 6]


    .. py:attribute:: length

        Возвращает число, количество элементов в массиве
        
        .. code-block:: js

            ['moscow', 'kazan'].length; 
            // 2  


    .. py:method:: concat(item...)

        Возвращает новый массив, расширенный значениями из аргумента

        Ели аргументом является массив, то добавляются только те элменты
        которых нет в исходном массиве

        .. code-block:: js

            var a = [1, 2, 3];

            a.concat([4, 5], 'end'); 
            // [1, 2, 3, 4, 5, 'end']  

            a.concat([4, 5])
            // [1, 2, 3, 4, 5]


    .. py:method:: copyWithin(targetIndex, startIndex, endIndex)

        Копирует последовательность значений массива в другое место этого массива

        .. versionadded:: EcmaScript6

        .. code-block:: js

            let arr1 = [1, 2, 3, 4, 5];
            arr1.copyWithin(1, 2, 4);
            arr1;
            // 1, 3, 4, 4, 5

            let arr2 = [1, 2, 3, 4, 5];
            arr2.copyWithin(0, 1);
            arr2;
            // 2, 3, 4, 5, 5

            let arr3 = [1, 2, 3, 4, 5];
            arr3.copyWithin(1, -2);
            arr3;
            // 1, 4, 5, 4, 5

            let arr4 = [1, 2, 3, 4, 5];
            arr4.copyWithin(1, -2, -1);
            arr4;
            // 1, 4, 3, 4, 5


    .. py:method:: entries()

        Возвращает итерируемый объект, содержащий массив пары ключ/значение, для каждого индекса массива.

        .. versionadded:: EcmaScript6


    .. py:method:: every(callback[, this])

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


    .. py:method:: fill(value, startIndex, endIndex)

        Заменяет все элементы массива в казанном промежутке указанным значением.

        .. note:: EcmaScript6

        .. code-block:: js

            [1, 2, 3, 4].fill(5);
            // [5, 5, 5, 5]

            [1, 2, 3, 4].fill(5, 1, 2);
            // [1, 5, 3, 4]

            [1, 2, 3, 4].fill(5, 1, 3);
            // [1, 5, 5, 4]

            [1, 2, 3, 4].fill(5, -3, 2);
            // [1, 5, 3, 4]

            [1, 2, 3, 4].fill(5, 0, -2);
            // [5, 5, 3, 4]


    .. py:method:: filter(callback[, filter])

        Возвращает массив элементов, удовлетворяющих требованиям обработчика

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].filter(function(item, index, array) {
                return item > 1;
            });
            // [2, 3]


    .. py:method:: find(testingFunc, this)

        Возвращает элемент массива, который удовлетворяет условиям функции проверки

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [11, 12, 13].find(function(value, index, array){
                if (value == this){
                    return true;
                }
            }, 12);
            // 12


    .. py:method:: findIndex(testingFunc, this)

        Возвращает индекс элемента массива удовлетворяющего условию

        .. versionadded:: EcmaScript6

        .. code-block:: js

            [11, 12, 13].find(function(value, index, array){
                if (value == this){
                    return true;
                }
            }, 12);
            // 1

        
    .. py:method:: forEach(callback[, this])

        Вызывает функцию-обработчик для каждого элемента массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].forEach(function(item, index, array){
                ...
            }); 


    .. py:method:: from(iterable, function, this)

        .. note:: ECMAScript6

        .. code-block:: js

            Array.from("1, 2, 3", function(item){
                return this.number * item;
            }, {number: 10});
            // [10, 20, 30]


    .. py:method:: join(separator=',')

        Возвращает строку,
        полученную преобразованием всех элементов массива в строки и
        объединенные через разделитель

        .. versionadded:: ECMAScript5
        
        .. code-block:: js

            [1,2,3].join('');
            // '123'


    .. py:method:: indexOf(значение[, int pos=0])

        Возвращает число, позиция элемента в массиве

        .. versionadded:: ECMAScript5

        .. code-block:: js

            ['a','b','c'].indexOf('b');   
            // 1
            
            ['a','b','c'].indexOf('d');   
            // -1

            ['a','b','c'].indexOf('a', 1); 
            // -1


    .. py:method:: keys()

        Возвращает итерируемый объект, содержащий ключи для всех идексов массива.

        .. versionadded:: EcmaScript6


    .. py:method:: lastIndexOf(значение[, int pos=array.length])

        Возвращает число, позиция элемента в массиве в обратном порядке

        .. versionadded:: ECMAScript5


    .. py:method:: map(callback[, this])

        Возвращает массив, вычисленный по функции-обработчику

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].map(function(item, index, array) {
                return item * item;
            }); 
            // [1, 4, 9]

            
    .. py:method:: of(values...)

        Создает массив из 1 значения

        .. note:: EcmaScript6

        .. code-block:: js

            Array(2);
            // []

            Array.of(2);
            // [2]


    .. py:method:: pop()

        Возвращает последний элемент и удаляет его из массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            var c = [1,2,3];
            c.pop();
            // 3
            c;
            // [1,2]

            
    .. py:method:: push(item...)

         Добавляет объект в конец массива и возвращает количесвто элементов в массиве

        .. code-block:: js

            var c = [1,2,3];
            c.push(4);
            c;
            // [1,2,3,4]

        .. code-block:: js

            // копирование значений из одного массива в другой
            var array1 = [2, 3, 4];
            var array2 = [1];
            Array.prototype.push.apply(array2, array1);
            // [1, 2, 3, 4]

        .. note:: EcmaScript6

            .. code-block:: js

                // копирование значений из одного массива в другой
                var array1 = [2, 3, 4];
                var array2 = [1];
                array2.push(...array1)
                // [1, 2, 3, 4]


    .. py:method:: reduce(callback[, int start=0])

        Вычисляет значение на основе элементов данного массива, свертка массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].reduce(function(a, b){
                return a + b;
            });
            // 6


    .. py:method:: reduceRight(callback[, int start=0])

        Вычисляет значение на основе элементов данного массива,
        спарва налево, свертка массива

        .. versionadded:: ECMAScript5


    .. py:method:: reverse()

        Возвращает развернутый в обратныом порядке массив

        .. code-block:: js

            var a = [1, 2, 3];
            a.reverse();
            // [3, 2, 1]


    .. py:method:: shift()

        Возвращает первый элемент массива, и удалеят его из массива

        .. code-block:: js

            var a = [1, [2, 3], 4];
            var b = a.shift();
            // 1
            a;
            // [[2, 3], 4]


    .. py:method:: slice(start, end)

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


    .. py:method:: some(callback[, this])

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


    .. py:method:: sort([comparator])

        Сортирует массив, принимает функцию сравнения,
        которая может вернуть -1, 0, 1

        .. code-block:: js

            var a = [1, 2, 15];
            a.sort();
            a;
            // [1, 15, 2]

            a.sort(func(a, b){});


    .. py:method:: splice(start, deleteCount, item...)

        Удаляет указанный срез и возвращает их,
        вставляя в исходный массив указанные элементы массива

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


    .. py:method:: unshift(item...)

        Добавляет в начало массива элементы и возвращает длину массива

        .. code-block:: js

            var a = [];
            a.unshift(1);
            a;
            // [1]


    .. py:method:: values()

        Возвращает итерируемый объект, содержащий значения элементов массива.

        .. versionadded:: EcmaScript6
        