BigInteger
==========

.. py:class:: BigInteger()

    наследник Number

    
    .. py:method:: BigInteger(String value)

        объект будет хранить большое целое число, заданное строкой цифр, перед которыми может стоять знак минус


    .. py:method:: BigInteger(String value, int radix)

        задается строка цифр со знаком value , записанная в системе счисления с основанием radix
    

    .. py:method:: BigInteger(byte[] value)

        объект будет хранить большое целое число, заданное массивом value , содержащим двоичное представление числа в дополнительном коде


    .. py:method:: doubleValue()
    .. py:method:: floatValue()
    .. py:method:: intValue()
    .. py:method:: longValue()
    .. py:method:: toByteArray()

        возвращает массив байтов объекта


    .. py:attribute:: ZERO
    .. py:attribute:: ONE
    .. py:attribute:: TEN


    .. py:method:: abs()

        возвращает объект, содержащий абсолютное значение числа, хранящегося в данном объекте this
    

    .. py:method:: add(x)

        операция сложения this + x


    .. py:method:: and(x)

        операция побитовой конъюнкции this & x


    .. py:method:: andNot(x)

        операция побитовой дизъюнкции с дополнением this & (~x)


    .. py:method:: divide(x)

        операция деления this / x


    .. py:method:: divideAndRemainder(x)

        возвращает массив из двух объектов класса BigInteger , содержащих частное и остаток от деления this на x


    .. py:method:: gcd(x)

        наибольший общий делитель абсолютных значений объекта this и аргумента x

    .. py:method:: max(x)

        наибольшее из значений объекта this и аргумента x


    .. py:method:: min(x)

        наименьшее из значений объекта this и аргумента x


    .. py:method:: mod(x)

        остаток от деления объекта this на аргумент метода x


    .. py:method:: modInverse(x)

        остаток от деления числа, обратного объекту this , на аргумент x

    
    .. py:method:: modPow(n, m)

        остаток от деления объекта this , возведенного в степень n , на m
    

    .. py:method:: multiply(x)

        операция умножения this * x


    .. py:method:: negate()

        перемена знака числа, хранящегося в объекте


    .. py:method:: not()

        операция отрицания ~this
    
    .. py:method:: or(x)

        операция побитовой дизъюнкции this | x


    .. py:method:: pow(n)

        операция возведения числа, хранящегося в объекте, в степень n


    .. py:method:: remainder(x)

        операция взятия остатка от деления this % x


    .. py:method:: shiftLeft(n)

        операция сдвига влево this << n


    .. py:method:: shiftRight(n)

        операция арифметического сдвига вправо this >> n


    .. py:method:: signum()

        функция sign(x)


    .. py:method:: subtract(x)

        операция вычитания this — x


    .. py:method:: xor(x)

        операция "исключающее ИЛИ" this ^ x