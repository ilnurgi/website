Date - объект дата
==================

.. py:class:: Date()

    Дата

    .. code-block:: js

        var g = new Date();
        var g = new Date(year, month, date, hours, minutes, seconds, ms);
        var g = new Date(2013, 1, 1);
        var g = new Date(5000);
        var g = new Date('2013-01-01');
        var g = new Date('December 25, 2013 21:46:10');
        var g = new Date('03/09/2000');


    .. py:function:: getDate(), getUTCDate()

        Возвращает число месяца


    .. py:function:: getDay(), getUTCDay()

        Возвращает число, номер дня недели


    .. py:function:: getFullYear(), getUTCFullYear()

        Возвращает текущий год, 2013


    .. py:function:: getHours(), getUTCHours()

        Возвращает число, часы


    .. py:function:: getMilliseconds(), getUTCMilliseconds()

        Возвращает число, миллисекунды


    .. py:function:: getMinutes(), getUTCMinutes()

        Возвращает число, минуты


    .. py:function:: getMonth(), getUTCMonth()

        Возвращает чилсо месяца


    .. py:function:: getSeconds(), getUTCSeconds()

        Возвращает число, секунды


    .. py:function:: getTime()

        Возвращает число, количество секунд прошедшее с 1970.1.1


    .. py:function:: getTimezoneOffset()

        Возвращает смещение даты в минутах.


    .. py:function:: getYear()

        Возвращает число, количесвто лет прошедшее с 1970.1.1


    .. py:function:: now()

        Статический метод, который возвращает текущее время в секундах

        .. versionadded:: ECMAScript5


    .. py:function:: parse()

        Статический метод, который парсит строку с датой и возвращает объект :py:class:`Date`


    .. py:function:: setDate(date), setUTCDate(date)

        Задаем новое число месяца


    .. py:function:: setFullYear(year[, month[, date]]), setUTCFullYear(year[, month[, date]])

        Задаем новый год


    .. py:function:: setHours(hours[, minute[, seconds[, millisec]]]), setUTCHours(hours[, minute[, seconds[, millisec]]])

        Задаем новые часы даты


    .. py:function:: setMilliseconds(ms), setUTCMilliseconds(ms)

        Задаем миллисекунды


    .. py:function:: setMinutes(minutesp, sec[, millisec]), setUTCMinutes(minutesp, sec[, millisec])

        Задаем новые минуты даты


    .. py:function:: setMonth(month[, day]), setUTCMonth(month[, day])

        Задаем новый месяц


    .. py:function:: setSeconds(seconds[, millisec]), setUTCSeconds(seconds[, millisec])

        Задаем новые секунды даты


    .. py:function:: setTime(ms)

        Устанавливаем новую дату, время в секндах с 1.1.1970


    .. py:function:: setYear(year)

        Устанавливаем новую год
        

    .. py:function:: toDateString()

        Возвращает строковое представление даты
        

    .. py:function:: toISOString()

        Возвращает строковое представление даты, в формате ISO8601 (yyyy-mm-ddThh:mm:ss.sssZ)  


    .. py:function:: toFSON()

        Возвращает JSON представление даты


    .. py:function:: toLocaleDateString()

        Возвращает дату с учетом региональных настроек


    .. py:function:: toLocaleString()

        Возвращает строковое представление даты с учетом региональных настроек


    .. py:function:: toLocaleTimeString()

        Возвращает строковое представление времени с учетом региональных настроек


    .. py:function:: toTimeString()

        Возвращает строковое представление времени


    .. py:function:: toUTCString()

        Возвращает строковое представление универсального времени


    .. py:function:: UTC(год, ме­сяц, день, ча­сы, ми­ну­ты, се­кун­ды, мс)

        Статический метод, который возвращает представление указанной даты и времени UTC в миллисекундах