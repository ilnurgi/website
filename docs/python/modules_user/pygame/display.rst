.. py:module:: pygame.display

display
=======


.. py:function:: flip()

    Отобразить последний отрисованный экран

    .. code-block:::: py

        display.flip()


.. py:function:: set_mode((higth, width))

    Возвращает экран/поверхность указанных размеров, :py:class:`pygame.Surface`

    .. code-block:: py

        window = display.set_mode((400, 400))


.. py:function:: set_caption(caption)

    Устанавливает заголовок окна

    .. code-block:: py

        display.set_caption(u'Hello PyGame')