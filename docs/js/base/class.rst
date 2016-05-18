Классы
======

В javascript нету классов в чистом виде,
"классы" создают используя функции с оператором :ref:`new`, однако, в EcmaScript6 добавили классы :ref:`class`.

.. _new:

new
---

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


.. _class:

class
-----

.. note:: Добавлено в EcmaScript6

    .. code-block:: js

        class Person {

            constructor(name) {
                this._name = name;
            }

            get name(){
                return this._name;
            }

            set name(value){
                this.name = name;
            }

            static getDefaultName(){
                // статический метод
                return 'ilnurgi';
            }

            * generator_function() {
                yield 1;
                yield 2;
            }
        }

        // статическое свойство
        Person.age = 26;

        let user = new Person('Ilnur');

    .. code-block:: js

        let Task = class {
            
        }



Наследование
------------

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

.. note:: EcmaScript6

    .. code-block:: js

        class Task {
            constructor(){
                ...
            }
        }        

        class SubTask extends Task {
            constructor(){
                // вызов родительского метода обязателен
                super();
                ...
            }
        }


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


