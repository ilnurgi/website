.. py:module:: tkMessageBox

tkMessageBox
============

Модуль диалоговых окон


.. py:method:: askokcancel(**kwargs)

    Отображает информационное окно с вопросом и с выбором Да/Отмена.


.. py:method:: askquestion(**kwargs)

    Отображает информационное окно с вопросом и с выбором Да/Нет.

    * `title` - заголовок окна
    * `message` - сообщение

    .. code-block:: py

        askquestion(u"Question", u"Are you sure to quit?")


.. py:method:: askyesno(**kwargs)


.. py:method:: askretrycancel(**kwargs)


.. py:method:: showerror(**kwargs)

    Отображает информационное окно с ошибкой

    * `title` - заголовок окна
    * `message` - сообщение

    .. code-block:: py

        showerror(u'Error', u'Could not open file')


.. py:method:: showinfo(**kwargs)

    Отображает информационное окно

    * `title` - заголовок окна
    * `message` - сообщение

    .. code-block:: py

        showinfo(u'Information', u'Could not open file')


.. py:method:: showwarning(**kwargs)

    Отображает информационное окно, с предупреждением

    * `title` - заголовок окна
    * `message` - сообщение

    .. code-block:: py

        showwarning(u"Warning", u"Deprecated function call")
