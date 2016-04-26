Функции
=======

Два метода создания функции

.. code-block:: jjs

    function name(){}
    // эта функция будет создана в самом начале при чтении скрипта

    var name = function(){}
    // эта функция будет создана тогда, когда интерпретаор до него дойдет


New
---

В javascript нету классов в чистом виде, "классы" создают используя функции с оператором New


.. code-block:: js

    function Human(name) {
        /*
         * конструктор
         *
         * при вызове этой функции через new, this это ново-создаваемый объект
         * иначе this глобальный
         */

        if (! (this instanceof Human)){
            // если это вызов не конструктора, то все равно вернем конструктор
            return new Human(name);
        }
        this.name = name;
    }

    /*
     * добавим метод прототипу
     * можно задать и в самом конструкторе, но потом его нельзя будет переопределить
     */
    Human.prototype.say = function(what) {
        console.log(this.name + ':' + what);
    }

    var alex = new Human('Alex');

    //подмена контекста, this

    var jack = new Human('Jack');

    alex.say.apply(jack, ['hi']);

Наследование

    .. code-block:: js

        var Track = function(){
            /*
             * конструктор какого то класса
             */
        }

        var YotubeTrack = function(){
            /*
             * конструктор какого то класса, наследник класса Track
             */

            // вызов родительского конструктора
            Track.apply(this)
        }

        // наследуем родительские методы
        YotubeTrack.prototype = Object.create(Track.prototype);
        // конструктор наследовать нам не надо
        YotubeTrack.prototype.constructor = YotubeTrack;


Миксины
-------

.. code-block:: js

    var nameMixin = {
        getName: function(){
            this.name;
        }
    };
    var controlsMixin = {
        play: function(){
            console.log(this.name + ' play');
        }
    }
    var Track = function(){};
    var Playlist = function(){};

    var extend = function(target){
        if (!arguments[1]){
            return;
        }
        for (var i=1; i<arguments.length; i++){
            var source = arguments[i];

            for(var prop in source){
                if (!target[prop] && source.hasOwnProperty(prop){
                    target[prop] = source[prop];
                }
            }
        }
    }
    extend(Track.prototype, namedMixin, controlMixin);
    extend(Playlist.prototype, namedMixin, controlMixin);


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


Примеры
-------

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
    (function() {
        console.log(a);
    })()
    // 10

    (function() {
        console.log(a);
        var a = 1;
    })()
    // undefined


стандартные функции
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