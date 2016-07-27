Поля формы
==========


BooleanField
------------

.. py:class:: django.forms.BooleanField()

    .. code-block:: py

        update = forms.BooleanField(
            required=False,
            initial=False,
            widget=forms.HiddenInput)


CharField
---------

.. py:class:: django.forms.CharField()

    Текстовое поле ввода

    .. code-block:: py

        name = forms.CharField(max_length=25)

        comments = forms.CharField(required=False, widget=forms.Textarea)


EmailField
----------

.. py:class:: django.forms.EmailField()

    Поле ввода для email

    .. code-block:: py

        email = forms.EmailField()


TypedChoiceField
----------------

.. py:class:: django.forms.TypedChoiceField()

    .. code-block:: py

        quantity = forms.TypedChoiceField(
            choices=[(i, str(i)) for i in range(1, 21)],
            coerce=int)