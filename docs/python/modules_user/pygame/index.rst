pygame
======

Содержание:

.. toctree::
   :maxdepth: 1


.. py:class:: Screen((height, width))

    .. code-block:: py

        screen = pygame.Screen((400, 400)


.. py:function:: event.get()

.. code-block:: py

    import pygame
    window = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Hello World')

    # pygame.key.set_repeat(a, b) a - задержка перед первым дублированием, b - задержка между остальными дублированиями
    # pygame.mouse.get_pos()
    # pygame.mouse.set_visible(True/False)

    screen = pygame.Screen((400, 400)

    square = pygame.Surface((40, 40))
    square.fill((0, 255, 0))

    bitmap = pygame.image.load(filename)
    bitmap.set_colorkey((0, 0, 0))

    x = 0
    square_go_right = True

    done = True
    while done:

        for e in pygame.event.get():
            # QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN,
            # JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBYTTONUP, JOYBUTTONDOWN,
            # VIDEORESIZE, VIDEOEXPOSE, USEREVENT
            if e.type == pygame.QUIT:
                done = False
                if e.key == pygame.K_LEFT:
                    pass

        if square_go_right is True:
            x += 1
            if x > 360:
                x = 360


        screen.fill((0,255,0))
        screen.blit(square, (x, 0))

        window.blit(screen, (400, 400))
        pygame.display.flip()
        pygame.time.delay(100)

    def intersect(s1_x, s1_y, s2_x, s2_y):
        if ((s1_x>s2_x-40) and (s1_x<s2_x+40) and
            (s1_y>s2_y-40) and (s1_y<s2_y+40)):
            return 1
        else:
            return 0
