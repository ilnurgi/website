.. py:module:: matplotlib.figure

figure
======

Figure()
--------

.. py:class:: Figure(**kwargs)

    Фигура

    * figsize - кортеж размера фигуры, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.figsize

    * dpi - количесвто точек на дюйм, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.dpi

    * facecolor - цвет фона фигуры, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.facecolor

    * edgecolor - цвет границ фигуры, по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.edgecolor

    * linewidth - ширина линии фигуры, по умолчанию 0.0

    * frameon - по умолчанию None

    * subplotpars - по умолчанию None

    * tight_layout - по умолчанию задано в
      :py:attr:`matplotlib.rcParams` -> figure.autolayout

    .. code-block:: py

        fig = matplotlib.pyplot.figure()


    .. py:method:: add_subplot(numrows, numcols, fignum)

        Добавляет объект для рисования графика по укзанным координатам

        Вовзвращает :py:class:`matplotlib.axes.Axes`, объект для рисования графиков.

        .. code-block:: py

            ax = fig.add_subplot(111)
            ax1 = fig.add_subplot(1, 1, 1)
            ax2 = fig.add_subplot(1, 1, 1, axisbg='r', projection='polar')


    .. py:method:: text()

        Аналог :py:func:`matplotlib.pyplot.figtext`


    .. py:method:: suptitle()

        Аналог :py:func:`matplotlib.pyplot.suptitle`


