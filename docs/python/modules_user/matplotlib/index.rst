.. py:module:: matplotlib

matplotlib
==========

.. toctree::
    :maxdepth: 1

    pyplot
    figure
    axes


rcParams
--------

.. py:attribute:: rcParams

    :py:class:`matplotlib.RcParams` типа словаря, стандартные свойства библиотеки

    .. code-block:: py

        rcParams['figure.figsize']
        # [8.0, 6.0]

    * agg.path.chunksize

    * axes.axisbelow

    * axes.edgecolor

    * axes.facecolor

    * figure.figsize - размеры сохраняемых изображений, по умолчанию [8.0, 6.0]

    * interactive - булево, интерактивный режим

    * line.linecolor - цвет линии

    * line.linewidth - ширина линии

    * numerix -

    * savefig.edgecolor - цвет граней при сохранений

    * savefig.facecolor -

    * savefig.dpi - количество точек на дюйм сохраняемых изображений, по умолчанию 100


rc()
----

.. py:function:: rc(params)

    Задает множественные настройки

    .. code-block:: py

        rc(('figure', 'savefig'), facecolor='r')
        # эквивалентно
        # mpl.rcParam['figure.facecolor'] = 'r'
        # mpl.rcParam['savefig.facecolor'] = 'r'

        mpl.rc('line', linewidth=4, linecolor='b')
        # эквивалентно
        # mpl.rcParam['line.linewidth'] = 4
        # mpl.rcParam['line.linecolor'] = 'b'


rcdefaults()
------------

.. py:function:: rcdefaults()

    Востанавливает стандартные настройки


use()
-----

.. py:function:: use(backend)

    Включает использование бакенда

    * mode - режим

        * Agg - наилучший режим для сохранения изображений в png

            Используется для рендера изображений без UI

        * GTKAgg - GTK UI

        * TkAgg - tkinter

    .. code-block:: py

        use('Agg')


Конфигурационный файл
---------------------

Параметры конфигурационного файла доступны в :py:attr:`rcParams`

* /etc/matplotlibrc - глобальгый конфигурационный файл для linux систем

* $HOME/.matplotlib/matplotlibrc - пользовательский конфигурационный файл
  для linux систем

* C:\Documents andSettings\username\.matplotlib - пользовательский
  конфигурационный файл для windows систем
