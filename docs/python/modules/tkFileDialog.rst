.. py:module:: tkFileDialog

tkFileDialog - диалоговое окно выбора файла
===========================================


Диалоговые окна имеют следующие параметры:

* defaultextension

* filetypes - список кортежей, (label, pattern)

* initialdir - начальная директория

* initialfile - начальный файл 

* parent - родительское окно

* title - заголовок окна

* multiple - True|False множественный выбор

* mustexist - True|False выбор только существующей директории


.. py:class:: _Dialog()

    Наследник :py:class:`tkCommonDialog.Dialog`


.. py:class:: Directory()

    Диалоговое окно выбора директории

    Наследник :py:class:`tkCommonDialog.Dialog`


.. py:class:: Open(**kwargs)

    Диалоговое окно выбора файла

    Наследник :py:class:`_Dialog`

    * `master` - родительский виджет
    * `filetypes` - список кортежей, для фильтрации типов фалов

    ..  code-block:: py

        dlg = Open(
            master=root,
            filetypes=[('Python files', '*.py'), ('All files', '*')]
        fl = dlg.show()


.. py:class:: SaveAs()

    Диалоговое окно выбора файла для сохранения

    Наследник :py:class:`_Dialog`


.. py:function:: askdirectory(**kwargs)

    Создает диалоговое окно выбора папки и возвращает путь к выбранной папке

    .. code-block:: py

        dir_path = askdirectory()


.. py:function:: askopenfile(mode='r', **kwargs)

    Создает диалоговое окно выбора файла и возвращает открытый файловый объектов


.. py:function:: askopenfilename(**kwargs)

    Создает диалоговое окно выбора файла и возвращает имя выбранного файла


.. py:function:: askopenfilenames(**kwargs)

    Создает диалоговое окно выбора файлов и возвращает список имен выбранных файлов


.. py:function:: askopenfiles(mode='r', **kwargs)

    Создает диалоговое окно выбора файлов и возвращает список открытых файловых объектов


.. py:function:: asksaveasfile(mode='w', **kwargs)

    Создает диалоговое окно сохранения файла и возвращает открытый файловый объект


.. py:function:: asksaveasfilename(**kwargs)

    Создает диалоговое окно сохранения файла и возвращает имя нового файла
