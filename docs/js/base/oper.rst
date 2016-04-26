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

if
--

.. code-block:: js

    var c1 = false, c2 = true, c3 = false;
    var a = c1 ? 1: (c2 ? 2: c3);

    if (){
        ...
    } else if () {
        ...
    }

for 
---

Итерация по элементам массива или объекта.

.. code-block:: js

    for (var i=0, max = myarray.length; i < max; i++){
        console.log(i);
    }

    for (attr in obj) {
        console.log(attr);
    }

while
-----

.. code-block:: js

    var i = 0;
    while (i < 5) {
        console.log(i);
        i++;
    }

switch
------

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

break
-----

Прерывает работу циклов


continue
--------

Перейти к новой итерации цикла


instanceof
----------

Проверяет тип объекта

.. code-block:: js

    function Human(){

        if (! (this instanceof Human)) {
            return new Human();
        }
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

in
--

Проверка существования свойства в объекте, по всей цепочке прототипов

.. code-block:: js
    
    console.log('x' in point);
    // true

?
-

.. code-block:: js

    (age == 18) ? alert('Большой'): alert('Маленький')


do - while
-----------

.. code-block:: js

    do {
        ...
    } while (...)


метки
-----

.. code-block:: js

    outer: for (...){
        inner: while (...){
            if (...){
                break inner;
            }
        }
    }


delete
------

Удаляет объекты

.. code-block:: js

    var a = [3, 4];
    del a[1];
    a;
    // [4]

typeof
------

Тип объекта

.. code-block:: js

    typeof true;
    // 'boolean'


debugger
--------

Устанавливает точу останова для интерпретатора

.. code-block:: js

    function(){
        debugger;
    };


use strict
----------

Директива включает строгий режим

.. code-block:: js

    'use strict';