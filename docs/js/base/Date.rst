Date - объект дата
==================

.. js:class:: Date()

    Дата

    .. code-block:: js

        var g = new Date();
        var g = new Date(year, month, date, hours, minutes, seconds, ms);
        var g = new Date(2013, 1, 1);
        var g = new Date(5000);
        var g = new Date('2013-01-01');
        var g = new Date('December 25, 2013 21:46:10');
        var g = new Date('03/09/2000');


    .. js:function:: getDate(), getUTCDate()

        Возвращает число месяца


    .. js:function:: getDay(), getUTCDay()

        Возвращает число, номер дня недели


    .. js:function:: getFullYear(), getUTCFullYear()

        Возвращает текущий год, 2013


    .. js:function:: getHours(), getUTCHours()

        Возвращает число, часы


    .. js:function:: getMilliseconds(), getUTCMilliseconds()

        Возвращает число, миллисекунды


    .. js:function:: getMinutes(), getUTCMinutes()

        Возвращает число, минуты


    .. js:function:: getMonth(), getUTCMonth()

        Возвращает чилсо месяца


    .. js:function:: getSeconds(), getUTCSeconds()

        Возвращает число, секунды


    .. js:function:: getTime()

        Возвращает число, количество секунд прошедшее с 1970.1.1


    .. js:function:: getTimezoneOffset()

        Возвращает смещение даты в минутах.


    .. js:function:: getYear()

        Возвращает число, количесвто лет прошедшее с 1970.1.1


    .. js:function:: now()

        Статический метод, который возвращает текущее время в секундах

        .. versionadded:: ECMAScript5


    .. js:function:: parse()

        Статический метод, который парсит строку с датой и возвращает объект :js:class:`Date`


    .. js:function:: setDate(date), setUTCDate(date)

        Задаем новое число месяца


    .. js:function:: setFullYear(year[, month[, date]]), setUTCFullYear(year[, month[, date]])

        Задаем новый год


    .. js:function:: setHours(hours[, minute[, seconds[, millisec]]]), setUTCHours(hours[, minute[, seconds[, millisec]]])

        Задаем новые часы даты


    .. js:function:: setMilliseconds(ms), setUTCMilliseconds(ms)

        Задаем миллисекунды


    .. js:function:: setMinutes(minutesp, sec[, millisec]), setUTCMinutes(minutesp, sec[, millisec])

        Задаем новые минуты даты


    .. js:function:: setMonth(month[, day]), setUTCMonth(month[, day])

        Задаем новый месяц


    .. js:function:: setSeconds(seconds[, millisec]), setUTCSeconds(seconds[, millisec])

        Задаем новые секунды даты


    .. js:function:: setTime(ms)

        Устанавливаем новую дату, время в секндах с 1.1.1970


    .. js:function:: setYear(year)

        Устанавливаем новую год
        

    .. js:function:: toDateString()

        Возвращает строковое представление даты
        

    .. js:function:: toISOString()

        Возвращает строковое представление даты, в формате ISO8601 (yyyy-mm-ddThh:mm:ss.sssZ)  


    .. js:function:: toFSON()

        Возвращает JSON представление даты


    .. js:function:: toLocaleDateString()

        Возвращает дату с учетом региональных настроек


    .. js:function:: toLocaleString()

        Возвращает строковое представление даты с учетом региональных настроек


    .. js:function:: toLocaleTimeString()

        Возвращает строковое представление времени с учетом региональных настроек


    .. js:function:: toTimeString()

        Возвращает строковое представление времени


    .. js:function:: toUTCString()

        Возвращает строковое представление универсального времени


    .. js:function:: UTC(год, ме­сяц, день, ча­сы, ми­ну­ты, се­кун­ды, мс)

        Статический метод, который возвращает представление указанной даты и времени UTC в миллисекундах