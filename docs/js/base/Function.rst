Функции
=======

Стандартные функции
-------------------

.. js:function:: isFinite()

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


.. js:class:: Function(args, function_body)

    Функция/конструктор функции, которая возвращает функцию

    Наследник :js:class:`Object`

    .. code-block:: js

        var func = Function("x", "y", "return x + y;")
        var result = func(20, 10)
        // 30


    .. js:attribute:: __proto__

        Ссылка экземпляра на прототип


    .. js:attribute:: arguments

        Массив аргументов, переданных функции


    .. js:attribute:: caller

        Ссылка на функцию, вызвавшую данную функцию


    .. js:attribute:: length

        Число именованных аргументов, указанных при объявлении функции


    .. js:attribute:: name

        Название функции


    .. js:attribute:: prototype
    
        Ссылка функции на прототип


    .. js:function:: apply(obj, arguments)

        Вызывает функцию с подменой контекста

        .. code-block:: js

            functionName.apply(thisArg, param1, param2)


    .. js:function:: bind(obj[, arguments])

        Возвращает новую функцию,
        которая вызывает данную,
        как метод указанного объекта с указанными аргументами.

        Таким образом можно подменить контекст

        .. code-block:: js

            function f(){...};
            var g = f.bind(o, 1, 2);
            // эквивалентно f.call(o, 1, 2, 3);


    .. js:function:: call(obj, argument1, ...)

        Вызывает функцию как метод указанного объекта


Самописные функции
------------------

Два метода создания функции

.. code-block:: js

    function name(){}
    // эта функция будет создана в самом начале при чтении скрипта

    var name = function(){}
    // эта функция будет создана тогда, когда интерпретаор до него дойдет


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