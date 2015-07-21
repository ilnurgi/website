.. py:module:: xlrd

xlrd - интсрумент для чтения xls фалйов
=======================================

`Страничка проекта`_

`Скачать`_

`Официальная документация`_

`GitHub`_

.. _Страничка проекта: http://www.python-excel.org/
.. _Скачать: http://pypi.python.org/pypi/xlrd
.. _Официальная документация: https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966
.. _GitHub: https://github.com/python-excel/xlrd

Функции модуля
--------------

.. py:attribute:: empty_cell
    
    Пустая ячейка. 

    >>> xlrd.empty_cell
    empty:''

.. py:attribute:: error_text_from_code
    
    Словарь ошибок

    ==== ======= ========================================
    hex  value     описание
    ==== ======= ========================================
    0x00 #NULL!  Intersection of two cell ranges is empty
    0x07 #DIV/0! деление на ноль
    0x0F #VALUE! не правильный оператор
    0x17 #REF!   Illegal or deleted cell reference  
    0x1D #NAME?  Wrong function or range name  
    0x24 #NUM!   Value range overflow  
    0x2A #N/A    Argument or function not available
    ==== ======= ========================================

    >>> xlrd.error_text_from_code
    {0: '#NULL!',
     7: '#DIV/0!',
     15: '#VALUE!',
     23: '#REF!',
     29: '#NAME?',
     36: '#NUM!',
     42: '#N/A'}

.. py:method:: cellname(rowx, colx)
    
    Возвращает название ячейки

    :param rowx: столбец
    :type rowx: int
    :param colx: строка
    :type colx: int

    >>> xlrd.cellname(5, 7)
    'Н6'

.. py:method:: cellnameabs(rowx, colx, r1c1=0)
    
    Возвращает абсолютное название ячейки

    :param rowx: столбец
    :type rowx: int
    :param colx: строка
    :type colx: int

    >>> xlrd.cellname(5, 7)
    '$Н$6'

.. py:method:: colname(colx)
    
    Возвращает название столбца

    :param colx: столбец
    :type colx: int

    >>> xlrd.colname(7)
    'Н'    
    >>> xlrd.colname(27)
    'AB'

.. py:method:: count_records(filename, outfile=sys.stdout)
    
    Для отладки и анализа: обобщить BIFF записи файла. Т.е. получаем отсортированный файл (запись, количесвто).

    :param filename: путь к файлу
    :type filename: str
    :param outfile: объект для записи (должен иметь метод write) результатов

    >>> xlrd.count_records(src, open(dst, 'w'))

.. py:method:: dump(filename, outfile=sys.stdout, unnumbered=False)
    
    Для отладки, выгрузка BIFF записей в char и hex

    :param filename: путь к файлу
    :type filename: str
    :param outfile: объект для записи (должен иметь метод write) результатов
    :param unnumbered: опустить смещения

    >>> xlrd.dump(src, open(dst, 'w'))

