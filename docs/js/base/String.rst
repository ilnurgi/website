String - строки
===============

.. js:class:: String()
    
    Строки

    Наследник :js:class:`Object`


    .. code-block:: js

        var a = new String('test'),
            string = 'ilnurgi',
            s += 's';

        // в переменную а мы можем добавить свои атрибуты и методы

        '\u1552'.length
        //1

        'il\'s'.length
        //3

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


    .. js:function:: length

        .. code-block:: js

            'ilnurgi'.length;
            // 7        


    .. js:function:: charAt(index)

        Символ из строки

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

        Статический метод, возвращает новую строку

        .. code-block:: js

            String.fromCharCode(33); // '!'
            String.fromCharCode(104, 101, 108, 108, 111); // "hello"


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

        Поиск совпадений в строке, возвращает индекс


    .. js:function:: split(разделитель, лимит)

        Разбиение строки на массив


    .. js:function:: substr(start[, length])

        Срез строки


    .. js:function:: substring(start[, length])

        Срез строки


    .. js:function:: toLowerCase()

        Преобразует строку в нижний регистр


    .. js:function:: toUpperCase()

        Преобразует строку в верхний регистр


    .. js:function:: trim()

        Возвращает копию строки, с удаленными пробелами вначале и в конце