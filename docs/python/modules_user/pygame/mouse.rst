.. py:module:: pygame.mouse

mouse
=====

get_pos
-------

.. py:method:: get_pos()

    Возвращает кортеж, позиции курсора мыши

    .. code-block:: py

        mouse_x, mouse_y = mouse.get_pos()


set_visible
-----------

.. py:function:: set_visible(visible)

    Задает видимость курсору

    .. code-block:: py

        # скрываем курсор
        mouse.set_visible(False)