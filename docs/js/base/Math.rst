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


    .. js:function:: ceil(var)

        Округление в большую сторону

        .. code-block:: js

            a = Math.ceil(1.99);  // 2.0
            b = Math.ceil(1.01);  // 2.0
            c = Math.ceil(1.0);   // 1.0
            d = Math.ceil(-1.99); // -1.0


    .. js:function:: exp(var)

        Вычисляет степень числа Е


    .. js:function:: floor(var)

        Округление в меньшую сторону

        .. code-block:: js

            a = Math.ceil(1.99);  // 1.0
            b = Math.ceil(1.01);  // 1.0
            c = Math.ceil(1.0);   // 1.0
            d = Math.ceil(-1.99); // -2.0


    .. js:function:: log(var)

        Вычисляет натуральный логарифм


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


    .. js:function:: round(var)

        Нормальное округление


    .. js:function:: sqrt(int)

        Возвращает квадратный корень числа

        .. code-block:: js

            Math.sqrt(81);
            // 9

Тригонометрические функции
--------------------------

    .. js:function:: acos()

        Вычисляет арккосинус


    .. js:function:: asin()

        Вычисляет арксинус


    .. js:function:: atan()

        Вычисляет арктангенс


    .. js:function:: atan2()

        Вычисляет угол между осью Х и точкой


    .. js:function:: cos()

        Вычисляет косинус


    .. js:function:: sin()

        Вычисляет синус


    .. js:function:: tan()

        Вычисляет тангенс