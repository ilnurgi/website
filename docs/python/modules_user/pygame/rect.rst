.. py:module:: pygame


Rect
----

.. py:class:: Rect(x, y, w, h)


    .. py:attribute:: bottom

        Координата нижней части

        .. code-block:: py

            screen_size.bottom
            # 100


    .. py:attribute:: center

        Координата центра по оси х и y

        .. code-block:: py

            screen_size.center
            # (50, 50)


    .. py:attribute:: centerx

        Координата центра по оси х

        .. code-block:: py

            screen_size.centerx
            # 50


    .. py:attribute:: centery

        Координата центра по оси y

        .. code-block:: py

            screen_size.centery
            # 50


    .. py:function:: collidepoint(point1, point2)

        Возвращет булево, пересекается ли область с точкой

        .. code-block:: py

            play_button.rect.collidepoint(mouse_x, mouse_y)


    .. py:attribute:: left

        Координата левой части

        .. code-block:: py

            screen_size.left
            # 0


    .. py:attribute:: right

        Координата правой части

        .. code-block:: py

            screen_size.right
            # 100


    .. py:attribute:: top

        Координата верхней части

        .. code-block:: py

            screen_size.top
            # 0