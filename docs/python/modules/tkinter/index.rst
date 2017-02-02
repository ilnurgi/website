.. py:module:: tkinter

tkinter
=======

Кроссплатформенная библиотека для построения графического интерфейса

Tkinter (от англ. tk interface) - это графическая библиотека,
позволяющая создавать программы с оконным интерфейсом.

Эта библиотека является интерфейсом к популярному языку программирования и
инструменту создания графических приложений tcl/tk.

Tkinter, как и tcl/tk, является кроссплатформенной библиотекой и
может быть использована в большинстве распространённых операционных систем (Windows, Linux, Mac OS X и др.).

Tkinter является событийно-ориентированной библиотекой.
В приложениях такого типа имеется главный цикл обработки событий.

.. versionadded:: 3.x

   Библиотека переименована в соответствии с PEP8 в tkinter (с маленькой буквы).


.. code-block:: py

    # для версии python 2.7 и ниже
    import Tkinter

.. code-block:: py

    # для версии python 3.0 и выше
    import tkinter


Базовые объекты:

.. toctree::
    :maxdepth: 1

    TK
    constants
    misk
    base_widget
    widget
    xview
    yview
    wm


Виджеты:

.. toctree::
    :maxdepth: 1

    button
    checkbutton
    entry
    frame
    label
    listbox
    message
    panedwindow
    radiobutton
    scale
    text
    toplevel
    scrollbar

    base
    vars
    canvas

    event
    labelframe
    menu
    menubutton
    optionmenu
    spinbox
    colorchooser
    filedialog
    messagebox
    simpledialog


Работа с изображениями

.. toctree::
    :maxdepth: 1

    image
    bitmapimage
    photoimage
