.. py:module:: mock

mock
====

Mock
----

.. py:class:: Mock([return_value])

    Простой мок класс

    * return_value - возвращаемое значение

    .. code-block:: py

        mock_obj = Mock()
        mock_obj_foo = mock_obj.foo

    .. py:class:: py

        class A:

            def get_x(self):
                return 100

            def get_y(self):
                return 100

            def compute(self):
                return self.get_x() + self_get_y()

        a = A()
        mock_obj2 = Mock()

        a.get_x = mock_obj2.get_x
        a.get_y = mock_obj2.get_y

        a.get_x.return_value = 200
        a.get_y.return_value = 200

        a.compute()
        # 400

        mock_obj2.mock_calls == [call.get_x(), call.get_y()]

    .. code-block:: py

        # патчим input
        __builtins__.input = Mock(return_value=100)
        input()
        # 100

        # если какой-то модуль не доступен, мокаем и его
        import sys
        sys.modules['some_module'] = Mock()


    .. py:attribute:::: mock_calls

        Список, который хранит вызванные объекты

        .. code-block:: py

            mock_obj.mock_calls
            # []

            mock_obj_foo()

            mock_obj.mock_calls
            # [call.foo()]

    .. py:attribute:: return_value

        Атрибут хранит значение, которое вернет мок объект при уго вызове


MagicMock
---------

.. py:class:: MagicMock()

    Наследник :py:class:`Mock`,
    расширенный реализацией магических методово питона


patch
-----

.. py:method:: patch(target, new=MagicMock)

    Возвращает новый патченный объект

    .. code-block:: py

        with patch('__main__.A.get_x', new=Mock(return_value=500)):
            a = A()
            a.compute()
            # 600

        with patch('__main__.A.get_x') as mock_A_get_x:
            mock_A_get_x.return_value = 400

            a = A()
            a.compute()
            # 600

