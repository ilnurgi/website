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

if
--

Условие

.. code-block:: js

    var c1 = false, c2 = true, c3 = false;
    var a = c1 ? 1: (c2 ? 2: c3);

    if (){
        ...
    } else if () {
        ...
    }

?
-

.. code-block:: js

    (age == 18) ? alert('Большой'): alert('Маленький')


switch
------

Условие

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

for 
---

Циклы

.. code-block:: js

    for (var i=0, max = myarray.length; i < max; i++){
        console.log(i);
    }

    for (attr in obj) {
        console.log(attr);
    }

while
-----

Циклы

.. code-block:: js

    var i = 0;
    while (i < 5) {
        console.log(i);
        i++;
    }

do - while
----------

.. code-block:: js

    do {
        ...
    } while (...)


throw
-----

Прерывает выполнение функции, возбуждая исключение

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

try, catche, finally
--------------------

Перехват и обработка исключений

.. code-block:: js

    try {
        // код который вызывает исключение
    } catche (e) {
        // перехват исключений
    } finally {
        // данный блок выполнится в любом случае
    }

break
-----

Прерывает работу циклов


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