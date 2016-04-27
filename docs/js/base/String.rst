String - строки
===============

.. js:class:: String()
    
    Строки

    Наследник :js:class:`Object`


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


    .. js:function:: length

        .. code-block:: js

            'ilnurgi'.length;
            // 7        


    .. js:function:: charAt(index)

        Символ из строки по индексу

        .. code-block:: js

            'ilnurgi'.charAt(2);
            // 'n'

            'ilnurgi'.charAt(200);
            // ''

            'ilnurgi'.charAt(-1);
            // ''


    .. js:function:: charCodeAt(index)

        Код символа из строки

        .. code-block:: js

            '!'.charCodeAt(0);
            // 33


    .. js:function:: concat(index)

        Конкатенация одного или нескольких значений со строкой


    .. js:function:: fromCharCode(code)

        Статический метод, возвращает символ по коду

        .. code-block:: js

            String.fromCharCode(33);
            // '!'

            String.fromCharCode(104, 101, 108, 108, 111);
            // "hello"


    .. js:function:: indexOf(substr, [start_pos])

        Возвращает индекс вхождения подстроки в строку.

        .. code-block:: js

            'строка'.indexOf("ока");
            // 3


    .. js:function:: lastIndexOf(substr, [start_pos])

        Возвращает индекс вхождения подстроки в строку с конца.

        .. code-block:: js

            'строка'.lastIndexOf("ока");
            // 3


    .. js:function:: localeCompare(str)

        Сравнивает строки с учетом порядка следования символов национальных алфавитов


    .. js:function:: match(str)

        Поиск совпадений в строке, возвращает массив


    .. js:function:: replace(str1, str2)

        Поиск и замена


    .. js:function:: search(str)

        Поиск совпадений в строке, возвращает индекс


    .. js:function:: slice(start, [end])

        Срез строки с позиции `start` до позиции `end`, не включая его.

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'


    .. js:function:: split(разделитель, лимит)

        Разбиение строки на массив


    .. js:function:: substr(start[, length])

        Срез строки с позиции `start`, количество `length` символов

        .. code-block:: js

            'stringify'.substr(2, 4);
            // 'ring'


    .. js:function:: substring(start[, end])

        Срез строки с позиции `start` до позиции `end`, не включая его.

        Отрицательные значение приравниваются к нулю.

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'

            'stringify'.substring(2);
            // 'ringify'


    .. js:function:: toLowerCase()

        Преобразует строку в нижний регистр


    .. js:function:: toUpperCase()

        Преобразует строку в верхний регистр


    .. js:function:: trim()

        Возвращает копию строки, с удаленными пробелами вначале и в конце