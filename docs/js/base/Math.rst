Math - математические операции
==============================

.. js:class:: Math()

    
    .. js:attribute:: E

        Основание натуральных логарифмов


    .. js:attribute:: LN10

        Натуральный логарифм числа 10


    .. js:attribute:: LN2

        Натуральный логарифм числа 2
    

    .. js:attribute:: LOG10E

        Десятичный логарифм числа Е


    .. js:attribute:: LOG2E

        Логарифм числа Е по основанию 2


    .. js:attribute:: PI

        Число пи


    .. js:attribute:: SQRT1_2

        Единица, деленная на корень квадратный из 2


    .. js:attribute:: SQRT2

        Квадратный корень из 2


    .. js:function:: abs(var)

        Возвращает абсолютное значение


    .. js:function:: cbrt(value)

        Корень кубический

        .. code-block:: js

            Math.cbrt(8);
            // 2


    .. js:function:: ceil(var)

        Округление в большую сторону

        .. code-block:: js

            a = Math.ceil(1.99);  // 2.0
            b = Math.ceil(1.01);  // 2.0
            c = Math.ceil(1.0);   // 1.0
            d = Math.ceil(-1.99); // -1.0


    .. js:function:: clz32(number)

        Возвращает число ведущих нулевых бит в 32 битном представлении числа

        .. note:: EcmaScript6

        .. code-block:: js

            Math.clz32(7);
            // 29

            Math.clz32(1000);
            // 22

            Math.clz32(295000000);
            // 3


    .. js:function:: exp(var)

        Вычисляет степень числа Е


    .. js:function:: expm1(value)

        Обратное от Math.log1p

        .. note:: EcmaScript6

        .. code-block:: js

            Math.expm1(0);
            // 0


    .. js:function:: floor(var)

        Округление в меньшую сторону

        .. code-block:: js

            a = Math.ceil(1.99);  // 1.0
            b = Math.ceil(1.01);  // 1.0
            c = Math.ceil(1.0);   // 1.0
            d = Math.ceil(-1.99); // -2.0


    .. js:function:: fround(number)

        Округляет число до 32 битного значения с плавающей точкой

        .. note:: EcmaScript6

        .. code-block:: js

            Math.fround(0);
            // 0
            
            Math.fround(1);
            // 1

            Math.fround(1.137);
            // 1.13699....

            Math.fround(1.5);
            // 1.5
            

    .. js:function:: imul(int1, int2)

        Возвращает младшие 32 бита результата умножения аргументов

        .. note:: EcmaScript6

        .. code-block:: js

            Math.imul(590, 5000000);
            // -1344967296
            
            590 * 5000000;
            // 2950000000


    .. js:function:: log(var)

        Вычисляет натуральный логарифм


    .. js:function:: log2(var)

        Вычисляет логарифм по основанию 2

        .. note:: EcmaScript6

        .. code-block:: js

            Math.log2(16);
            // 4


    .. js:function:: log10(var)

        Вычисляет логарифм по основанию 10

        .. note:: EcmaScript6

        .. code-block:: js

            Math.log10(1000);
            // 3


    .. js:function:: log1p(value)

        Вычисляет логарифм (1 + value)

        .. note:: EcmaScript6

        .. code-block:: js

            Math.log1p(0);
            // 0


    .. js:function:: max(var1, var2, ....)

        Возвращает максимум из переданных аргументов


    .. js:function:: min(var1, var2, ....)

        Возвращает минимум из переданных аргументов


    .. js:function:: pow(var, pow)

        Возведение в степень

        .. code-block:: js

            Math.pow(5, 2);
            //25


    .. js:function:: random()

        Возвращает случайное число из промежутка от 0 до 1

        .. code-block:: js

            Math.random()
            // 0.33


    .. js:function:: round(var)

        Нормальное округление


    .. js:function:: sign(number)

        Возвращает знак числа, сообщающий, является ли число отрицательным, положительным или равно нулю.

        .. note:: EcmaScript6

        .. code-block:: js

            Math.sign(11);
            // 1

            Math.sign(-11);
            // -1

            Math.sign(0);
            // 0


    .. js:function:: sqrt(int)

        Возвращает квадратный корень числа

        .. code-block:: js

            Math.sqrt(81);
            // 9


    .. js:function:: trunc(number)

        Возвращает целую часть числа

        .. note:: EcmaScript6

        .. code-block:: js

            Math.trunc(11.17);
            // 11

            Math.trunc(-1.112);
            // -1


Тригонометрические функции
--------------------------

    .. js:function:: acos()

        Вычисляет арккосинус


    .. js:function:: acosh()

        Вычисляет обратный гиперболический косинус

        .. note:: EcmaScript6

        .. code-block:: js

            Math.acosh(1);
            // 0


    .. js:function:: asin()

        Вычисляет арксинус


    .. js:function:: asinh()

        Вычисляет обратный гиперболический синус

        .. note:: EcmaScript6

        .. code-block:: js

            Math.asinh(0);
            // 0


    .. js:function:: atan()

        Вычисляет арктангенс


    .. js:function:: atanh()

        Вычисляет обратный гиперболический тангенс

        .. note:: EcmaScript6

        .. code-block:: js

            Math.atanh(0);
            // 0


    .. js:function:: atan2()

        Вычисляет угол между осью Х и точкой


    .. js:function:: cos()

        Вычисляет косинус


    .. js:function:: cosh()

        Вычисляет гиперболический косинус

        .. note:: EcmaScript6

        .. code-block:: js

            Math.cosh(0);
            // 1


    .. js:function:: hypot()

        Теорема Пифагора

        .. note:: EcmaScript6

        .. code-block:: js

            Math.hypot(2, 2, 1);
            // 3


    .. js:function:: sin()

        Вычисляет синус


    .. js:function:: sinh()

        Вычисляет гиперболический синус

        .. note:: EcmaScript6

        .. code-block:: js

            Math.sinh(0);
            // 0


    .. js:function:: tan()

        Вычисляет тангенс


    .. js:function:: tanh()

        Вычисляет гиперболический тангенс

        .. note:: EcmaScript6

        .. code-block:: js

            Math.tanh(0);
            // 0