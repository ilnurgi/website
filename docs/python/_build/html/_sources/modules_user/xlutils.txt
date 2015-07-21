.. py:module:: xlutils

xlutils - инструмент для работы с xls файлами
=============================================

`Страничка проекта`_

`Скачать`_

`Официальная документация`_

`GitHub`_

.. _Страничка проекта: http://www.python-excel.org/
.. _Скачать: http://pypi.python.org/pypi/xlutils
.. _Официальная документация: http://pythonhosted.org/xlutils/
.. _GitHub: https://github.com/python-excel/xlutils

Модуль с утилитами, для работы с Excel файлами

copy
----
    .. py:module:: copy
    
    Функции из этого модуля, копируют объект :py:class:`xlrd.Book` в объект :py:class:`xlwt.Workbook`

    >>> from os.path import join
    >>> from xlrd import open_workbook
    >>> rb = open_workbook(join(test_files,'testall.xls'), formatting_info=True, on_demand=True)
    >>> rb.sheet_by_index(0).cell(0,0).value
    u'R0C0'
    >>> rb.sheet_by_index(0).cell(0,1).value
    u'R0C1'

    >>> from xlutils.copy import copy
    >>> wb = copy(rb)

    >>> wb.get_sheet(0).write(0,0,'changed!')
    >>> wb.save(join(temp_dir.path,'output.xls'))
    >>> temp_dir.listdir()
    output.xls

    >>> rb = open_workbook(join(temp_dir.path,'output.xls'))
    >>> rb.sheet_by_index(0).cell(0,0).value
    u'changed!'
    >>> rb.sheet_by_index(0).cell(0,1).value
    u'R0C1'

    .. note:: Рекомендуется использовать pass on_demand=True в open_workbook() это экономит память

display
-------
    
    .. py:module:: display

    Модуль содержит методы, для безопасного отображения информации из книги.

    .. py:method:: quoted_sheet_name(sheet_name, encoding='ascii')
        
        Возвращает строку, название листа.

        >>> from xlutils.display import quoted_sheet_name
        >>> quoted_sheet_name(u'Price(\xa3)','utf-8')
        'Price(\xc2\xa3)'

        >>> quoted_sheet_name(u'My Sheet')
        "'My Sheet'"

        >>> quoted_sheet_name(u"John's Sheet")
        "'John''s Sheet'"

    .. py:method:: cell_display(cell, datemode=0, encoding='ascii')
        
        Возвращает строковое представление ячейки

        >>> import xlrd
        >>> from xlrd.sheet import Cell
        >>> from xlutils.display import cell_display

        >>> cell_display(Cell(xlrd.XL_CELL_EMPTY, ''))
        'undefined'

        >>> cell_display(Cell(xlrd.XL_CELL_BLANK, ''))
        'blank'

        >>> cell_display(Cell(xlrd.XL_CELL_NUMBER, 1.2))
        'number (1.2000)'

        >>> cell_display(Cell(xlrd.XL_CELL_BOOLEAN, 0))
        'logical (FALSE)'

        >>> cell_display(Cell(xlrd.XL_CELL_DATE, 36892.0))
        'date (2001-01-01 00:00:00)'

        >>> cell_display(Cell(xlrd.XL_CELL_DATE, 1.5))
        'date? (1.500000)'

        .. note:: To display dates correctly, make sure that datemode is passed and is taken from the datemode attribute of the xlrd.Book from which the cell originated as shown below:

        >>> wb = open_workbook(join(test_files,'date.xls'))
        >>> cell = wb.sheet_by_index(0).cell(0, 0)
        >>> cell_display(cell, wb.datemode)
        'date (2012-04-13 00:00:00)'

        >>> cell_display(Cell(xlrd.XL_CELL_TEXT,u'Price (\xa3)'))
        'text (Price (?))'

        >>> cell_display(Cell(xlrd.XL_CELL_TEXT,u'Price (\xa3)'), encoding='utf-8')
        'text (Price (\xc2\xa3))'

        >>> cell_display(Cell(xlrd.XL_CELL_ERROR, 0))
        'error (#NULL!)'

        >>> cell_display(Cell(xlrd.XL_CELL_ERROR, 2000))
        'unknown error code (2000)'

        >>> cell_display(Cell(69, 0))
        Traceback (most recent call last):
        ...
        Exception: Unknown Cell.ctype: 69

filter
------
    
    .. py:module:: filter

    .. py:class:: filter.BaseFilter
    
        Базовый фильтр, для последующих фильтров

    .. py:class:: BaseFilterInterface

        This is the filter interface that shows the correct way to call the next filter in the chain. The next attribute is set up by the :py:meth:`process()` function. It can make a good base class for a new filter, but subclassing BaseFilter is often a better idea!

cell(rdrowx, rdcolx, wtrowx, wtcolx)
This is called for every cell in the sheet being processed. This is the most common method in which filtering and queuing of onward calls to the next filter takes place.

Parameters: 
rdrowx – the index of the row to be read from in the current sheet.
rdcolx – the index of the column to be read from in the current sheet.
wtrowx – the index of the row to be written to in the current output sheet.
wtcolx – the index of the column to be written to in the current output sheet.
finish()
This method is called once processing of all workbooks has been completed.

A filter should call this method on the next filter in the chain as an indication that no further calls will be made to any methods or that, if they are, any new calls should be treated as new batch of workbooks with no information retained from the previous batch.

row(rdrowx, wtrowx)
This is called every time processing of a new row in the current sheet starts. It is primarily for copying row-based formatting from the source row to the target row.

Parameters: 
rdrowx – the index of the row in the current sheet from which information for the row to be written should be copied.
wtrowx – the index of the row in sheet to be written to which information should be written for the row being read.
set_rdsheet(rdsheet)
This is only ever called by a filter that wishes to change the source of cells mid-way through writing a sheet.

Parameters: rdsheet – the Sheet object from which cells from this point forward should be read from.
sheet(rdsheet, wtsheet_name)
This method is called every time processing of a new sheet in the current workbook starts.

Parameters: 
rdsheet – the Sheet object from which the new sheet should be created.
wtsheet_name – the name of the sheet into which content should be written.
start()
This method is called before processing of a batch of input. This allows the filter to initialise any required data structures and dispose of any existing state from previous batches.

It is called once before the processing of any workbooks by the included reader implementations.

This method can be called at any time. One common use is to reset all the filters in a chain in the event of an error during the processing of a rdbook.

Implementations of this method should be extremely robust and must ensure that they call the start() method of the next filter in the chain regardless of any work they do.

workbook(rdbook, wtbook_name)
This method is called every time processing of a new workbook starts.

Parameters: 
rdbook – the Book object from which the new workbook should be created.
wtbook_name – the name of the workbook into which content should be written.
    
    .. py:method:: process(reader, *chain)
        
        The driver function for the xlutils.filter module.

        It takes a chain of one reader, followed by zero or more filters and ending with one writer.

        All the components are chained together by the process() function setting their next attributes appropriately. The reader is then called with the first filter in the chain.