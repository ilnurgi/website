String - строки
===============

.. py:class:: String()
    
    Строки

    Наследник :py:class:`Object`


    .. code-block:: js

        a = new String('test');
        string = 'ilnurgi';
        s += 's';

        'ilnurgi' + 123;
        // 'ilnurgi123'

        '12'/2 + 1;
        // 7

        'day' * 2;
        // NaN

        'a' < 'b';
        // true

        'c' < 'b';
        // false

        'bra' / 2;
        // NaN


    .. py:function:: length

        .. code-block:: js

            'ilnurgi'.length;
            // 7        


    .. py:function:: charAt(index)

        Символ из строки по индексу

        .. code-block:: js

            'ilnurgi'.charAt(2);
            // 'n'

            'ilnurgi'.charAt(200);
            // ''

            'ilnurgi'.charAt(-1);
            // ''


    .. py:function:: charCodeAt(index)

        Код символа из строки

        .. code-block:: js

            '!'.charCodeAt(0);
            // 33


    .. py:function:: codePointAt(index)

        Возвращает неотрицательное целое число - кодовый пнкт символа.

        .. note:: EcmaScript6

        .. code-block:: js

            '\uD83D\uDE91'.codePointAt(1);
            // 56977

            '\u{1F691}'.codePointAt(1);
            // 56977

            'hello'.codePointAt(2);
            // 1080


    .. py:function:: concat(index)

        Конкатенация одного или нескольких значений со строкой


    .. py:function:: endsWith(string, index)

        Проверяет, заканчивается ли строка на указанную

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".endsWith("il");
            // false


    .. py:function:: fromCharCode(code)

        Статический метод, возвращает символ по коду

        .. code-block:: js

            String.fromCharCode(33);
            // '!'

            String.fromCharCode(104, 101, 108, 108, 111);
            // "hello"


    .. py:function:: fromCodePoint(number1, ...)

        Возвращает строку по кодовым пунктам

        .. note:: EcmaScript6

        .. code-block:: js

            String.fromCodePoint(0x61, 0x62, 0x63);
            // 'abc'


    .. py:function:: includes(string, index=0)

        Проверяет наличие подстроки в строке

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".includes('il');
            // true


    .. py:function:: indexOf(substr, [start_pos])

        Возвращает индекс вхождения подстроки в строку.

        .. code-block:: js

            'строка'.indexOf("ока");
            // 3


    .. py:function:: lastIndexOf(substr, [start_pos])

        Возвращает индекс вхождения подстроки в строку с конца.

        .. code-block:: js

            'строка'.lastIndexOf("ока");
            // 3


    .. py:function:: localeCompare(str)

        Сравнивает строки с учетом порядка следования символов национальных алфавитов


    .. py:function:: match(str)

        Поиск совпадений в строке, возвращает массив


    .. py:function:: normalize()

        Возвращает нормализованную строку, по умолчанию NFC.

        .. note:: Нормализованная версия не используется для отображение, только для различных операции: сравнение и т.п.

        .. note:: EcmaScript6


    .. py:function:: repeat(count)

        Возвращает строку, содержащую указанное количество копии

        .. note:: EcmaScript6

        .. code-block:: js

            "a".repeat(5);
            // "aaaaa"


    .. py:function:: replace(str1, str2)

        Поиск и замена


    .. py:function:: search(str)

        Поиск совпадений в строке, возвращает индекс


    .. py:function:: slice(start, [end])

        Срез строки с позиции `start` до позиции `end`, не включая его.

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'


    .. py:function:: split(разделитель, лимит)

        Разбиение строки на массив


    .. py:function:: startsWith(string, index=0)

        Проверяет, начинается ли строка с указанной строки

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".startsWith("il");
            // true


    .. py:function:: substr(start[, length])

        Срез строки с позиции `start`, количество `length` символов

        .. code-block:: js

            'stringify'.substr(2, 4);
            // 'ring'


    .. py:function:: substring(start[, end])

        Срез строки с позиции `start` до позиции `end`, не включая его.

        Отрицательные значение приравниваются к нулю.

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'

            'stringify'.substring(2);
            // 'ringify'


    .. py:function:: toLowerCase()

        Преобразует строку в нижний регистр


    .. py:function:: toUpperCase()

        Преобразует строку в верхний регистр


    .. py:function:: trim()

        Возвращает копию строки, с удаленными пробелами вначале и в конце


Интерполяция
------------

.. code-block:: js

    var str = "My first name is " + "ilnur" + " and last name " + "ilnur" + "gii"

.. note:: EcmaScript6

    .. code-block:: js

        let name = "ilnur";
        let last_nme = "gii";
        let str = `My first name is ${name} and last name ${name + last_name}`


Многострочные строки
--------------------

.. code-block:: js

    var multiline_str = "1\n2";

.. note:: EcmaScript6

    .. code-block:: js

        let multiline_str = `1
        2`;
