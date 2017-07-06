.. py:module:: main

main
====


main
----

.. py:method:: main(defaultTest=None)

    Запускает выполнение тестов

    * defaultTest - название функции, которая вернет тестсюиты

    .. code-block:: py

        def suite():
            return SomeTestSuite()

        if __name__ == '__main__':
            main(defaultTest='suite')