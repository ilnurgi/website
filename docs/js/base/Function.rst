.. _function:

Функции
=======

Два метода создания функции

.. code-block:: js

    function name(){}
    // эта функция будет создана в самом начале при чтении скрипта

    var name = function(){}
    // эта функция будет создана тогда, когда интерпретаор до него дойдет


Стандартные функции
-------------------

.. py:function:: isFinite()

    Возвращает true  только тогда, когда n  — обычное число, а не одно из NaN , Infinity  и ‐Infinit

    .. code-block:: js

        isFinite(1);
        // true

        isFinite(Infinity);
        // false

        isFinite(NaN);
        // false


Function
--------


.. py:class:: Function(args, function_body)

    Функция/конструктор функции, которая возвращает функцию

    Наследник :py:class:`Object`

    .. code-block:: js

        var func = Function("x", "y", "return x + y;")
        var result = func(20, 10)
        // 30


    .. py:attribute:: __proto__

        Ссылка экземпляра на прототип


    .. py:attribute:: arguments

        Массив аргументов, переданных функции


    .. py:attribute:: caller

        Ссылка на функцию, вызвавшую данную функцию


    .. py:attribute:: length

        Число именованных аргументов, указанных при объявлении функции


    .. py:attribute:: name

        Название функции


    .. py:attribute:: prototype
    
        Ссылка функции на прототип


    .. py:method:: apply(thisArg, arguments)

        Вызывает функцию с подменой контекста

        .. code-block:: js

            functionName.apply(thisArg, param1, param2)


    .. py:method:: bind(obj[, arguments])

        Возвращает новую функцию,
        которая вызывает данную,
        как метод указанного объекта с указанными аргументами.

        Таким образом можно подменить контекст

        .. code-block:: js

            function f(){...};
            var g = f.bind(o, 1, 2);
            // эквивалентно f.call(o, 1, 2, 3);


    .. py:method:: call(obj, argument1, ...)

        Вызывает функцию как метод указанного объекта


arguments
---------

.. code-block:: js

    var average = function(x, y){
        // массив всех принятых аргументов
        console.log(arguments);

        return (x+y)/2;
    }

Анонимная функция
-----------------

.. code-block:: js
    
    (function(){
        var property = 1;
    })();


Замыкани
--------

.. code-block:: js

    var getAnswer = (function(){
        var answer = 42;

        return function inner(){
            // эта переменная замыкается
            return answer;
        };
    }());

    getAnswer();
    // 42


Области видимости
-----------------

.. code-block:: js

    var a = 10;
    (function() {
        console.log(a);
    })()
    // 10

    (function() {
        console.log(a);
        var a = 1;
    })()
    // undefined


Значения по умолчанию функции
-----------------------------

.. code-block:: js

    function some(x, y, z){
        x = x || 1;
        y = y || 2;
        z = z || 3;
        ...
    }

.. note:: 

    EcmaScript6

    .. code-block:: js

        function some(x=1, y=2, z=3){
            ...
        }


Распаковка аргументов
---------------------

.. code-block:: js

    function some(a, b){
        return a + b;
    }
    var data = [1, 4];
    some.apply(null, [data]);
    // 5

.. note:: 

    EcmaScript6

    .. code-block:: js

        function some(a, b){
            return a + b;
        }
        var data = [1, 4];
        some(...data);
        // 5


Стрелочные функции
------------------

.. note:: EcmaScript6

.. code-block:: js

    let circleArea = (pi, r) => {
        let area = pi * r * r;
        return area;
    }   
    let circleArea2 = (pi, r) => pi * r * r;
    let square = x => x * x;
    let log = () => console.log("Some text");
    let getPerson = () => ({ name: "ilnurgi" });
    (() => console.log("IIFE"))();
    
    circleArea(3.14, 3);
    // 28.26


Функция генератор
-----------------

.. note:: EcmaScript6

Функция возвращает несколько значений по одному. 

.. code-block:: js

    function* generator_function(){

        yield 1;
        yield 2;
    }
    var generator = generator_function()
    generator.next().value
    // 1
    generator.next().value
    // 2

.. code-block:: js
    
    // генератор с передачей параметра в yield
    function* generator_function(){
        var a = yield 12;
        var b = yield a + 1;
    }
    var generator = generator_function()
    generator.next().value
    // 12
    generator.next(5).value
    // 6

.. code-block:: js
    
    // досрочное завершение генератора
    function* generator_function(){
        var a = yield 12;
        var b = yield a + 1;
    }
    var generator = generator_function()
    generator.next().value
    // 12
    generator.return(5).value
    // 5

.. code-block:: js
    
    // вызов исключении в генераторе
    function* generator_function(){
        try {
            yield 1;
        } catch(e) {
            console.log("1st exception");
        }
        try {
            yield 2;
        } catch(e) {
            console.log("2st exception");
        }
    }
    var generator = generator_function()
    generator.next().value
    generator.throw("exception string").value