.. py:method:: open_workbook(filename=None, logfile=sys.stdout, verbosity=0, pickleable=True, use_mmap=USE_MMAP, file_contents=None, encoding_override=None, formatting_info=False, on_demand=False, ragged_rows=False, )
    
    Открывает файл и возвращает объект :py:class:`xlrd.Book`

    :param filename: путь к файлу
    :type filename: str
    :param logfile: объект, для записи лог информации
    :param verbosity: уровень логируемой информации
    :param pickleable: что то связанное с использованием памяти, актуально для 2.4 и ниже. (Default is true. In Python 2.4 or earlier, setting to false will cause use of array.array objects which save some memory but can't be pickled. In Python 2.5, array.arrays are used unconditionally. Note: if you have large files that you need to read multiple times, it can be much faster to cPickle.dump() the xlrd.Book object once, and use cPickle.load() multiple times.)
    :param use_mmap: Whether to use the mmap module is determined heuristically. Use this arg to override the result. Current heuristic: mmap is used if it exists.
    :param file_contents: as a string or an mmap.mmap object or some other behave-alike object. If file_contents is supplied, filename will not be used, except (possibly) in messages.
    :param encoding_override: кодировка открываемого файла -- New in version 0.6.0
    :param formatting_info: Governs provision of a reference to an XF (eXtended Format) object for each cell in the worksheet. Default is False. This is backwards compatible and saves memory. "Blank" cells (those with their own formatting information but no data) are treated as empty (by ignoring the file's BLANK and MULBLANK records). It cuts off any bottom "margin" of rows of empty (and blank) cells and any right "margin" of columns of empty (and blank) cells. Only cell_value and cell_type are available. True provides all cells, including empty and blank cells. XF information is available for each cell. -- New in version 0.6.1
    :param on_demand: управляет загрузкой листов. При открытии файла загружаются сразу все листы или листы будут загружены позже при необходимости.
    :param ragged_rows: False (the default) means all rows are padded out with empty cells so that all rows have the same size (Sheet.ncols). True means that there are no empty cells at the ends of rows. This can result in substantial memory savings if rows are of widely varying sizes. See also the Sheet.row_len() method. -- New in version 0.7.2

.. py:method:: rangename3d(book, ref3d)

    Ref3D((1, 4, 5, 20, 7, 10)) => 'Sheet2:Sheet3!$H$6:$J$20'

.. py:method:: rangename3drel(book, ref3d, browx=None, bcolx=None, r1c1=0)

    Ref3D(coords=(0, 1, -32, -22, -13, 13), relflags=(0, 0, 1, 1, 1, 1)) R1C1 mode => 'Sheet1!R[-32]C[-13]:R[-23]C[12]' A1 mode => depends on base cell (browx, bcolx)

.. py:method:: xldate_as_tuple(xldate, datemode)
    
    Преобразует дату из Excel формата в кортеж c датой (год, месяц, день, час, минута, секунды).

    :param xldate: дата в Excel формате
    :param datemode: 0: 1900-based, 1: 1904-based. 
    :raises XLDateNegative: xldate < 0.00
    :raises XLDateAmbiguous: The 1900 leap-year problem (datemode == 0 and 1.0 <= xldate < 61.0)
    :raises XLDateTooLarge: Gregorian year 10000 or later
    :raises XLDateBadDatemode: datemode arg is neither 0 nor 1
    :raises XLDateError: Covers the 4 specific errors

    .. warning:: when using this function to interpret the contents of a workbook, you should pass in the Book.datemode attribute of that workbook. Whether the workbook has ever been anywhere near a Macintosh is irrelevant.

    .. note:: 1904-01-01 is not regarded as a valid date in the datemode 1 system; its "serial number" is zero.

    >>> date.value
    41403.9227662037
    >>> xlrd.xldate_as_tuple(date.value, 0)
    (2013, 5, 9, 22, 8, 47)
    >>> xlrd.xldate_as_tuple(date.value, 1)
    (2017, 5, 10, 22, 8, 47)

.. py:method:: xldate_from_date_tuple((year, month, day), datemode)

    Преобразует дату из кортежа, в формат даты Excel. 

    :param datemode: 0: 1900-based, 1: 1904-based.
    :raises XLDateAmbiguous: The 1900 leap-year problem (datemode == 0 and 1.0 <= xldate < 61.0)
    :raises XLDateBadDatemode: datemode arg is neither 0 nor 1
    :raises XLDateBadTuple: (year, month, day) is too early/late or has invalid component(s)
    :raises XLDateError: Covers the specific errors

.. py:method:: xldate_from_datetime_tuple(datetime_tuple, datemode)

    Преобразует дату и время из кортежа в формат даты и времени Excel.

    :param datemode: 0: 1900-based, 1: 1904-based.

.. py:method:: xldate_from_time_tuple((hour, minute, second))

    Преобразует время из кортежа, во время в формате Excel

    :raises XLDateBadTuple: Out-of-range hour, minute, or second

BaseObject
----------------------

.. py:class:: BaseObject
    
    Родительсикй класс для других классов модуля

    .. py:method:: dump(f=None, header=None, footer=None, indent=0)
    
        :param f: файловый объект для выгрузки дампа
        :param header: текс, записываемы в файл дампа перед дампом
        :type header: str
        :param footer: текст, записываемый после дампа
        :type footer: str
        :param indent: количество пробелов, заменяющих табуляцию
        :type indent: int

Book
----

.. py:class:: Book
    
    Объект "Книга"

    .. warning:: Вы не можете создать экземпляры данного класса сами. Данный объект возвращает метод :py:meth:`xlrd.open_workbook`.

    >>> book = xlrd.open_workbook(file_path)

    .. py:attribute:: biff_version
        
        Возвращает число, версию о BIFF (Binary Interchange File Format) используемый при создании файла. (Latest is 8.0 (represented here as 80), introduced with Excel 97. Earliest supported by this module: 2.0 (represented as 20).)

        >>> book.biff_version
        80

    .. py:attribute:: codepage

        Возвращает число, кодировку файла. Для BIFF 8 и выше это будет 1200, что означает юникод (UTF_16_LE). Для более ранних версии, используется число натиболее подходящее кодировке Python, например 1252 -> 'cp1252', 10000 -> 'mac_roman'.

        >>> book.codepage
        1200

    .. py:attribute:: colour_map

        Возвращает словарь, индексы цветов. Только если открывать книгу с атрибутом open_workbook(..., formatting_info=True)

        >>> book = xlrd.open_workbook(file_path)
        >>> book.colour_map
        {}
        >>> book = xlrd.open_workbook(file_path, formatting_info=True)
        >>> book.colour_map
        {0: (0, 0, 0),
         1: (255, 255, 255),
         2: (255, 0, 0),
         3: (0, 255, 0),
         ...}

    .. py:attribute:: countries

        Возвращает кортеж, содержащий код страны для 

        0. настройки пользовательского интерфейса
        1. региональных настроек

        Например: (1, 61) meaning (USA, Australia).

        >>> book.countries
        (1, 7)

    .. py:attribute:: datemode

        Возвращает число, формат даты файла
        
        0. => 1900 system (the Excel for Windows default).
        1. => 1904 system (the Excel for Macintosh default).

        >>> book.datemode
        0

    .. py:attribute: encoding
        
        Кодировка файла

        >>> book.encoding
        'utf_16_le'

    .. py:attribute:: font_list
        
        Возврашает список экземпляров объекта :py:class:`xlrd.Font` каждая из которых соответствует записи

        >>> book.font_list
        [<xlrd.formatting.Font at 0xb5f96c8c>,
         <xlrd.formatting.Font at 0xb5f0418c>,
         ...]

    .. py:attribute:: format_list

        Возвращает список экземпляров объекта :py:class:`xlrd.Format` каждая из которых соответствует записи. 
        It does not contain builtin formats. If you are creating an output file using (for example) pyExcelerator, use this list. The collection to be used for all visual rendering purposes is format_map. 

        >>> book.format_list
        [<xlrd.formatting.Format at 0xb5f04a4c>,
         <xlrd.formatting.Format at 0xb5f04aac>,
         ...]

    .. py:attribute:: format_map

        Возвращает словарь, полученный путем связывания :py:attr:`xlrd.XF.format_key` с объектом :py:class:`xlrd.Format`

        >>> book.format_map
        {0: <xlrd.formatting.Format at 0xb5f04dcc>,
         1: <xlrd.formatting.Format at 0xb5f04dec>,
         ...}

    .. py:attribute:: load_time_stage_1

        Возвращает число, время в секундах извлеченич XLS образа в одну строку. (Time in seconds to extract the XLS image as a contiguous string (or mmap equivalent).)

        >>> book.load_time_stage_1
        0.0

    .. py:attribute:: load_time_stage_2

        Возвращает число, время в секундах разбора XLS образа. (Time in seconds to extract the XLS image as a contiguous string (or mmap equivalent).)

        >>> book.load_time_stage_2
        0.14

    .. py:attribute:: name_and_scope_map
        
        Возвращает словарь. (A mapping from (lower_case_name, scope) to a single Name object.)

        >>> book.name_and_scope_map
        {}

    .. py:attribute:: name_map
        
        A mapping from lower_case_name to a list of Name objects. The list is sorted in scope order. Typically there will be one item (of global scope) in the list. 

        >>> book.name_map
        {}

    .. py:attribute:: name_obj_list
        
        Возвращает список, содержит объект :py:class:`xlrd.Name` для каждой записи книги

        >>> book.name_obj_list
        []

    .. py:attribute:: nsheets
        
        Возвращает число, количество листов в книге

        >>> book.nsheets
        3

    .. py:attribute:: palette_record

        Возвращает список.
        Если пользователь изменил любой из цветов в стандартной палитре, файл XLS будет содержать запись Палитра с 56 (16 для Excel 4.0 и ранее) значения RGB в нем, и этот список будет, например, [(r0, b0, g0 ), ..., (r55, b55, g55)]. В противном случае этот список будет пустым. Это то, что вам нужно, если вы пишете файл XLS выходной. Если вы хотите сделать клетки на экране или в PDF файле, используйте colour_map. 
        Книга должна быть открыта с параметром :py:meth:`xlrd.open_workbook(..., formatting_info=True)`

        (If the user has changed any of the colours in the standard palette, the XLS file will contain a PALETTE record with 56 (16 for Excel 4.0 and earlier) RGB values in it, and this list will be e.g. [(r0, b0, g0), ..., (r55, b55, g55)]. Otherwise this list will be empty. This is what you need if you are writing an output XLS file. If you want to render cells on screen or in a PDF file, use colour_map.)

        Extracted only if open_workbook(..., formatting_info=True)

        >>> book.palette_record
        []

    .. py:attribute:: user_name
        
        Возвращает строку, автора, который последним изменил файл.

        >>> book.user_name
        'ilnurgi'

    .. py:method:: xf_list

        Возвращает список объектов, экземпляров класса :py:class:`xlrd.XF` соответствующих каждой записи XF

        >>> book.xf_list
        [<xlrd.formatting.XF at 0xb5f04c4c>,
         <xlrd.formatting.XF at 0xb5f04dac>,
         <xlrd.formatting.XF at 0xb5f0a74c>,
         ...]


    .. py:method:: style_name_map

        Возвращает словарь. 
        This provides access via name to the extended format information for both built-in styles and user-defined styles.
        It maps name to (built_in, xf_index), where:
        name is either the name of a user-defined style, or the name of one of the built-in styles. Known built-in names are Normal, RowLevel_1 to RowLevel_7, ColLevel_1 to ColLevel_7, Comma, Currency, Percent, "Comma [0]", "Currency [0]", Hyperlink, and "Followed Hyperlink".
        built_in 1 = built-in style, 0 = user-defined
        xf_index is an index into Book.xf_list.
        References: OOo docs s6.99 (STYLE record); Excel UI Format/Style 

        >>> book.style_name_map
        {u'20% - Accent1': (0, 16),
         u'20% - Accent2': (0, 17),
         u'20% - Accent3': (0, 18),
         u'20% - Accent4': (0, 19),
         u'20% - Accent5': (0, 20),
         ...}


    .. py:method:: release_resources()
        
        Данный метод имеет двойное предназначение.

        1. Вы можете вызвать данный метод для освобождения памяти, после загрузки необходимого листа.

        2. Также данный метод вызывается автоматический:

          * когда open_workbook вызывает исключение
          * если вы используете оператор :py:meth:`with`

    .. py:method:: sheet_by_index(sheetx)

        Возвращает лист книги по индексу, экземпляр класса :py:class:`xlrd.Sheet`
        
        :param int sheetx: индекс листа
        
        >>> sheet = book.sheet_by_index(1)
        >>> sheet
        <xlrd.sheet.Sheet at 0xb5f04cec>

    .. py:method:: sheet_by_name(sheet_name)

        Возвращает лист книги по наименованию, экземпляр класса :py:class:`xlrd.Sheet`
        
        :param str sheet_name: название листа

        >>> names = book.sheet_names()
        >>> sheet = book.sheet_by_name(names[0])
        >>> sheet
        <xlrd.sheet.Sheet at 0xb5f04cec>

    .. py:method:: sheet_loaded(sheet_name_or_index)

        Возвращает True|False, загружен ли лист

        :param sheet_name_or_index: индекс или название листа
        :type sheet_name_or_index: int, str

        >>> book.sheet_loaded(0)
        True
        >>> book.sheet_loaded(names[0])
        True

    .. py:method:: sheet_names()
        
        Возвращает список названий листов книги.

        >>> book.sheet_names()
        [u'Таблица1', u'Таблица 2']

    .. py:method:: sheets()
        
        Возвращает список листов книги, экземпляров :py:class:`xlrd.Sheet`.

        >>> book.sheets()
        [<xlrd.sheet.Sheet at 0xb5f04cec>,
         <xlrd.sheet.Sheet at 0xb5f2a66c>,
         <xlrd.sheet.Sheet at 0xb5f2adac>]

    .. py:method:: unload_sheet(sheet_name_or_index)

        Выгружает указанный лист.

        :param sheet_name_or_index: индекс или название листа
        :type sheet_name_or_index: int, str

        >>> book.sheet_loaded(0)
        True
        >>> book.unload_sheet(0)
        >>> book.sheet_loaded(0)
        False


Cell
----

.. py:class:: Cell(ctype, value, xf_index=None)

    Объект "Ячейка", содержит информацию об одной ячейке

    .. warning:: вы не сможете создать этот класс самостоятельно. Данный объект возвращается только методами объекта :py:class:`xlrd.Sheet`

    :param int ctype: 
    :param value: зависит от ctype
    :param xf_index: None, если "formatting_info" не включен при открытии книги

    Таблица соответсвии типов ячеек:

    =============== =========== ===========================
    Type symbol     Type number Python value
    =============== =========== ===========================
    XL_CELL_EMPTY   0           пустая строка u''
    XL_CELL_TEXT    1           Unicode строка
    XL_CELL_NUMBER  2           число с плавающей точкой
    XL_CELL_DATE    3           число с плавающей точкой
    XL_CELL_BOOLEAN 4           1 или 0
    XL_CELL_ERROR   5           число, индекс ошибки; текстовое представление ошибки можно узнать из словаря :py:attr:`xlrd.error_text_from_code`
    XL_CELL_BLANK   6           пустая строка u''. Тип появится, если открывать книгу с атрибутом formatting_info=True.
    =============== =========== ===========================

Colinfo
-------

.. py:class:: Colinfo

    Объект "Колонка"

    .. py:attribute:: bit1_flag
        
        Value of a 1-bit flag whose purpose is unknown but is often seen set to 1

    .. py:attribute:: collapsed

        Возвращает 1|0, колокна разрушена

    .. py:attribute:: hidden
        
        Возвращает 1|0, колокна скрыта

    .. py:attribute:: outline_level

        Возвращает число, уровень границ колонки от 0 до 7

    .. py:attribute:: width

        Возвращает число, ширину колонки в 1/256 ширины нулевого параметра. (Width of the column in 1/256 of the width of the zero character, using default font (first FONT record in the file).)

    .. py:attribute:: xf_index

        Возвращает число, XF индекс, для формирования пустой ячейки

EqNeAttrs
----------

.. py:class:: EqNeAttrs 

    Миксин для объектов "Формат", "Шрифт" и т.п., для возможности сравнивания значений объектов

Font
----

.. py:class:: Font 

    Объект "Шрифт", содержит информацию о шрифте


    .. py:attribute:: bold
        
        True|False жирность шрифта

    .. py:attribute:: character_set

        === ==================================        
        key value
        === ==================================        
        0   ANSI Latin
        1   System default
        2   Symbol
        77  Apple Roman
        128 ANSI Japanese Shift-JIS
        129 ANSI Korean (Hangul)
        130 ANSI Korean (Johab)
        134 ANSI Chinese Simplified GBK
        136 ANSI Chinese Traditional BIG5
        161 ANSI Greek
        162 ANSI Turkish
        163 ANSI Vietnamese
        177 ANSI Hebrew
        178 ANSI Arabic
        186 ANSI Baltic
        204 ANSI Cyrillic
        222 ANSI Thai
        238 ANSI Latin II (Central European)
        255 OEM Latin I
        === ==================================        

        .. py:attribute:: colour_index

        .. py:attribute:: escapement
            
            Возвращает число, регистр:

            1. верхний
            2. нижний

        .. py:attribute:: family

            Возвращает число, семейство шрифта

                0. None (unknown or don't care)
                1. Roman (variable width, serifed)
                2. Swiss (variable width, sans-serifed)
                3. Modern (fixed width, serifed or sans-serifed)
                4. Script (cursive)
                5. Decorative (specialised, for example Old English, Fraktur)

        .. py:attribute:: font_index

            The 0-based index used to refer to this Font() instance. Note that index 4 is never used; xlrd supplies a dummy place-holder.

        .. py:attribute:: height
        
            Высота шрифта (твипы). Твип = 1/20 пукта.

        .. py:attribute:: italic
            
            Возвращает 1|0, шрифт курсивый

        .. py:attribute:: name
            
            Возвращает строку, название шрифта.

        .. py:attribute:: outline 
            
            Возвращет 1|0, шрифт с контуром (Macintosh only)

        .. py:attribute:: shadow
            
            Возвращет 1|0, шрифт с тенью (Macintosh only)


        .. py:attribute:: struck_out
            
            Возвращет 1|0, шрифт перечеркнутый

        .. py:attribute:: underline_type

            Возвращет число, подчеркивание шрифта

            0. Отсутсвует
            1. Одинарный; 0x21 (33) = Single accounting
            2. Двойное; 0x22 (34) = Double accounting

        .. py:attribute:: underlined
            
            Возвращет 1|0, шрифт с подчеркиванием

        .. py:attribute:: weight

            Возвращает число, уровень жирности шрифта от 100 до 1000.

Format
------

.. py:class:: Format(format_key, type, format_str) 

    Объект "Формат ячйки"

    .. py:attribute:: format_key

        Возвращает число, ключ :py:attr:`xlrd.format_map`

    .. py:attribute:: format_str

        Возвращает строку, название формата

    .. py:attribute:: type
        
        Возвращает число, определяющий тип формата:

            * FUN = 0 # unknown 
            * FDT = 1 # date 
            * FNU = 2 # number 
            * FGE = 3 # general 
            * FTX = 4 # text

Hyperlink
---------

.. py:class:: Hyperlink

    Объект "Гиперссылка", содержит атрибуты гиперссылки. Объект можно получить из объекта "Лист" :py:attr:Sheet.hyperlink_list` или :py:attr:`hyperlink_map`

    .. py:attribute:: desc

        Какое-то описание. (Description ... this is displayed in the cell, and should be identical to the cell value. Unicode string, or None. It seems impossible NOT to have a description created by the Excel UI.)

    .. py:attribute:: fcolx

        Возвращает число, первую колонку

    .. py:attribute:: frowx

        Возвращает число, первую строку

    .. py:attribute:: lcolx

        Возвращает число, номер последней колонки

    .. py:attribute:: lrowx

        Возвращает число, номер последней строки

    .. py:attribute:: quicktip
        
        Возвращает текст, подсказка при наведении на ссылку

    .. py:attribute:: target
        
        Target frame. Unicode string. Note: I have not seen a case of this. It seems impossible to create one in the Excel UI.

    .. py:attribute:: textmark
        
        "Textmark": the piece after the "#" in "http://docs.python.org/library#struct_module", or the Sheet1!A1:Z99 part when type is "workbook".

    .. py:attribute:: type
        
        Возвращает строку, тип гиперссылки: 'url', 'unc', 'local file', 'workbook', 'unknown'

    .. py:attribute:: url_or_path
        
        Возвращает строку, полный путь ссылки

Name
----

.. py:class:: Name

    Объект "Информация"

    .. py:attribute:: area2d(clipped=True)
        
        Возвращает кортеж (sheet_object, rowxlo, rowxhi, colxlo, colxhi), часть области листа

        :param clipped: обрезает область (If true (the default), the returned rectangle is clipped to fit in (0, sheet.nrows, 0, sheet.ncols) -- it is guaranteed that 0 <= rowxlo <= rowxhi <= sheet.nrows and that the number of usable rows in the area (which may be zero) is rowxhi - rowxlo; likewise for columns.)

        :raises XLRDError: The name is not a constant absolute reference to a single area in a single sheet.

    .. py:attribute:: binary

        Возвращет число:

            0. Formula definition; 
            1. Binary data

    .. py:attribute:: builtin

        Возвращает число:

            0. User-defined name; 
            1. Built-in name (common examples: Print_Area, Print_Titles; see OOo docs for full list)

    .. py:attribute:: complex

        Возвращает число:

            0. Простая формула 
            1. Комплексная формула

    .. py:attribute:: func

        Возвращает число:

            0. Макро команда
            1. Макро функция

    .. py:attribute:: funcgroup
        
        Возвращает строку, группу функции

    .. py:attribute:: hidden

        Возвращает число:
        
            0. видимый
            1. скрытый

    .. py:attribute:: macro

        Возвразает число:
            
            0. стандартное имя
            1. имя макроса

    .. py:attribute:: name
        
        Возвращает строку, название класса

    .. py:attribute:: name_index
        
        Возвращает число, индекс данного объекта в :py:attr:`xlrd.Book.name_obj_list`

    .. py:attribute:: raw_formula
        
        Возвращает 8 битную строку

    .. py:attribute:: result
    
        Возвращает результат вычисления формулы или None.

    .. py:attribute:: scope

        Возвращает число:

            * -1: глобальное имя
            * -2: имя относится к листу
            * -3: недействительное имя
            * 0 <= scope < book.nsheets: номер листа

    .. py:attribute:: vbasic

        Возвращает:

            0. Sheet macro; 
            1. VisualBasic macro. Relevant only if macro == 1

    .. py:method:: cell()
        
        Возвращает экземпляр объекта "Ячейка", :py:class:`xlrd.Cell`
        
        :raises XLRDError: The name is not a constant absolute reference to a single cell.

Note
----

.. py:class:: Note

    Объект "Примечание"

    .. py:attribute:: author
        
        Возвращает строку, автора примечания

    .. py:attribute:: col_hidden
        
        Возвращает True|False, если колонка скрыта

    .. py:attribute:: colx
        
        Возвращает число, номер колонки

    .. py:attribute:: rich_text_runlist
        
        Возвращает список кортежей (offset_in_string, font_index). В отличие от :py:attr:`xlrd.Sheet.rich_text_runlist_map` первое смещение всегда должно быть 0.

    .. py:attribute:: row_hidden
        
        Возвращает True|False, если строка скрыта

    .. py:attribute:: rowx
    
        Возвращает число, номер строки

    .. py:attribute:: show
    
        Возвращает True|False, если примечание всегда отображается

    .. py:attribute:: text

        Возвращает строку, текст примечания

Operand
-------

.. py:class:: Operand(akind=None, avalue=None, arank=0, atext='?')

    Используется в оценке формул. В следующей таблице описываются типы и как их значения представлены.

        =========== =========== ====================
        Kind symbol Kind number Value representation
        =========== =========== ====================
        oBOOL       3           целое: 0 => False; 1 => True
        oERR        4           None, или код ошибки
        oMSNG       5           Используется в качестве заполнителя для отсутствующего (не прилагается) аргумента функции. (Если * не * появляются в качестве окончательного результата формулы. Значение Нет. (Should *not* appear as a final formula result. Value is None.)
        oNUM        2           A float. Note that there is no way of distinguishing dates.
        oREF        -1          The value is either None or a non-empty list of absolute Ref3D instances.
        oREL        -2          The value is None or a non-empty list of fully or partially relative Ref3D instances.
        oSTRG       1           A Unicode string.
        oUNK        0           The kind is unknown or ambiguous. The value is None
        =========== =========== ====================

    .. py:attribute:: akind
        
        oUNK means that the kind of operand is not known unambiguously.

    .. py:attribute:: atext
        
        The reconstituted text of the original formula. Function names will be in English irrespective of the original language, which doesn't seem to be recorded anywhere. The separator is ",", not ";" or whatever else might be more appropriate for the end-user's locale; patches welcome.

    .. py:attribute:: value
        
        None means that the actual value of the operand is a variable (depends on cell data), not a constant.

Ref3D
-----

.. py:class:: Ref3D(atuple)
    
    Абсолютная или относительная ссылка на ячейку

The coords attribute is a tuple of the form:
(shtxlo, shtxhi, rowxlo, rowxhi, colxlo, colxhi)
where 0 <= thingxlo <= thingx < thingxhi.
Note that it is quite possible to have thingx > nthings; for example Print_Titles could have colxhi == 256 and/or rowxhi == 65536 irrespective of how many columns/rows are actually used in the worksheet. The caller will need to decide how to handle this situation. Keyword: IndexError :-)

The components of the coords attribute are also available as individual attributes: shtxlo, shtxhi, rowxlo, rowxhi, colxlo, and colxhi.

The relflags attribute is a 6-tuple of flags which indicate whether the corresponding (sheet|row|col)(lo|hi) is relative (1) or absolute (0).
Note that there is necessarily no information available as to what cell(s) the reference could possibly be relative to. The caller must decide what if any use to make of oREL operands. Note also that a partially relative reference may well be a typo. For example, define name A1Z10 as $a$1:$z10 (missing $ after z) while the cursor is on cell Sheet3!A27.
The resulting Ref3D instance will have coords = (2, 3, 0, -16, 0, 26) and relflags = (0, 0, 0, 1, 0, 0).
So far, only one possibility of a sheet-relative component in a reference has been noticed: a 2D reference located in the "current sheet". 
This will appear as coords = (0, 1, ...) and relflags = (1, 1, ...).

Rowinfo
-------

.. py:class:: Rowinfo()
    
    Объект "Строка"

    .. py:attribute:: height 

        Высота строки в твипсах (twip == 1/20 of a point.)

    .. py:attribute:: has_default_height

        Возвращает 0|1, стандартная высота строка

    .. py:attribute:: outline_level

        Возвращает число, уровень границы (0 ... 7)

    .. py:attribute:: outline_group_starts_ends

        1 = Outline group starts or ends here (depending on where the outline buttons are located, see WSBOOL record [TODO ??]), and is collapsed

    .. py:attribute:: hidden

        Возвращает 1|0, строка скрыта

    .. py:attribute:: height_mismatch

        Возвращает 1|0 если высота строки и высота строки не совпадают

    .. py:attribute:: has_default_xf_index

        Возвращает 1|0 используется ли xf_index атрибут

    .. py:attribute:: xf_index

        Возвращает чилсо, XF индекс пустых ячеек. (Index to default XF record for empty cells in this row. Don't use this if has_default_xf_index == 0.)

    .. py:attribute:: additional_space_above

        This flag is set, if the upper border of at least one cell in this row or if the lower border of at least one cell in the row above is formatted with a thick line style. Thin and medium line styles are not taken into account.

    .. py:attribute:: additional_space_below

        This flag is set, if the lower border of at least one cell in this row or if the upper border of at least one cell in the row below is formatted with a medium or thick line style. Thin line styles are not taken into account.

Sheet
-----

.. py:class:: Sheet(book, position, name, number)
    
    Объект "Лист", содержит информацию о листе

    .. py:attribute:: book
        
        Возвращает родительский объект :py:class:`xlrd.Book`

    .. py:attribute:: cell_note_map
        
        Возвращает словарь, содержащий информацию об объектах "Примечание" :py:class:`xlrd.Note`. 

    .. py:attribute:: col_label_ranges
        
        Список адресов, диапазонов ячеек, содержащих заголовки столбцов

        >>> for crange in thesheet.col_label_ranges:
                rlo, rhi, clo, chi = crange
                for rx in xrange(rlo, rhi):
                    for cx in xrange(clo, chi):
                        print "Column label at (rowx=%d, colx=%d) is %r" \
                            (rx, cx, thesheet.cell_value(rx, cx))

    .. py:attribute:: colinfo_map
        
        The map from a column index to a Colinfo object. Often there is an entry in COLINFO records for all column indexes in range(257). Note that xlrd ignores the entry for the non-existent 257th column. On the other hand, there may be no entry for unused columns. Populated only if open_workbook(formatting_info=True).

    .. py:attribute:: default_additional_space_above
        
        Возвращает строку, стандартное значение для ячейки

    .. py:attribute:: default_additional_space_below
        
        Возвращает строку, стандартное значение для ячейки

    .. py:attribute:: default_row_height
        
        Возвращает число, стандартное значение для высоты строки

    .. py:attribute:: default_row_height_mismatch
        
        Default value to be used for a row if there is no ROW record for that row. From the optional DEFAULTROWHEIGHT record.

    .. py:attribute:: default_row_hidden
        
        Default value to be used for a row if there is no ROW record for that row. From the optional DEFAULTROWHEIGHT record.

    .. py:attribute:: defcolwidth

        Default column width from DEFCOLWIDTH record, else None. From the OOo docs:
        """Column width in characters, using the width of the zero character from default font (first FONT record in the file). Excel adds some extra space to the default width, depending on the default font and default font size. The algorithm how to exactly calculate the resulting column width is not known.
        Example: The default width of 8 set in this record results in a column width of 8.43 using Arial font with a size of 10 points."""
        For the default hierarchy, refer to the Colinfo class. 

    .. py:attribute:: gcw
        
        A 256-element tuple corresponding to the contents of the GCW record for this sheet. If no such record, treat as all bits zero. Applies to BIFF4-7 only. See docs of the Colinfo class for discussion.

    .. py:attribute:: has_pane_record
        
        Boolean specifying if a PANE record was present, ignore unless you're xlutils.copy

    .. py:attribute:: horizontal_page_breaks
        
        A list of the horizontal page breaks in this sheet. Breaks are tuples in the form (index of row after break, start col index, end col index). Populated only if open_workbook(formatting_info=True). 

    .. py:attribute:: horz_split_first_visible
        
        Index of first visible row in bottom frozen/split pane

    .. py:attribute:: horz_split_pos
        
        Number of rows in top pane (frozen panes; for split panes, see comments below in code)

    .. py:attribute:: hyperlink_list
    
        Возвращает список гиперссылок :py:class:`xlrd.Hyperlink`

    .. py:attribute:: hyperlink_map
        
        Словарь, ссылки на гиперссылки

    .. py:attribute:: merged_cells
        
        List of address ranges of cells which have been merged. These are set up in Excel by Format > Cells > Alignment, then ticking the "Merge cells" box. 
        Extracted only if open_workbook(formatting_info=True). 
        How to deconstruct the list:

        >>> for crange in thesheet.merged_cells:
                rlo, rhi, clo, chi = crange
                for rowx in xrange(rlo, rhi):
                    for colx in xrange(clo, chi):
                        # cell (rlo, clo) (the top left one) will carry the data
                        # and formatting info; the remainder will be recorded as
                        # blank cells, but a renderer will apply the formatting info
                        # for the top left cell (e.g. border, pattern) to all cells in
                        # the range.
    
    .. py:attribute:: name

        Строка, название листа

    .. py:attribute:: ncols
        
        Число, количество колонок

    .. py:attribute:: nrows
        
        Число, количество строк

    .. py:attribute:: rich_text_runlist_map
        
        Mapping of (rowx, colx) to list of (offset, font_index) tuples. The offset defines where in the string the font begins to be used. Offsets are expected to be in ascending order. If the first offset is not zero, the meaning is that the cell's XF's font should be used from offset 0. 
        This is a sparse mapping. There is no entry for cells that are not formatted with rich text. 
        Populated only if open_workbook(formatting_info=True). 
        How to use:

        >>> runlist = thesheet.rich_text_runlist_map.get((rowx, colx))
            if runlist:
                for offset, font_index in runlist:
                    # do work here.
                    pass

    .. py:attribute:: row_label_ranges
        
        Список адресов ячеек, содержащих названия строк

    .. py:attribute:: rowinfo_map
        
        Словарь, содержащий ссылки на объекты колонки :py:class:`xlrd.Rowinfo`. Доступен только при открытии книги с параметром open_workbook(formatting_info=True).

    .. py:attribute:: split_active_pane
        
        Frozen panes: ignore it. Split panes: explanation and diagrams in OOo docs.

    .. py:attribute:: standardwidth
    
        Стандартная ширина

    .. py:attribute:: vert_split_first_visible
        
        Index of first visible column in right frozen/split pane

    .. py:attribute:: vert_split_pos
        
        Number of columns in left pane (frozen panes; for split panes, see comments below in code)

    .. py:attribute:: vertical_page_breaks
        
        A list of the vertical page breaks in this sheet. Breaks are tuples in the form (index of col after break, start row index, end row index). Populated only if open_workbook(formatting_info=True). 

    .. py:attribute:: visibility
        
        Число, видимость листа:

            0. видимый 
            1. скрытый, можно отобразить через интерфейс
            2. скрытый, можно отобразить только через VBA

    .. py:method:: cell(rowx, colx)
        
        Возвращает ячейку :py:class:`xlrd.Cell`

        :param int rowx: номер колонки
        :param int colx: номер строки

    .. py:method:: cell_type(rowx, colx)
        
        Возвращает тип ячейки

        :param int rowx: номер колонки
        :param int colx: номер строки

    .. py:method:: cell_value(rowx, colx)
        
        Возвращает значение ячейки

        :param int rowx: номер колонки
        :param int colx: номер строки

    .. py:method:: cell_xf_index(rowx, colx) 
        
        Возвращает xf_index ячейки

        :param int rowx: номер колонки
        :param int colx: номер строки

    .. py:method:: col(colx) 
        
        Возвращает список ячеек строки
        
        :param int colx: номер строки

    .. py:method:: col_slice(colx, start_rowx=0, end_rowx=None)

        Возвращает список, срез ячеек
        
        :param int colx: номер строки
        :param int start_rowx: начальная позиция
        :param int end_rowx: конечная позиция

    .. py:method:: col_types(colx, start_rowx=0, end_rowx=None)

        Возвращает список, срез типов ячеек
        
        :param int colx: номер строки
        :param int start_rowx: начальная позиция
        :param int end_rowx: конечная позиция

    .. py:method:: col_values(colx, start_rowx=0, end_rowx=None)

        Возвращает список, срез значений ячеек
        
        :param int colx: номер строки
        :param int start_rowx: начальная позиция
        :param int end_rowx: конечная позиция

    .. py:method:: computed_column_width(colx)

        Число, ширина колонки

        :param int colx: номер колонки
        
    .. py:method:: row(rowx)
        
        Возвращает список ячеек колонки
        
        :param int rowx: номер колонки

    .. py:method:: row_len(rowx)
        
        Возвращает число, количество колонок
        
        :param int rowx: номер колонки

    .. py:method:: row_slice(rowx, start_colx=0, end_colx=None)

        Возвращает список, срез ячеек
        
        :param int rowx: номер строки
        :param int start_colx: начальная позиция
        :param int end_colx: конечная позиция

    .. py:method:: row_types(rowx, start_colx=0, end_colx=None) 

        Возвращает список, срез типов ячеек
        
        :param int rowx: номер строки
        :param int start_colx: начальная позиция
        :param int end_colx: конечная позиция

    .. py:method:: row_values(rowx, start_colx=0, end_colx=None) 

        Возвращает список, срез значений ячеек
        
        :param int rowx: номер строки
        :param int start_colx: начальная позиция
        :param int end_colx: конечная позиция

XF
--

.. py:class:: XF()
    
    Расширенная информация о листе, ячейки и т.п.

    Следующие флаги несут информацию о применении XF

        * _alignment_flag
        * _background_flag
        * _border_flag
        * _font_flag
        * _format_flag
        * _protection_flag

    Для ячеек, 0 - родительский стиль, 1 - текущий XF.

    Для стилей, 0 - действительный, 1 - не действительный
 

    .. py:attribute:: alignment
    
        Экземпляр объекта :py:class:`xlrd.XFAlignment`

    .. py:attribute:: background

        Экземпляр объекта :py:class:`xlrd.XFBackground`

    .. py:attribute:: border

        Экземпляр объекта :py:class:`xlrd.XFBorder`

    .. py:attribute:: font_index
        
        Число, индекс из :py:attr:`xlrd.Book.font_list`

    .. py:attribute:: format_key
        
        Число, ключ из :py:attr:`xlrd.Book.format_map`

        .. warning:: OOo docs on the XF record call this "Index to FORMAT record". It is not an index in the Python sense. It is a key to a map. It is true only for Excel 4.0 and earlier files that the key into format_map from an XF instance is the same as the index into format_list, and only if the index is less than 164.

    .. py:attribute:: is_style

        Возвращает: 
            
            0. XF ячейки
            1. XF стиля

    .. py:attribute:: parent_style_index

        Для ячейки возвращает число, индекс :py:meth:`xlrd.Book.xf_list`.

        Для стиля возвращает 0xFFF

    .. py:attribute:: protection

        Экземпляр объекта :py:class:`xlrd.XFProtection`

    .. py:attribute:: xf_index
        
        Число, индекс :py:class:`xlrd.Book.xf_list`

XFAlignment
-----------

.. py:class:: XFAlignment()
    
    Выравнивание листа, ячейки и т.п.

    .. py:attribute:: hor_align
        
        Values: section 6.115 (p 214) of OOo docs

    .. py:attribute:: indent_level
        
        A number in range(15).

    .. py:attribute:: rotation
        
        Values: section 6.115 (p 215) of OOo docs.
        
        .. note:: file versions BIFF7 and earlier use the documented "orientation" attribute; this will be mapped (without loss) into "rotation".

    .. py:attribute:: shrink_to_fit
    
        1 = shrink font size to fit text into cell.

    .. py:attribute:: text_direction
        
        Возвращает:
            0. выравнивание по контексту
            1. слева-направо
            2. справа-налево

    .. py:attribute:: text_wrapped
        
        Возвращает:
            
            1. пекст переносится

    .. py:attribute:: vert_align
        
        Values: section 6.115 (p 215) of OOo docs

XFBackground
------------

.. py:class:: XFBackground()
    
    Фон листа, ячейки и т.п.

    .. py:attribute:: background_colour_index

    .. py:attribute:: fill_pattern

    .. py:attribute:: pattern_colour_index

XFBorder
--------

.. py:class:: XFBorder()
    
    Границы листа, ячейки и т.п.

    Есть несколько значений типов границ: 

        0. нет линий
        1. тонкий
        2. средний
        3. с точками
        4. пунктирная
        5. толстая
        6. двухместный
        7. hair
        8. средний пунктирная
        9. тонкий штрихпунктирной
        10. средняя штрихпунктирной
        11. тонкий тире-точка-пунктир
        12. средняя тире-точка-пунктир
        13. наклонная среднего штрихпунктирной. 

    .. py:attribute:: bottom_colour_index
        
        Число, индекс цвета нижней границы

    .. py:attribute:: bottom_line_style
        
        Число, тип нижней границы

    .. py:attribute:: diag_colour_index
        
        Число, индекс цвета диагональных линий

    .. py:attribute:: diag_down
        
        Возвращает 1, если диагональ слева сверху вниз вправо

    .. py:attribute:: diag_line_stylу
        
        Число, тип линии диагонали

    .. py:attribute:: diag_up

        Возвращает 1, если диагональ слева снизу вверх вправо

    .. py:attribute:: left_colour_index
        
        Число, индекс цвета левой границы

    .. py:attribute:: left_line_style

        Число, тип левой границы

    .. py:attribute:: right_colour_index

        Число, индекс цвета правой границы

    .. py:attribute:: right_line_style
        
        Число, тип правой границы

    .. py:attribute:: top_colour_index
        
        Число, индекс цвета верхней границы

    .. py:attribute:: top_line_style
        
        Число, тип верхней границы

XFProtection
------------

.. py:class:: XFProtection()
    
    Защита листа, ячейки и т.п.

    .. py:attribute:: cell_locked
    
        Возвращает 1, ячейка заблокирована

    .. py:attribute:: formula_hidden
        
        Возвращает 1, формула скрыта