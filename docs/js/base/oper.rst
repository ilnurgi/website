Операторы
=========


Логические
----------

======== ========
оператор описание
======== ========
||       или
&&       И
!        не
======== ========


Битовые 
-------

======== ========
Оператор Описание
======== ========
&        И (AND)
\|        ИЛИ (OR)
^        XOR
~        НЕ (NOT)
<<       Shift Left
>>       Shift Right
\>>>     Shift Right
======== ========

.. code-block:: js

    var a = 5;
    var b = 13;

    a | b;
    // OR, 13

    a & b;
    // AND, 5

    a ^ b;
    // XOR, 8

    ~a;
    // NOT, -6

    a >> b;
    // RIGHT SHIFT, 0

    a << b:
    // LEFT SHIFT, 40960

    a >>> b;
    // ZERO FILLED RIGHT SHIFT, 0

Бинарные
--------

.. code-block:: js

    'Hello' + 'GoIt';
    // HelloGoIT

    '1' + 2;
    // '12'

    2 + '1'
    // '21'

    '1' - 2
    // '-1'

    6 / '2'
    // '3'

    +1
    // 1

    +(1-2);
    // -1

    +'2' + +'3';
    // 5


Условия
-------

.. code-block:: js

    if (){
        ...
    } else if () {
        ...
    } else () {

    }

.. code-block:: js

    (age == 18) ? alert('Большой'): alert('Маленький')

.. code-block:: js

    var a = 1;
    switch(a) {
        case 1:
            console.log('one');
            break;
        case 0:
            console.log('zero');
            break;
        default:
            console.log('not one zero')
    }

Циклы
-----

.. code-block:: js

    for (var i=0, max = myarray.length; i < max; i++){
        console.log(i);
    }

    for (attr in obj) {
        console.log(attr);
    }

.. code-block:: js

    var i = 0;
    while (i < 5) {
        console.log(i);
        i++;
    }

.. code-block:: js

    do {
        ...
    } while (...)

.. note:: EcmaScript6

    .. code-block:: js

        // обход значений итерируемого объекта
        function* gf(){
            yield 1; 
            yield 2; 
        }
        for (let value of gf()){
            ...
        }

    .. code-block:: js

        // обход значений итерируемого объекта
        for (let value of [1, 2, 3]){
            ...
        }


Исключения
----------

.. code-block:: js

    if (typeof a !== 'number' || typeof b !== 'number') {
        throw {
            name: 'TypeError',
            message: 'add needs numbers'
        };

        // throw 'error text';
        // throw 123;
        // throw new Error("message");
    }

.. code-block:: js

    try {
        // код который вызывает исключение
    } catche (e) {
        // перехват исключений
    } finally {
        // данный блок выполнится в любом случае
    }


Оператор расширения
-------------------

.. note:: EcmaScript6

.. code-block:: js

    function some(a, b){
        return a + b;
    };
    var data = [1, 4];
    some(...data);

.. code-block:: js

    let array1 = [2, 3, 4];
    let array2 = [1, ...array1, 5, 6, 7];
    // 1, 2, 3, 4, 5, 6, 7



break
-----

Прерывает работу циклов


const
-----

Объявление переменных, доступных только для чтения в пределах блока.

.. code-block:: js

    const PI = 3.14;


continue
--------

Перейти к новой итерации цикла


debugger
--------

Устанавливает точу останова для интерпретатора

.. code-block:: js

    function(){
        debugger;
    };


.. _delete:

delete
------

Удаляет объекты

.. code-block:: js

    var a = [3, 4];
    del a[1];
    a;
    // [4]


in
--

Проверка существования свойства в объекте, по всей цепочке прототипов

.. code-block:: js

    console.log('x' in point);
    // true


instanceof
----------

Проверяет тип объекта

.. code-block:: js

    function Human(){

        if (! (this instanceof Human)) {
            return new Human();
        }
    }


let
---

.. note:: EcmaScript6

Объявление переменных с областью видимости в пределах блока и возможностью инициализации их значений

Отличие от :ref:`var`_:
    
    * переменная доступна только внутри блока

    * переменную повторно нельзя объявить в той области видимости

.. code-block:: js
    
    function some() {
        if (true){
            // переменная доступная только в условии
            let a = 5;
        }
    }


typeof
------

Тип объекта

.. code-block:: js

    typeof undefined;
    // "undefined"

    typeof 0;
    // "number"

    typeof true;
    // "boolean"

    typeof "foo";
    // "string"

    typeof {};
    // "object"

    typeof null;
    // "object"

    typeof function(){};
    // "function"


use strict
----------

Директива включает строгий режим

.. code-block:: js

    'use strict';


.. _var:

var 
---

Объявляет переменную, доступную внутри области видимости функции


yield, yield*
-------------

.. note:: EcmaScript6

Приостанавливает функцию и возвращает значение

yield* - принимает итерируемый объект и выполняет итерации по нему

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

    function* gf1(){
        yield 2;
        yield 3;
    }
    function* gf2(){
        yield 1;
        yield* gf1();
        yield* [4, 5];
    }
    var g = gf2();
    g.next().value;
    // 1
    g.next().value;
    // 2
    g.next().value;
    // 3
    g.next().value;
    // 4
    g.next().value;
    // 5