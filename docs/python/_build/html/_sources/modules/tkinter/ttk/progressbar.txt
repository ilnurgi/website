Progressbar
===========

.. py:class:: Progressbar(widget, **kwargs)

    Виджет, прогрессбар

    :param widget: родительский виджет
    :param int height: длина
    :param int maximum: максимум пунктов в виджете

    .. py:method:: start([time])

        Запускает прогрессбар

        :param int time: интервал между загрузками, мс


    .. py:method:: step()

        Делает шаг в прогрессбаре


    .. py:method:: stop()

        Останавливает загрузку

