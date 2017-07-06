.. py:module:: pygame.sprite

sprite
======


groupcollide
------------

.. py:function:: groupcollide(group1, group2, remove_sprite_1, remove_sprite_2)

    Возвращает словарь, коллизии групп, где ключ - спрайт из второй группы,
    значение - спрайт из первой группы

    .. code-block:: py

        collisions = sprite.groupcollide(some_group1, some_group2, True, True)


spritecollideany
----------------

.. py:function:: spritecollideany(sprite, group)

    Возвращает спрайт из группы, с кем пересекается спрайт из аргумента

    .. code-block:: py

        sprite = spritecollideany(some_sprite, some_group)


Group
-----

.. py:class:: Group()

    Группа объектов

    .. code-block:: py

        some_group = Group()


    .. py:method:: add(sprite)

        Добавляет элемент в группу

        .. code-block:: py

            some_group.add(some_sprite)


    .. py:method:: copy()

        Возвращает копию списка спрайтов группы

        .. code-block:: py

            for sprite in some_group.copy():
                some_group.remove(sprite)


    .. py:method:: draw(screen)

        Отрисовывает группу на экране, у каждого спрайта должно быть поле rect

        .. code-block:: py

            some_group.draw(screen)


    .. py:method:: empty()

        Удаляет все спрайты

        .. code-block:: py

            some_group.empty()


    .. py:method:: remove(sprite)

        Удаляет элемент из группы

        .. code-block:: py

            some_group.remove(sprite)


    .. py:method:: sprites()

        Возвращает список спрайтов

        .. code-block:: py

            for sprite in some_group.sprites():
                sprite.update()


Sprite
------

.. py:class:: Sprite()

    Спрайт для группировки

    .. py:attribute:: rect

        Позиция спрайта, :py:class:`Rect`