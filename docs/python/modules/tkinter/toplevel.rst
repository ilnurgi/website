TopLevel - виджет, окно верхнего уровня
=======================================


.. py:class:: TopLevel(**kwargs)

    Окно верхнего уровня

    Наследник :py:class:`BaseWidget`, :py:class:`WM`

    .. code-block:: py

        # модальное окно
        modal_window = TopLevel(root)
        Button(modal_window, command=lambda: modal_window.destroy())

        modal_window.focus_set()
        modal_window.grab_set()
        modal_window.wait_window()

        modal_window.mainloop()
