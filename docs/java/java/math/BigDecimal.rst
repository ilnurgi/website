BigDecimal
==========

.. py:class:: BigDecimal()

    Каждый объект этого класса хранит два целочисленных значения: мантиссу вещественного числа в виде объекта класса BigInteger и неотрицательный десятичный порядок числа типа int . Например, для числа 76,34862 будет храниться мантисса 7 634 862 в объекте класса BigInteger и порядок 5 как целое число типа int . Таким образом, мантисса может содержать любое количество цифр, а порядок ограничен значением константы Integer.MAX_VALUE .

    
    .. py:method:: BigDecimal(BigInteger bi)

        объект будет хранить большое целое bi , порядок равен нулю


    .. py:method:: BigDecimal(BigInteger mantissa, int scale)

        задается мантисса mantissa и неотрицательный порядок scale объекта; если порядок scale отрицателен, возникает исключительная ситуация


    .. py:method:: BigDecimal(double d)

        объект будет содержать вещественное число удвоенной точности d ; если значение d бесконечно или NaN , то возникает исключительная ситуация;


    .. py:method:: BigDecimal(String val)

        число задается строкой символов val , которая должна содержать запись числа по правилам языка Java.


    .. py:method:: doubleValue()
    .. py:method:: floatValue()
    .. py:method:: intValue()
    .. py:method:: longValue()

    .. py:method:: abs()

        абсолютное значение объекта this


    .. py:method:: add(BigDecimal x)

        операция сложения this + x


    .. py:method:: divide(BigDecimal x, r)

        операция деления this / x с округлением по способу r


    .. py:method:: divide(BigDecimal x, Integer n, r)

        операция деления this / x с изменением порядка и округлением по способу r


    .. py:method:: max(BigDecimal x)

        наибольшее из this и x ;


    .. py:method:: min(BigDecimal x)

        наименьшее из this и x


    .. py:method:: movePointLeft(Integer n)

        сдвиг влево на n разрядов


    .. py:method:: movePointRight(Integer n)

        сдвиг вправо на n разрядов


    .. py:method:: multiply(BigDecimal x)

        операция умножения this * x


    .. py:method:: negate()

        возвращает объект с обратным знаком
    

    .. py:method:: scale()

        возвращает порядок числа


    .. py:method:: setScale(Integer n)

        устанавливает новый порядок n


    .. py:method:: setScale(Integer n, r)

        устанавливает новый порядок n и округляет число при необходимости по способу r


    .. py:method:: signum()

        знак числа, хранящегося в объекте


    .. py:method:: subtract(BigDecimal x)

        операция вычитания this — x


    .. py:method:: toBigInteger()

        округление числа, хранящегося в объекте


    .. py:method:: unscaledValue()

        возвращает мантиссу числа


    .. py:method:: upl()

        возвращает расстояние до следующего числа


    .. py:attribute:: ROUND_CEILING

        округление в сторону большего целого
    
    
    .. py:attribute:: ROUND_DOWN

        округление к нулю, к меньшему по модулю целому значению


    .. py:attribute:: ROUND_FLOOR

        округление к меньшему целому


    .. py:attribute:: ROUND_HALF_DOWN

        округление к ближайшему целому, среднее значение округляется к меньшему целому


    .. py:attribute:: ROUND_HALF_EVEN

        округление к ближайшему целому, среднее значение округляется к четному числу


    .. py:attribute:: ROUND_HALF_UP

        округление к ближайшему целому, среднее значение округляется к большему целому


    .. py:attribute:: ROUND_UNNECESSARY

        предполагается, что результат будет целым, и округление не понадобится


    .. py:attribute:: ROUND_UP

        округление от нуля, к большему по модулю целому значению

    
    .. py:attribute:: ZERO
    .. py:attribute:: ONE
    .. py:attribute:: TEN

        моделируют вещественные нуль, единицу и вещественное число десять в операциях с объектами класса BigDecimal .