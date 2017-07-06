.. py:module:: case

case
====


TestCase
--------

.. py:class:: TestCase

    базовый класс для тестов, запускаемые тесты должны начинаться со слова `test`

    .. py:method:: setUp()

        Вызывается для выполнения настроек, перед вызовом любых методов тестирования.

    .. py:method:: tearDown()

        Вызывается для выполнения заключительных действий после выполнения всех тестов.

    .. py:method:: assert(expr, [msg])

        проверяет `expr` на `False`

    .. py:method:: assertEqual(x, y, [msg])

        сравнивает `x`, `y`


    .. py:method:: assertIsInstance(x, y[, msg])

        Проверяет, является ли объект экземпляром класса

        .. code-block:: py

            self.assertIsInstance(a, b, 'some msg')


    .. py:method:: assertNotEqual(x, y, [msg])

        сравнивает `x`, `y`

    .. py:method:: assertAlmostEqual(x, y, [places, msg])

        сравнивает `x`, `y` c точностью до `places`

    .. py:method:: assertNotAlmostEqual(x, y, [places, msg])

        сравнивает `x`, `y` c точностью до `places`

    .. py:method:: assertRaises(exc, calable, *args)

        проверяет что `calable` вызывает исключение `exc`, `args` передаются в `calable`

    .. py:method:: failUnless(expr, [msg])

        проверяет `expr` на `False`

    .. py:method:: failUnlessEqual(x, y, [msg])

        сравнивает `x`, `y`

    .. py:method:: failAlmostEqual(x, y, [places, msg])

        сравнивает `x`, `y` c точностью до `places`

    .. py:method:: failUnlessNotEqual(x, y, [msg])

        сравнивает `x`, `y`

    .. py:method:: failNotAlmostEqual(x, y, [places, msg])

        сравнивает `x`, `y` c точностью до `places`

    .. py:method:: failUnlessRaises(exc, calable, *args)

        проверяет что `calable` вызывает исключение `exc`, `args` передаются в `calable`

    .. py:method:: failIf(expr, [msg])

        если `expr` == `True`, то ошибка

    .. py:method:: fail([msg])

        возбуждает ошибку

    .. py:attribute:: failureException

        хранит последнее исключение теста


expectedFailure
---------------

.. py:method:: expectedFailure()

    Декоратор, ожидает что метод завершится с ошибкой

    .. code-block:: py

        @expectedFailure
        def test_1(self):
            """
            """

skip
----

.. py:method:: skip()

    Декоратор для пропускания тестов

    .. code-block:: py

        @skip('message')
        def test_1(self):
            """


            """