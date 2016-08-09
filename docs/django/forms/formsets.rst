Наборы форм
===========

inlineformset_factory
---------------------

.. py:method:: django.forms.models.inlineformset_factory(**kwargs)

    Фабрика набора форм для дочерних моделей модели

    * parent_model - родительская модель

    * model - дочерняя модель, по которой формируется набор форм

    * form - класс формы, которая будет использоватся для ввода данных.
      По умолчанию :py:class:`django.forms.models.ModelForm`

    * formset - =BaseInlineFormSet,

    * fk_name - =None,

    * fields - список полей модели, которые будут в одной форме

    * exclude - список полей модели, которые не будут в одной форме

    * extra - максимальное количество выводимых пустых форм для создания новых записей,
      по умолчанию 3

    * can_order - булево,  пользователь может сортировать записи

    * can_delete - булево, пользователь может удалить записи

    * max_num - максимальное количество форм в наборе, по умолчанию 1000

    * formfield_callback - =None,

    * widgets - =None,

    * validate_max - булево, количество форм в наборе не должно быть больше max_num

    * localized_fields - =None,

    * labels - словарь, полей форм, с надписями

    * help_texts - словарь, полей форм, с дополнительным текстом

    * error_messages - словарь, полей форм с текстом сообщений

    * min_num - =None,

    * validate_min - =False

    .. code-block:: py

        # formset.py

        from django.forms.models import inlineformset_factory
        from .models import SomeModel, ParentModel

        SomeFormSet = inlineformset_factory(ParentModel, SomeModel)

    .. code-block:: py

        # views.py

        def some_view(request):

            instance = ParentModel.objects.get()
            formset = SomeFormSet(instance=instance)

            if formset.is_valid():
                formset.save()


modelformset_factory
--------------------

.. py:method:: django.forms.models.modelformset_factory(**kwargs)

    Фабрика набора форм для модели

    * model - модель, по которой формируется набор форм

    * form - класс формы, которая будет использоватся для ввода данных.
      По умолчанию :py:class:`django.forms.models.ModelForm`

    * formfield_callback - =None,

    * formset - =BaseModelFormSet,

    * extra - максимальное количество выводимых пустых форм для создания новых записей,
      по умолчанию 1

    * can_delete - булево, пользователь может удалить записи

    * can_order - булево,  пользователь может сортировать записи

    * max_num - максимальное количество форм в наборе, по умолчанию 1000

    * fields - список полей модели, которые будут в одной форме

    * exclude - список полей модели, которые не будут в одной форме

    * widgets - =None,

    * validate_max - булево, количество форм в наборе не должно быть больше max_num

    * localized_fields - =None,

    * labels - словарь, полей форм, с надписями

    * help_texts - словарь, полей форм, с дополнительным текстом

    * error_messages - словарь, полей форм с текстом сообщений

    * min_num - =None,

    * validate_min - =False

    .. code-block:: py

        # formset.py

        from django.forms.models import modelformset_factory
        from .models import SomeModel

        SomeFormSet = modelformset_factory(SomeModel)

        formset = SomeFormSet(queryset=SomeModel.objects.all())

    .. code-block:: py

        # views.py

        def some_view(request):

            formset = SomeFormSet(request.POST, request.FILES)

            if formset.is_valid():
                formset.save()

    .. code-block:: html

        <form>
            {{ formset.as_p }}
            {{ formset.can_order }}
            {{ formset.can_delete }}
        </form>

    .. code-block:: html

        <form>
            {{ formset.management_form }}
            {% for form in formset %}
                {{ form.as_p }}
                {{ form.ORDER }}
                {{ form.DELETE }}
            {% endfor %}
        </form>

