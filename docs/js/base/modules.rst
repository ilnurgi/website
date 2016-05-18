Модули
======

В Java Script нету модулей. Но нечто подобное можно реализовать


.. code-block:: js

    var MyModule = {
        public_var: 1,
        public_method: function(){},
    };


.. code-block:: js

    /*
     * данный способ позволяет скрывать какие-то приватные методы
     */

    var MyModule = (function(){
        var private_var = [];
        return {
            public_var: 1,
            public_method: function(){
                ...
            },
        }
    }());