.. py:module:: pygame

Screen
======

.. py:class:: Screen((height, width))

    .. code-block:: py

        screen = pygame.Screen((400, 400)


    .. py:module:: blit(surface, rect)

        Выводит изображение на экран

        .. code-block:: py

            screen.blit(image_surface, image_rect)


    .. py:module:: get_rect()

        Возвращает :py:class:`Rect`

        .. code-block:: py

            screen_rect = screen.get_rect()