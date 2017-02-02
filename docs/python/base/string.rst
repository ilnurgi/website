Строки
======

str
---

.. py:class:: str([obj, encode, errors='strict'])

    Возвращает :py:class:`str`, преобразованный из объекта

    Через атрибут `errors` настраивается обработка ошибок:

        * `strict` - при ошибке возбуждается исключение :py:class:`UnicodeDecodeError`

        * `replace` - неизвестный символ заменяется символом, имеющим код \uFFFD

        * `ignore` - неизвестные символы игнорируются

    .. code-block:: py

        str()
        # ''

        str(125)
        # '125'

        str([1, 2, 3])
        # '[1, 2, 3]'

        str((1, 2, 3))
        # '(1, 2, 3)'

        str({"x": 5, "у": 10})
        # "{'у': 10, 'х': 5}"

        str(bytes("строка", "utf-8"))
        # "b'\\xd1\\x81\\xd1\\x82\\xd1\\x80\\xd0\\xbe\\xd0\\xba\\xd0\\хbО'"

        str(bytearray("строка", "utf-8") )
        # "bytearray(b'\\xd1\\x81\\xd1\\x82\\xd1\\x80\\xd0\\xbe\\xd0\\xba\\xdO\\xbO')"

        str(bytes("строка1", "utf-8"), "utf-8")
        # 'строка1'

        str(bytes("строка1", "utf-8"), "ascii", "strict")
        # Traceback (most recent са11 1ast):
        #   Fi1e "<pyshe11#16>", 1ine 1, in <modu1e>
        #     str(bytes("строка1", "utf-8"), "ascii", "strict")
        # UnicodeDecodeError: 'ascii' codec can't decode byte Oxd1 in position 0: ordina1 not in range(128)

        str(bytes("строка1", "utf-8"), "ascii", "ignore")
        # '1'

        # вернет строку не зависима от типа аргумента
        str(b"\xf1\xf2\xf0\xee\xea\xe0")
        "b'\\xf1\\xf2\\xf0\\xee\\xea\\xe0'"

        # вернет строку именно из типа bytes или bytearray
        str(b"\xf1\xf2\xf0\xee\xea\xe0", "ср1251")
        # 'строка'

    .. code-block:: py

        "однострочная строка"
        "однострочная \'строка\'"
        'однострочная строка'
        'однострочная \"строка\"'
        """многострочная строка"""
        '''многострочная строка'''

    .. code-block:: py

        'ilnurgi' + '.ru'
        # 'ilnurgi.ru'

        'ilnurgi' * 3
        #'ilnurgiilnurgiilnurgi'

        'il' in 'ilnurgi'
        # True

        'il' not in 'ilnurgi'
        # False

        'ilnurgi'[0]
        # 'i'

        'ilnurgi'[2]
        # 'n'

        'ilnurgi'[:2]
        # 'il'

        'ilnurgi'[-2:]
        # 'gi'


    .. py:staticmethod:: maketrans(x [, y [, z]])

        Создает и возвращает таблицу символов

        * Если указан только первый параметр, то он должен быть словарем:

            .. code-block:: py

                t = str.maketrans({"a": "А", "о": "О", "с": None})
                # t = {1072: 'А', 1089: None, 1086: 'О'}

                "cтpoкa".translate(t)
                # 'трОкА'

        * Если указаны два первых параметра, то они должны быть строками одинаковой длины:

            .. code-block:: py

                t = str.maketrans("абвгдежзи", "АБВГДЕЖЗИ")
                # t = {1072: 1040, 1073: 1041, ...}

                "aбвгдeжзи".translate(t)
                # 'АБВГДЕЖЗИ'

        * В третьем параметре можно дополнительно указать строку из символов,
          которым будет сопоставлено значение None:

            .. code-block:: py

                t = str.maketrans("123456789", "О" * 9, "str")
                # t = {116: None, 115: None, 114: None, 49: 48, ююю}

                "strl23456789str".translate(t)
                # '000000000'


    .. py:method:: capitalize()
    
        Возвращает новую строку, :py:class:`str`, у которой первая буква заменена на прописную
        
        .. code-block:: py

            'ilnur'.capitalize()
            # 'Ilnur'


    .. py:method:: center(width, [pad])

        Возвращает новую строку, :py:class:`str`, заданной длины, выравненная по центру.

        .. code-block:: py

            'ilnur'.center(7)
            # ' ilnur '


    .. py:method:: count(sub [, start [, end]])
        
        Возвращает :py:class:`int`, количество вхождений искомой строки в исходной строке.
        
        .. code-block:: py

            'Help me! Help!'.count('Help')
            # 2


    .. py:method:: decode([coding, errors])
        
        Возвращает новую юникодную строку, :py:class:`unicode`,
        раскодированная из указанной кодировки в юникод.
            
        .. code-block:: py

            '\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x83\xd1\x80'.decode('utf-8')
            # u'\u0438\u043b\u044c\u043d\u0443\u0440'


    .. py:method:: encode([coding, errors])
        
        Возвращает новую строку, :py:class:`str`,
        закодированную из юникода в указанную кодировку.
        
        .. code-block:: py

            u'Ильнур'.encode('cp1251')
            # '\xc8\xeb\xfc\xed\xf3\xf0'


    .. py:method:: endswith(sub[, start [, end]])
        
        Возвращает :py:class:`bool`, строка заканчивается c искомой строки

        .. code-block:: py

            'ilnur'.endswith('il')
            # False

            'ilnur'.endswith('nur')
            # True


    .. py:method:: expandtabs([tabsize=8])
        
        Возвращает новую строку, :py:class:`str`,
        символы табуляции заменены указанным количеством пробелов.
        
        .. code-block:: py

            u'\tИльнур'.expandtabs()
            # u'        \u0418\u043b\u044c\u043d\u0443\u0440'


    .. py:method:: find(sub[, start [, end]])
        
        Возвращает :py:class:`int`, позиция, в котором встречается искомая строка,
        если ничего не найдено возвращает -1, поиск ведется слева.
        
        .. code-block:: py

            'ilnur'.find('nur')
            # 2

            'ilnur'.find('run')
            # -1


    .. py:method:: format(*args, **kwargs)
        
        Возвращает новую строку, :py:class:`str`,
        форматированную в соответствии с переданными параметрами
        
        Синтаксис: `{[Поле][!Функция][:Формат]}`

        Синтаксис формата: `[[Заполнитель] Выравнивание] [Знак] [#] [0] [Ширна] [,] [.Точность] [Преобразование]`

            * `заполнитель` - заполнитель пространства в поле
            * `выравнивание` - выравниваение поля

                * `<` - по левому краю
                * `>` - по правому краю
                * `^` - по центру
                * '=' - знак числа по левому краю, число по правому

            * `ширина` - ширина поля

                .. code-block:: py

                    "'{0:10}'".format(3)
                    # '         3'

                    "'{0:{1}}'".format(3, 10)
                    # '         3'

            * `знак` - управляет выводом знака числа

                * `+` - обязательный вывод знаков
                * `-` - знаки только для отрицательных
                * `пробел` - вывод отрицательных знаков и пробел вместо положительного знака

            * `преобразование` - преобразование чисел

                * `b` - двоичное значение
                * `c` - преобразование числа в символ
                * `d` - десятичное значение
                * `n` - аналогично `d`, но с учетом локали
                * `o` - восьмиричное значение
                * `x`, 'X' - шестнадцатиричное значение 
                * `f`, `F` - вещественное число в десятичном представлении
                * `e`, `E` - вещественное число в экспоненциальной форме
                * `g`, `G` - эквивалентно `f`, `e` или `E` (выбирается более короткая запись числа)
                * `n` - аналогично `g`, но учитвает локаль
                * `%` - умножает число на 100 и добавляет символ процента в конце
                * `` - 
                * `` - 
                * `` - 
                * `` - 

        .. code-block:: py

            '{0} и {1}'.format('фарш', 'яйца')
            # 'фарш и яйца'

            'Этот {food} — {adjective}.'.format(food='фарш', adjective='непередаваемо ужасен')
            # Этот фарш — непередаваемо ужасен.

            'История о {0}е, {1}е, и {other}е.'.format('Билл', 'Манфред', other='Георг')
            # История о Билле, Манфреде, и Георге.

            'Значение ПИ — примерно {0:.3f}.'.format(3.14))
            # Значение ПИ — примерно 3.14159.

            '{0:10} ==> {1:10d}'.format('Sjoerd', 4127)
            # Sjoerd     ==>       4127

            table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
            'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
            # Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

            # вывод в двоичном формате
            '{0:b} & {1:b} = {2:b}'.format(100, 75, 100 & 75)
            # '1100100 & 1001011 = 1000000'


    .. py:method:: index(sub [, start [, end]])
        
        Возвращает :py:class:`int`, позиция, в котором встречается искомая строка,
        если ничего не найдено вызовет исключение :py:class:`ValueError`,
        поиск ведется слева.
        
        .. code-block:: py

            'ilnur'.index('nur')
            # 2

            'ilnur'.index('run')
            """
            Traceback (most recent call last):
                File "<stdin>", line 1, in <module>
            ValueError: substring not found
            """


    .. py:method:: isalpha()
        
        Возвращает :py:class:`bool`, строка содержит только буквы
        
        .. code-block:: py

            '123'.isalpha()
            # False

            'ilnur'.isalpha()
            # True


    .. py:method:: isalnum()
        
        Возвращает :py:class:`bool`, строка содержит только буквы и цифры
        

    .. py:method:: isdigit()
        
        Возвращает :py:class:`bool`, строка содержит только цифры
        
        .. code-block:: py

            '123'.isdigit()
            # True

            'ilnur'.isdigit()
            # False
        

    .. py:method:: isdecimal()
        
        Возвращает :py:class:`bool`, строка содержит только десятичные символы
        

    .. py:method:: islower()

        Возвращает :py:class:`bool`, строка содержит только строчные буквы
        

    .. py:method:: isnumeric()
        
        Возвращает :py:class:`bool`, строка содержит только числовые символы

        .. code-block:: py

            "\u2155".isnumeric()
            # True

            "\u2155".isdigit()
            # False

            print("\u2155")
            # '1/5'


    .. py:method:: isspace()
        
        Возвращает :py:class:`bool`, строка содержит только пробельные символы

        .. code-block:: py

            '123'.isalpha()
            # False


    .. py:method:: istitle()

        Возвращает :py:class:`bool`, строка содержит слова начинающиеся с заглавной буквы


    .. py:method:: isupper()

        Возвращает :py:class:`bool`, если строка содержит только заглавные буквы


    .. py:method:: join(iter)

        Возвращает строку :py:class:`str`,
        содержащий сконкатенированные значения исходной строки с итерируемым объектом.

        .. code-block:: py

            'ilnur'.join('---')
            # '-ilnur-ilnur-


    .. py:method:: ljust(width, [fill])

        Возвращает новую строку :py:class:`str`, заданной длины, выравненная слева.

        .. code-block:: py

            'ilnur'.ljust(7)
            # 'ilnur  '


    .. py:method:: lower()
        
        Возвращает новую строку :py:class:`str`, в нижнем регистре
        
        .. code-block:: py

            'iLnur'.lower()
            'ilnur'


    .. py:method:: lstrip([chrs=" "])
        
        Возвращает новую строку :py:class:`str`, с удаленными пробелами слева

        .. code-block:: py

            ' ilnur privet '.lstrip()
            # 'ilnur privet  '


    .. py:method:: partition(sep)

        Находит первое вхождение символа-разделителя в строку и возвращает кортеж из трех элементов.

            * первый элемент - содержать фрагмент, расположенный перед разделителем
            * второй элемент - символ-разделитель
            * третий эле­мент - фрагмент, расположенный после символа-разделителя.

        Поиск производится сле­ва направо.

        Если символ-разделитель не найден,
        то первый элемент кортежа будет со­держать всю строку,
        а остальные элементы будут пустыми.

        .. code-block:: py

            "wordl word2 wordЗ".partition(" ")
            # ('wordl', ' ', 'word2 word3')
        
            "wordl word2 wordЗ".partition("\n")
            # ('wordl word2 wordЗ', '', '')


    .. py:method:: replace(old, new, [maxreplace])

        Возвращает новую строку :py:class:`str`, с замененой строкой на новую строку.

        .. code-block:: py

            'ilnur'.replace('nur','nurgi')
            # 'ilnurgi'


    .. py:method:: rfind(sub [, start [, end]])

        Возвращает :py:class:`int`, позиция с которого начинается искомая строка,
        если ничего не найдено возвращает -1, поиск ведется справа.

        Аналог :py:meth:`find`.


    .. py:method:: rindex(sub [, start [, end]])

        Возвращает :py:class:`int`, позиция с которого начинается искомая строка,
        если ничего не найдено вызовет исключение :py:class:`ValueError`,
        поиск ведется справа.

        Аналог :py:meth:`index`.



    .. py:method:: rjust(width, [fill])

        Возвращает новую строку :py:class:`str`, заданной длины, выравненная по правому краю.

        .. code-block:: py

            'ilnur'.rjust(7)
            # '  ilnur'


    .. py:method:: rpartition(sep)

        Аналогично методу :py:meth:`str.partition`,
        но поиск символа­ разделителя производится не слева направо,
        а, справа налево.

        Если символ­ разделитель не найден,
        то первые два элемента кортежа будут пустыми,
        а третий эле­мент будет содержать всю строку.

        .. code-block:: py

            "wordl word2 wordЗ".rpartition(" ")
            # ('wordl word2', ' ', 'wordЗ')

            "wordl word2 wordЗ".rpartition("\n")
            # (' ', '', 'wordl word2 word3')


    .. py:method:: rsplit([razd, maxcount])

        Возвращает :py:class:`list`, полученный из строки, путем разделения разделителем.

        .. code-block:: py

            'i l n u r'.split(' ')
            # ['i', 'l', 'n', 'u', 'r']


    .. py:method:: rstrip([chrs=" "])
        
        Возвращает новую строку :py:class:`str`,
        с удаленными пробелами справа
       
        .. code-block:: py

            ' ilnur privet '.rstrip()
            # ' ilnur privet'


    .. py:method:: split([sep [, maxcount]])

        Возвращает :py:class:`list`, полученный из строки, путем разделения разделителем.

        .. code-block:: py

            'i l n u r'.split(' ')
            # ['i', 'l', 'n', 'u', 'r']


    .. py:method:: splitlines([keepends=1])
        
        Возвращает :py:class:`list`, аналогично :py:meth:`split`,
        но использующий в качестве разделителя переход на новую строку.

        Символы перехода на новую строку включаются в результат,
        только если необязательный аргумент keepends равен 1.

        .. code-block:: py

            """Hello World!\nHello!""".splitlines()
            # ['Hello World!', 'Hello!']


    .. py:method:: startswith(sub[, start [, end]])
        
        Возвращает :py:class:`bool`, если строка начинается c искомой строки

        .. code-block:: py

            'ilnur'.startswith('il')
            # True

            'ilnur'.startswith('nur')
            # False


    .. py:method:: strip([chrs=" "])

        Возвращает новую строку :py:class:`str`,
        с удаленными пробелами c обоих концов соответственно.

        .. code-block:: py

            ' ilnur '.strip()
            # 'ilnur'


    .. py:method:: swapcase()
        
        Возвращает новую строку :py:class:`str`,
        в которой регистр букв изменен с верхнего на нижний и наоборот.

        .. code-block:: py

            'Ilnur'.swapcase()
            # 'iLNUR'


    .. py:method:: title()
        
        Возвращает новую строку :py:class:`str`,
        в которой регистр букв соответствует заголовку.

        .. code-block:: py

            'ilnur'.title()
            # 'ILNUR'


    .. py:method:: translate(table, [deletechars])

        Выполняет преобразование строки в соответствии с таблицей замены.

        Упростить создание таблицы символов позволяет статический метод :py:meth:`maketrans`

        .. code-block:: py

            s = "Пример"
            d = {ord('П''): None, ord('p'): ord('P')}
            # d = {1088: 1056, 1055: None}
            s.translate(d)
            # s = 'РимеР'

    .. py:method:: upper()
        
        Возвращает новую строку :py:class:`str`, в верхнем регистре

        .. code-block:: py

            'iLnur'.upper()
            # 'ILNUR'


    .. py:method:: zfill(width)
        
        Возвращает новую строку :py:class:`str`,
        заданной длины, пустое пространство слева заполнится нулями

        .. code-block:: py

            '12'.zfill(5)
            # '00012'


unicode
-------

.. py:class:: unicode

    Юникодная строка, имеет теже методы что и :py:class:`str`


Экранированные последовательности
---------------------------------

=========== ========
Строка      Описание
=========== ========
\\\         слеш
\\'         апостроф
\\"         кавычки
\\a         ascii-символ звуковой сигнал
\\b         ascii-символ забоя
\\f         ascii-символ перевода формата
\\n         ascii-символ новой строки
\\N{имя}    именованный символ юникода (юникод)
\\r         ascii-символ возврата каретки
\\t         ascii-символ горизонтальной табуляции
\\uXXXX     16-ый код 16-й битного сивола (юникод)
\\UXXXXXXXX 16-ый код 32-й битного сивола (юникод)
\\v         ascii-символ вертикальной табуляции
\\000       8-ный код символа
\\xhh       16-ый код символа
=========== ========