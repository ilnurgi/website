taggit - теги
=============

.. code-block:: py

    # settings.py

    INSTALLED_APPS = (
        ...
        'taggit',
    )

.. code-block:: py

    # models.py

    from taggit.managers import TaggableManager

    class SomeModel(models.Model):

        tags = TaggableManager()

.. code-block:: py

    # forms.py

    from taggit.forms import TagField

    class SomeForm(forms.ModelForm):

        class Meta:
            model = SomeModel

        tags = TagField(label="tags")

.. code-block:: py

    # views.py

    SomeModel.objects.filter(tags__name='python')
    SomeModel.objects.filter(tags__name__in=('python', 'django')).distinct()


TaggableManager
---------------

.. py:class:: taggit.managers.TaggableManager(blank, verbose_name, help_text)

    Менеджер, реализующий возможность работы с тегами.

    .. py:method:: add(*tag_names)

        Добавляет теги

        .. code-block:: py

            record.tags.add("python")
            record.save()

    .. py:method:: clear()

        Удаляет все теги

        .. code-block:: py

            record.tags.clear()
            record.save()

    .. py:method:: remove(*tag_names)

        Удаляет теги

        .. code-block:: py

            record.tags.remove("python", "django")
            record.save()

    .. py:method:: set(*tag_names)

        Удаляет все теги и записывает новые

        .. code-block:: py

            record.tags.set("python")
            record.save()






TagField
--------

.. py:class:: taggit.forms.TagField(label)

    Поле для формы

    * если введенная строка не содержит запятых, двойных кавычек,
      то каждое слово это отдельный тег

    * строки в двойных кавчках, считаются отдельными тегами

    * строки, разделенные запятыми считаются отдельными тегами


TagWidget
---------

.. py:class:: taggit.forms.TagWidget()

    HTML виджет

