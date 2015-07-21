Function - функция
==================


.. js:class:: Function(args, function_body)

    Функция/конструктор объектов

    Наследник :js:class:`Object`


    .. js:attribute:: __proto__

        Ссылка экземпляра на прототип


    .. js:attribute:: arguments

        Массив аргументов, переданных функции


    .. js:attribute:: caller

        Ссылка на функцию, вызвавшую данную функцию


    .. js:attribute:: length

        Число именованных аргументов, указанных при объявлении функции


    .. js:attribute:: prototype
    
        Ссылка функции на прототип


    .. js:function:: apply(obj, arguments)

        Вызывает функцию как метод указанного объекта


    .. js:function:: bind(obj[, arguments])

        Возвращает новую функцию, которая вызывает данную как метод указанного объекта с указанными аргументами

        .. code-block:: js

            function f(){...};
            var g = f.bind(o, 1, 2);
            // эквивалентно f.call(o, 1, 2, 3);

    .. js:function:: call(obj, argument1, ...)

        Вызывает функцию как метод указанного объекта

    
.. code-block:: js
    
    // анонимная функция
    (function(){
        var property = 1;
    })();

    
.. code-block:: js

    var func = Function("x", "y", "return x + y;")
    var result = func(20, 10)
    // 30


.. code-block:: js

    // ничего не вернет
    function foo() {
        return
        {
            foo: 'bar'
        }
    }

    // вернет объект
    function bar() {
        return {
            foo: 'bar'
        }
    }


.. code-block:: js

    var average = function(x, y){
        // массив всех принятых аргументов
        console.log(arguments);

        return (x+y)/2;
    }


.. code-block:: js

    var a = 10;
    (function() { console.log(a); })()
    // 10

    (function() { console.log(a); var a = 1; })()
    // undefined


.. code-block:: js

    /* 
     * конструктор 
     */
    function Human(name) {
        // при вызове этой функции через new, this это ново-создаваемый объект
        // иначе this глобальный
        if (! (this instanceof Human)){
            // если это вызов не конструктора, то все равно вернем конструктор
            return new Human(name);
        }
        this.name = name;


    }

    Human.prototype.say = function(what) {
        console.log(this.name + ':' + what);
    }

    var alex = new Human('Alex');

    /*подмена контекста, this */

    var jack = new Human('Jack');

    alex.say.apply(jack, ['hi']);