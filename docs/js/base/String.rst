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


    .. py:method:: length

        .. code-block:: js

            'ilnurgi'.length;
            // 7        


    .. py:method:: charAt(index)

        Возвращает символ по индексу

        .. code-block:: js

            'ilnurgi'.charAt(2);
            // 'n'

            'ilnurgi'.charAt(200);
            // ''

            'ilnurgi'.charAt(-1);
            // ''


    .. py:method:: charCodeAt(index)

        Возвращает число, код символа из строки

        .. code-block:: js

            '!'.charCodeAt(0);
            // 33


    .. py:method:: codePointAt(index)

        Возвращает неотрицательное целое число - кодовый пнкт символа.

        .. note:: EcmaScript6

        .. code-block:: js

            '\uD83D\uDE91'.codePointAt(1);
            // 56977

            '\u{1F691}'.codePointAt(1);
            // 56977

            'hello'.codePointAt(2);
            // 1080


    .. py:method:: concat(string..)

        Возвращает новую строку, соединенную с указанными

        .. code-block:: js

            "C".concat("a", "t");
            // "Cat"


    .. py:method:: endsWith(string, index)

        Проверяет, заканчивается ли строка на указанную

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".endsWith("il");
            // false


    .. py:method:: fromCharCode(char...)

        Статический метод, возвращает строку из последовательности чисел

        .. code-block:: js

            String.fromCharCode(33);
            // '!'

            String.fromCharCode(104, 101, 108, 108, 111);
            // "hello"


    .. py:method:: fromCodePoint(number1, ...)

        Возвращает строку по кодовым пунктам

        .. note:: EcmaScript6

        .. code-block:: js

            String.fromCodePoint(0x61, 0x62, 0x63);
            // 'abc'


    .. py:method:: includes(string, index=0)

        Проверяет наличие подстроки в строке

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".includes('il');
            // true


    .. py:method:: indexOf(searchString, [start_pos])

        Возвращает число, индекс вхождения подстроки в строку.

        Возвращает -1 если не найдено

        .. code-block:: js

            'строка'.indexOf("ока");
            // 3


    .. py:method:: lastIndexOf(searchString, [start_pos])

        Возвращает число, индекс вхождения подстроки в строку с конца

        .. code-block:: js

            'строка'.lastIndexOf("ока");
            // 3


    .. py:method:: localeCompare(str)

        Сравнивает строки с учетом порядка следования символов национальных алфавитов

        Возвращает 0 если строки равны
        Возвращает отрицательное число если аргумент меньше


    .. py:method:: match(regexp)

        Возвращает массив найденных вхождений по регулярке

        .. code-block:: js

            "kj5k3".match(/\d/);
            // ["5"]

            "kj5k3".match(/\d/g);
            // ["5", "3"]


    .. py:method:: normalize()

        Возвращает нормализованную строку, по умолчанию NFC.

        .. note:: Нормализованная версия не используется для отображение, только для различных операции: сравнение и т.п.

        .. note:: EcmaScript6


    .. py:method:: repeat(count)

        Возвращает строку, содержащую указанное количество копии

        .. note:: EcmaScript6

        .. code-block:: js

            "a".repeat(5);
            // "aaaaa"


    .. py:method:: replace(searchValue, replaceValue)

        Возвращает новую строку, заменяя в исходной указанные значения

        .. code-block:: js

            "mother_in_low".replace("_", "-");
            // "mother-in-low"

            "mother_in_low".replace("_", function(c){});

            "(777)888-2323".replace(/\((\d{3})\)/g, "$1-");
            // "111-888-2323"


    .. py:method:: search(regexp)

        Возвращает число, позицию первого символа соответсвия

        В отличие от :py:meth:`String.indexOf`
        работает только с регулярными выражениями


    .. py:method:: slice(start, [end])

        Возвращает срез строки

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'

            'stringify'.substring(3);
            // 'ingify'

            'stringify'.substring(-5);
            // 'ngify'


    .. py:method:: split(separator, limit)

        Возаращает массив строк, полученная путем разбиения исходной

        .. code-block:: js

            "12345".split("", 3);
            // ["1", "2", "3"]

            "last, first ,middle".split(/\s*,\s*/);
            // ["last", "first", "middle"]


    .. py:method:: startsWith(string, index=0)

        Проверяет, начинается ли строка с указанной строки

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".startsWith("il");
            // true


    .. py:method:: substr(start[, length])

        Срез строки с позиции `start`, количество `length` символов

        .. code-block:: js

            'stringify'.substr(2, 4);
            // 'ring'


    .. py:method:: substring(start[, end])

        Возвращает срез строки

        В отличие от :py:meth:`String.slice`
        отрицательные значение приравниваются к нулю.

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'

            'stringify'.substring(2);
            // 'ringify'


    .. py:method:: toLocalLowerCase()

        Возвращает строку, приведенную к нижнему регистру в соответсвйи с локалью


    .. py:method:: toLocalUpperCase()

        Возвращает строку, приведенную к верхнему регистру в соответсвйи с локалью


    .. py:method:: toLowerCase()

        Возвращает строку, приведенную к нижнему регистру


    .. py:method:: toUpperCase()

        Возвращает строку, приведенную к верхнему регистру


    .. py:method:: trim()

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
