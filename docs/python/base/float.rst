float
=====

Вещественное число.

.. py:class:: float(obj)

    Для точных расчетов необходимо использователь модуль :py:mod:`decimal`
    или модуль :py:mod:`fractions` для рациональных чисел.

    .. code-block:: py

        10.
        # 10.

        11E20
        # 11E20

        2.5e-12
        # 2.5e-12

        0.3 - 0.1 - 0.1 - 0.1
        # -2.7755575615628914е-17

    .. code-block:: py

        float(7)
        # 7.0

        float("7.1")
        # 7.1

        float("Infinity")
        # inf

        float("-inf")
        # -inf

        float("Infinity") + float ("-inf")
        # nan