.. py:module:: textwrap

textwrap
========

.. py:method:: fill(text, width=70)

    Возвращает новую строку,
    разделив строку переходами на новую строку с учетом ширины

    .. code-block:: py

        textwrap.fill('long long text', 10)
        # long long\ntext