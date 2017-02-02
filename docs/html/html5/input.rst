.. _input:

input
=====

Поле ввода информации


autocomplete
------------

Автозавершение

.. code-block:: html

    <input type="text" autocomplete="off" />


disabled
--------

Отключает элемент формы

Данные элемента не уйдут с запросом

.. code-block:: html

    <input type="time" disabled />


form
----

Идентификатор формы, на которую ссылается элемент

.. code-block:: html

    <form id="form1"></form>
    <input type="text" form="form1" />


maxlength
---------

Максимальная длина значения элемента

Применяется для text, password, url, search, telephone, email


min, max
--------

Диапазон допустимых значений для дат, number и range.

.. code-block:: html

    <input type="time" min="17:00" max="22:00" />


pattern
-------

Регулярка для валидации

.. code-block:: html

    <input
        type="color"
        pattern="#[0-9A-Fa-f]{6}"
        placeholder="#ffffff"
        title="color" />

    <input
        type="text"
        pattern="[0-9]{13,16}"
        title="13 или 16 цифр кредитки"
        placeholder="номер карты" />


placeholder
-----------

Подсказка

.. code-block:: html

    <input type="time" placeholder="подсказка" />


readonly
--------

Элемент доступен только для чтения

.. code-block:: html

    <input type="text" value="Not Editable" readonly />


required
--------

Помечает поле как обязательное

Не используется для buttons, range, color, hidden

.. code-block:: html

    <input type="email" required />


step
----

Шаг для полей дат, number, range

.. code-block:: html

    <input type="number" step="5" />

type
----

Тип поля

* button - кнопка, ничего не делает, используется для навешивания различных обработчиков

    .. code-block:: html

        <input type="button" value="кнопка" />

* checkbox - флажок

    .. code-block:: html

        <input type="checkbox" name="remember" value="true" />

* colour - поле выбора цвета

    .. code-block:: html

        <input
            name="clr"
            type="color"
            placeholder="#0 00000"
            pattern="#[0-9A-Fa-f]{6}"
            required />

* date - поле ввода даты

    .. code-block:: html

        <input
            name="date"
            type="date"
            placeholder="YYYY-MM-DD"
            min="1900-01-01"
            required />

* datetime - поле ввода даты со временем в системе utc

    .. code-block:: html

        <input
            name="datetime"
            type="datetime"
            placeholder="YYYY-MM-DD"
            min="2010-01-01T00:00Z"
            max="2011-12-31T23:59Z"
            required />

* datetime-local - поле ввода даты со временем

* email - поле ввода электронной почты

    Доступные атрибуты

    * autocomplete
    * autofocus
    * disabled
    * form
    * list
    * maxlength
    * multiple - несколько значений через запятые
    * name
    * pattern
    * placeholder
    * readonly
    * required
    * size

    .. code-block:: html

        <input type="email" name="email" />

* file - поле для закачки файла

    Доступные атрибуты:

        * accept - список допустимых файлов
        * autofocus
        * capture
        * disabled
        * multiple
        * name
        * required

    .. code-block:: html

        <input type="file" name="image" accept="image/*" capture />
        <input type="file" name="video" accept="video/*" capture />
        <input type="file" name="audio" accept="audio/*" capture />

* hidden - скрытое поле

    .. code-block:: html

        <input type="hidden" name="user_id" value="1" />

* image -

* month - поле ввода месяца с годом

    .. code-block:: html

        <input
            name="month"
            type="month"
            placeholder="YYYY-MM"
            min="2010-01"
            max="2020-01"
            step="6"
            required />

* number - поле ввода числовых данных

    .. code-block:: html

        <input type="number" min="0" step="5">
        <input
            type="number" p
            laceholder="100 to 999"
            pattern="[1-9][0-9]{2}"
            min="100"
            max="999"
            required />

* password - пароль

    .. code-block:: html

        <input type="password" name="password" id="password" />

* radio - переключатель

    .. code-block:: html

        <input type="radio" name="color" value="red" />
        <input type="radio" name="color" value="green" />

* range - ползунок

* reset - кнопка сброса

    .. code-block:: html

        <input type="reset" value="Очистить эту форму" />

* search - поле поиска

* submit - кнопка отправки

    .. code-block:: html

        <input type="submit" value="Отправить эту форму" />

* tel - используется для ввода телефонного номера.

    .. code-block:: html

        <input
            type="tel"
            placeholder="XXX-XXX-XXXX"
            pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
            required />

* text - обычное текстовое поле

    * autocomplete
    * autofocus
    * disabled
    * form
    * list - идентификатор на список возможных значений, :ref:`datalist`
    * maxlength
    * name
    * pattern
    * placeholder
    * readonly
    * required
    * size



    .. code-block:: html

        <input type="text" name="username" id="username" />

* time - поле ввода времени

    .. code-block:: html

        <input
            type="time"
            min="09:00"
            max="17:00"
            name="time"
            step="900"
            placeholder="12:00"
            required />

* url - поле ввода веб адреса

    .. code-block:: html

        <input
            type="url"
            pattern="^(http|https|ftp)\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]*"
            placeholder="http://www.domain.com"
            required />

* week - поле ввода номера недели

    .. code-block:: html

        <input
            type="week"
            name="week"
            min="2010-W01"
            max="2020-W02"
            required />

value
-----

Значение поля