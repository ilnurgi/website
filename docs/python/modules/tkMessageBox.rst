.. py:module:: tkMessageBox

tkMessageBox
============

Модуль диалоговых окон


.. py:method:: askokcancel(title, message)

    Отображает информационное окно с вопросом и с выбором Да/Отмена.

    .. code-block:: py

        if askokcancel("Exit", "Are you sure?"):
            pass


.. py:method:: askquestion(title, message)

    Отображает информационное окно с вопросом и с выбором Да/Нет.

    .. code-block:: py

        if askquestion("Exit", "Are you sure?")
            pass


.. py:method:: askyesno(**kwargs)


.. py:method:: askretrycancel(**kwargs)


.. py:method:: showerror(title, message)

    Отображает информационное окно с ошибкой

    .. code-block:: py

        showerror(u'Error', u'Could not open file')


.. py:method:: showinfo(title, message)

    Отображает информационное окно

    .. code-block:: py

        showinfo(u'Information', u'Could not open file')


.. py:method:: showwarning(title, message)

    Отображает информационное окно, с предупреждением

    .. code-block:: py

        showwarning(u"Warning", u"Deprecated function call")
