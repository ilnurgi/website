.. py:module:: docx

docx - инструмент для работы с docx форматом
============================================


Document
--------


.. py:class:: docx.api.Document([str path])

    создает пустой документ или открывает существующий


    .. py:attribute:: inline_shapes

        возвращает экземпляры :py:class:`docx.InlineShape` документа


    .. py:attribute:: paragraphs

        возвращает список параграфов документа :py:class:`Paragraph`


    .. py:attribute:: sections

        возвращает список секции документа :py:class:`Sections`


    .. py:attribute:: tables

        возвращает список таблиц документа :py:class:`Table`


    .. py:method:: add_heading(str text, [int level=0...9])

        добавляет заголовок и возвращает его экземпляр


    .. py:method:: add_bage_break()

        добавляет новый лист в документ


    .. py:method:: add_paragraph(str text, [str style])

        добавляет новый параграф в документ и возвращает его экземпляр :py:class:`Paragraph`


    .. py:method:: add_picture(str path, [width], [height])

        добавляет картинку в документ и возвращает его экземпляр


    .. py:method:: add_section([start_type])

        добавляет новцую секцию в документ и возвращает его экземпляр :py:class:`Section` WD_SECTION.ODD_PAGE


    .. py:method:: add_table(int rows, int cols, [str style])

        добавляет новую таблицу в документ и возвращает его экземпляр :py:class:`Table`


    .. py:method:: save(str path)

        сохраняет документ в файл


Section
-------


.. py:class:: docx.section.Section(sectPr)

    объект секция


    .. py:attribute:: bottom_margin

        отступ сверху


    .. py:method:: footer_distance


    .. py:method:: gutter


    .. py:method:: header_distance


    .. py:attribute:: left_margin

        отступ слева


    .. py:attribute:: orientation

        ориентация секции, :py:attr:`WD_ORIENTATION`


    .. py:attribute:: page_height

        высота сецкии


    .. py:attribute:: page_width

        ширина сецкии


    .. py:attribute:: right_margin

        отступ слева


    .. py:attribute:: start_type

        тип разделителя секции (NEW_PAGE(2), EVEN_PAGE (3), ODD_PAGE (4))


    .. py:attribute:: top_margin

        отступ сверху


Sections
--------


.. py:class:: docx.parts.document.Sections(document)

    секции документа


Table
-----


.. py:class:: docx.table.Table

    таблица в документе


    .. py:attribute:: autofit

        автовыравнивание ширины столбца по содержимому


    .. py:attribute:: columns

        список колонок таблицы :py:ref:`columns`


    .. py:attribute:: rows

        список строк :py:class:`_Row` таблицы


    .. py:attribute:: style

        стиль для таблицы


    .. py:method:: add_column()

        добавляет колонку в таблицу, возвращает :py:class:`_Column`


    .. py:method:: add_row()

        добавляет строку в таблицу, возвращает :py:class:`_Row`


    .. py:method:: cell(int row, int coll)

        возвращает объект ячейки :py:class:`_Cell`



_Cell
-----


.. py:class:: docx.table._Cell(tc, parent)

    объект ячейки таблицы документа

    
    .. py:attribute:: paragraphs

        список параграфов :py:class:`Paragraph` ячейки 

    
    .. py:attribute:: tables

        список таблиц :py:class:`Table` ячейки

    
    .. py:attribute:: text

        значение ячейки

    
    .. py:attribute:: width

        ширина ячейки

    
    .. py:method:: add_paragraph(str text, [str style])

        добавляет новый параграф в ячейку таблицы и возвращает экземпляр :py:class:`Paragraph`

    
    .. py:method:: add_table(int rows, int cols)

        добавляет таблицу в ячейку таблицы и возвращает экземпляр :py:class:`Table`


_Row
----


.. py:class:: docx.table._Row(tr, parent)

    объект строка таблицы


    .. py:attribute:: cells

        список ячеек строки :py:class:`_Cell`

_Rows
-----


.. py:class:: docx.table._Rows(tr, parent)

    список строк таблицы


_Column
-------


.. py:class:: docx.table._Column(col, tbl, parent)

    объект колонка таблицы


    .. py:attribute:: cells

        список ячеек колонки :py:class:`_Cell`


    .. py:attribute:: width

        ширина колонки


.. _columns:

Columns
-------


.. py:class:: docx.table._Columns(tbl, parent)

    список колонок таблицы


Paragraph
---------


.. py:class:: docx.text.Paragraph(p, parent)

    параграф


    .. py:attribute:: alignment

        выранивание параграфа,  WD_PARAGRAPH_ALIGNMENT


    .. py:attribute:: runs

        список :py:class:`Run` объектов


    .. py:attribute:: style

        стиль параграфа


    .. py:attribute:: text

        содержимое параграфа


    .. py:method:: add_run(str text, [str style])

        добавляет в параграф, возвращает экземпляр текста :py:class:`Text`


    .. py:method:: clear()

        очищает параграф


    .. py:method:: insert_paragraph_before(str text, [str style])

        возваращает новы параграф, вставленный перед текущим текстом


