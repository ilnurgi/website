Поля формы
==========


BooleanField
------------

.. py:class:: django.forms.BooleanField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля

    .. code-block:: py

        update = forms.BooleanField(
            required=False,
            initial=False,
            widget=forms.HiddenInput)


CharField
---------

.. py:class:: django.forms.CharField(**kwargs)

    Текстовое поле ввода

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * max_length - число, максимальная длина значения элемента

    * mix_length - число, минимальная длина значения элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля

    .. code-block:: py

        name = forms.CharField(max_length=25)

        comments = forms.CharField(required=False, widget=forms.Textarea)


ChoiceField
-----------

.. py:class:: django.forms.ChoiceField(**kwargs)


    * choices - список доступных значений

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


DateField
---------

.. py:class:: django.forms.DateField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * input_formats - список форматов значений

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


DateTimeField
-------------

.. py:class:: django.forms.DateTimeField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * input_formats - список форматов значений

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


EmailField
----------

.. py:class:: django.forms.EmailField(**kwargs)

    Поле ввода для email

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * max_length - число, максимальная длина значения элемента

    * mix_length - число, минимальная длина значения элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля

    .. code-block:: py

        email = forms.EmailField()


FileField
---------

.. py:class:: django.forms.FileField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


FilePathField
-------------

.. py:class:: django.forms.FilePathField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


FloatField
----------

.. py:class:: django.forms.FloatField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * max_value - максимальное значение

    * min_value - максимальное значение

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


GenericIPAddressField
---------------------

.. py:class:: django.forms.GenericIPAddressField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


IntegerField
------------

.. py:class:: django.forms.IntegerField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * max_value - максимальное значение

    * min_value - максимальное значение

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


ImageField
----------

.. py:class:: django.forms.ImageField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


IPAddressField
--------------

.. py:class:: django.forms.IPAddressField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


ModelChoiceField
----------------

.. py:class:: django.forms.ModelChoice(**kwargs)

    * empty_label - текст, пустого поля

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * queryset - набор записей, из которой будут взяты записи для выбора

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


SlugField
---------

.. py:class:: django.forms.SlugField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


TimeField
---------

.. py:class:: django.forms.TimeField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * input_formats - список форматов значений

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля


TypedChoiceField
----------------

.. py:class:: django.forms.TypedChoiceField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля

    .. code-block:: py

        quantity = forms.TypedChoiceField(
            choices=[(i, str(i)) for i in range(1, 21)],
            coerce=int)


URLField
--------

.. py:class:: django.forms.URLField(**kwargs)

    * error_messages - словарь сообщений для кодов ошибок (required, min_length,
      max_length, invalid_choice, invalid, min_value, max_value)

        .. code-block:: py

            Field(
                error_messages={
                    'error_code': 'text',
                },
            )

    * help_text - строка, дополнительный текст для элемента

    * initial - начальное значение поля

    * label - строка, текст надписи для элемента

    * max_length - число, максимальная длина значения элемента

    * mix_length - число, минимальная длина значения элемента

    * required - булево, поле обязательное

    * validators - список функции, валидаторы значения

    * widget - ссылка на виджет поля