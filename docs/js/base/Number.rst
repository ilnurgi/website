Number - числа
==============


.. code-block:: js
    
    a = 1;
    a = 1.23;
    a = 1E6;

    // восьмиричная форма записи
    a = 045;

    // шестнадцатеричная форма
    a = 0x45;

    a = 10 % 3;
    // 2, остаток от целочисленного деления

    a++;
    a--;
    ++a;
    --a;
    a += 5;
    a -= 5;
    a /= 5;

    0.1 + 0.2 == 0.3;
    // false

    1 == 1.0;
    // true

    1/0;
    // Infinity - бесконечность

    -1/0;
    // -Infinity - бесконечность

.. note:: EcmaScript6

    .. code-block:: js

        // двоичное число
        let a = 0b00001111;

        // восьмиричное
        let b = 0o17;

.. js:class:: Number()
 
    Число, с типом float64

    Наследник :js:class:`Object`

    .. code-block:: js

        Number(10);
        // 10
        
        Number(“42.23”);
        // 42.23

        Number(“71oshi”);
        // Nan


    .. js:attribute:: EPSILON

        Расчетная погрешность при сравнений чисел с плавающей запятой

        
    .. js:attribute:: NaN

        Нечисло


    .. js:attribute:: NEGATIVE_INFINITY

        Отрицательная бесконечность


    .. js:attribute:: MIN_VALUE

        Наименьшее представимое число


    .. js:attribute:: MAX_SAFE_INTEGER

        .. note:: ECMAScript6


    .. js:attribute:: MAX_VALUE

        Наибольшее представимое число


    .. js:attribute:: MIN_SAFE_INTEGER

        .. note:: ECMAScript6


    .. js:attribute:: POSITIVE_INFINITY

        Положительная бесконечность


    .. js:function:: isFinite(number)

        Значение является конечным числом

        .. note:: ECMAScript6

        .. code-block:: js

            Number.isFinite(10);
            // true

            Number.isFinite(Nan);
            // false

            Number.isFinite(null);
            // false

            Number.isFinite([]);
            // false


    .. js:function:: isInteger(number)

        Переменная - целое число

        .. note:: ECMAScript6

        .. code-block:: js

            Number.isInteger(42);     
            // true
            
            Number.isInteger(42.000); 
            // true
            
            Number.isInteger(42.3);   
            // false

        .. code-block:: js

            // полифил
            if (!Number.isInteger){
                Number.isInteger = function(num){
                    return (
                        typeof num === 'number' && 
                        num % 1 == 0
                    );
                }
            }


    .. js:function:: isNan(number)

        Переменная Nan

        .. note:: ECMAScript6

        .. code-block:: js

            // полифил
            if (!Number.isNan){
                Number.isNan = function(num){
                    return (
                        typeof num === 'number' &&
                        window.isNan(num)
                    );
                }
            }


    .. js:function:: isSafeInteger(number)

        .. note:: ECMAScript6

        .. code-block:: js

            Number.isSafeInteger(Number.MAX_SAFE_INTEGER); // true
            Number.isSafeInteger(Math.pow(2, 53));         // false
            Number.isSafeInteger(Math.pow(2, 53) - 1);     // true

        .. code-block:: js

            // полифил
            if (!Number.isSafeInteger){
                Number.isSafeInteger = function(num){
                    return (
                        Number.isInteger(num) && 
                        Math.abs(num) <= Number.MAX_SAFE_INTEGER
                    );
                }
            }


    .. js:function:: toExponential([offset])

        Форматирует число в экспоненциальную форму представления

        .. code-block:: js

            var x = 123456789;

            x.toExponential();
            // '1.23456789e+8'

            x.toExponential(1);
            // '1.2e+8'

            x.toExponential(2);
            // '1.23e+8'

            x.toExponential(3);
            // '1.235e+8'


    .. js:function:: toFixed([offset])

        Возвращает строку, с определенным количеством знаков после запятой

        .. code-block:: js

            var y = 43.81327;
            
            y.toFixed();
            // '44'

            y.toFixed(1);
            // '43.8'
            
            y.toFixed(2);
            // '43.81'
            
            y.toFixed(3);
            // '43.813'


    .. js:function:: toPrecission()

        .. code-block:: js

            var n = 12345.6789;

            n.toPrecission(6);
            // '12345.7'

            n.toPrecission(4);
            // '1.235e+4'

    .. js:function:: toString()

        Возвращает строковое представление числа

        .. code-block:: js

            var n = 7432;

            n.toString();
            // '7432'

            n.toString(2);
            // '1110100001000'