Run
---


.. py:class:: docx.text.Run(r, parent)

    объект ...


    .. py:attribute:: all_caps


    .. py:attribute:: bold

        жирность текста


    .. py:attribute:: complex_script

        жирность текста


    .. py:attribute:: cs_bold
    .. py:attribute:: cs_italic
    .. py:attribute:: double_strike
    .. py:attribute:: emboss
    .. py:attribute:: hidden
    .. py:attribute:: imprint
    .. py:attribute:: italic
    .. py:attribute:: math
    .. py:attribute:: no_proof
    .. py:attribute:: outline
    .. py:attribute:: rtl
    .. py:attribute:: shadow
    .. py:attribute:: small_caps
    .. py:attribute:: snap_to_grid
    .. py:attribute:: spec_vanish
    .. py:attribute:: strike
    .. py:attribute:: style
    .. py:attribute:: text
    .. py:attribute:: underline
    .. py:attribute:: web_hidden        


    .. py:method:: add_break([int break_type=6])

        добавляет перевод строки WD_BREAK.LINE, WD_BREAK.PAGE, and WD_BREAK.COLUMN


    .. py:method:: add_picture(str path, [width], [height])

        добавляет картинку в и возвращает экземпляр :py:class:`InlineShape`


    .. py:method:: add_tab()


    .. py:method:: add_text(str text)

        добавляет текст и возвращает :py:class:`Text`


    .. py:method:: clear()

        очищает


.. py:class:: Text

    текст


    .. py:attribute:: bold 

        текст жирный


    .. py:attribute:: style 

        стиль текста 
    
    
InlineShape
-----------

.. py:class:: docx.shape.InlineShape(inline)


    .. py:attribute:: height
    .. py:attribute:: type

        WD_INLINE_SHAPE

    .. py:attribute:: width


InlineShapes
------------

.. py:class:: docx.parts.document.InlineShapes(body_elem, parent)


    .. py:method:: add_picture(str path, run)


Length
------

.. py:class:: docx.shared.Length

    .. py:attribute:: cm
    .. py:attribute:: wmu
    .. py:attribute:: inches
    .. py:attribute:: mm
    .. py:attribute:: twips


Inches
------

.. py:class:: docx.shared.Inches


Cm
--

.. py:class:: docx.shared.Cm


Mm
--

.. py:class:: docx.shared.Mm


Emu
---

.. py:class:: docx.shared.Emu


WD_ALIGN_PARAGRAPH
------------------

.. py:attribute:: docx.enum.text.WD_ALIGN_PARAGRAPH

    .. py:attribute:: LEFT
    .. py:attribute:: CENTER
    .. py:attribute:: RIGHT
    .. py:attribute:: JUSTIFY
    .. py:attribute:: DISTRIBUTE
    .. py:attribute:: JUSTIFY_MED
    .. py:attribute:: JUSTIFY_HI
    .. py:attribute:: JUSTIFY_LOW
    .. py:attribute:: THAI_JUSTIFY


WD_ORIENTATION
--------------

.. py:attribute:: docx.enum.section.WD_ORIENTATION

    .. py:attribute:: PORTRAIT
    .. py:attribute:: LANDSCAPE


WD_SECTION_START
----------------

.. py:attribute:: docx.enum.section.WD_SECTION_START

    .. py:attribute:: CONTINUOUS
    .. py:attribute:: NEW_COLUMN
    .. py:attribute:: NEW_PAGE
    .. py:attribute:: EVEN_PAGE
    .. py:attribute:: ODD_PAGE


WD_UNDERLINE
------------

.. py:attribute:: WD_UNDERLINE

    .. py:attribute:: NONE
    .. py:attribute:: SINGLE
    .. py:attribute:: WORDS
    .. py:attribute:: DOUBLE
    .. py:attribute:: DOTTED
    .. py:attribute:: THICK
    .. py:attribute:: DASH
    .. py:attribute:: DOT_DASH
    .. py:attribute:: DOT_DOT_DASH
    .. py:attribute:: WAVY
    .. py:attribute:: DOTTED_HEAVY
    .. py:attribute:: DASH_HEAVY
    .. py:attribute:: DOT_DASH_HEAVY
    .. py:attribute:: DOT_DOT_DASH_HEAVY
    .. py:attribute:: WAVY_HEAVY
    .. py:attribute:: DASH_LONG
    .. py:attribute:: WAVY_DOUBLE
    .. py:attribute:: DASH_LONG_HEAVY

::

    from docx import Document
    from docx.shared import Inches

    document = Document()

    document.add_heading('Document Title', 0)

    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True

    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='IntenseQuote')

    document.add_paragraph(
        'first item in unordered list', style='ListBullet'
    )
    document.add_paragraph(
        'first item in ordered list', style='ListNumber'
    )

    document.add_picture('monty-truth.png', width=Inches(1.25))

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for item in recordset:
        row_cells = table.add_row().cells
        row_cells[0].text = str(item.qty)
        row_cells[1].text = str(item.id)
        row_cells[2].text = item.desc

    document.add_page_break()

    document.save('demo.docx')