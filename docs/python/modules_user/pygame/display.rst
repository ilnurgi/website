.. py:module:: pygame.display

display
=======


.. py:function:: flip()

    отображаем окно

    .. code-blog:: py

        pygame.display.flip()


.. py:function:: set_mode((higth, width))

    Возвращает экран указанных размеров

    .. code-blog:: py

        window = pygame.display.set_mode((400, 400))


.. py:function:: set_caption(caption)

    Устанавливает заголовок окна

    .. code-blog:: py

        pygame.display.set_caption(u'Hello PyGame')