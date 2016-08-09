Формы
=====

.. code-block:: py

    # forms.py
    # описание форм

    from django import forms

    class SomeForm(forms.Form):

        name = forms.CharField(max_length=100)
        age = forms.IntegerField()
        password = forms.CharField(widget=forms.PasswordInput)

    class DetailsForm2(forms.Form):

        def __init__(self, *args, **kwargs):
            upgrade = kwargs.pop('upgrade', False)

            super().__init__(*args, **kwargs)

            if upgrade:
                self.fields["upgrade"] = forms.BooleanField(label="Upgrade")

.. code-block:: py

    # обработка форм в представлениях

    from .forms import EmailPostForm

    def post(request, post_id):

        post = get_object_or_404(Post, id=post_id)

        if request.method == "POST":
            form = EmailPostForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
        else:
            form = EmailPostForm()

        return render(
            request,
            'index.html',
            {
                'post': post,
                'form': form,
            },
        )

.. code-block:: html

    <!-- отображение форм в шаблонах -->

    <form action="." method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>

    <form action="." method="post">
        {% csrf_token %}
        {% for field in form %}
            {{ field }}
            {{ field.errors }} - html-код, список ошибок поля
            {{ field.help_text }} - дополнительный текст
            {{ field.is_hidden }} - булево, поле скрыто
            {{ field.label }} - текст надписи
            {{ field.label_tag }} - html-код, записи
            {{ field.name }} - имя поля
        {% endfor %}
        <input type="submit">
    </form>


Form
----

.. py:class:: django.forms.Form()

    Базовая форма


    .. py:attribute:: cleaned_data

        Данные формы

    .. py:attribute:: is_bound

        Возвращает булево, заполнена ли форма

    .. py:attribute:: required_css_class

        Строка, название класса стиля обязательного поля формы

        .. code-block:: py

            class SomeForm(Form):

                required_css_class = 'required'

    .. py:attribute:: error_css_class

        Строка, название класса стиля поля формы с ошибкой

        .. code-block:: py

            class SomeForm(Form):

                error_css_class = 'error'

    .. py:method:: as_p()

        Возвращает строку, HTML форма используя параграфы p

        .. code-block:: py

            form.as_p()
            # <p><label ... /><input ... /></p>

    .. py:method:: as_table()

        Возвращает строку, HTML форма используя таблицы table

        .. code-block:: py

            form.as_p()
            # <tr><th><label ... /></th><td><input ... /></td></tr>

    .. py:method:: as_ul()

        Возвращает строку, HTML форма используя списки ul

        .. code-block:: py

            form.as_p()
            # <li><label ... /><input ... /></li>

    .. py:method:: clean()

        Валидирует всю форму.

        .. code-block:: py

            class SomeForm():

                def clean(self):
                    cd = super().clean()
                    if cd['password'] != cd['password2']:
                        raise forms.ValidationError('Passwords don\'t match.')
                    return cd

    .. py:method:: clean_some_field()

        Валидирует конкретное поле формы.

        .. code-block:: py

            class SomeForm():

                def clean_password2(self):
                    cd = self.cleaned_data
                    if cd['password'] != cd['password2']:
                        raise forms.ValidationError('Passwords don\'t match.')
                    return cd['password2']

    .. py:method:: hidden_fields()

        Возвращает список всех не видимых полей формы

    .. py:method:: is_valid()

        Возвращает булево, валидные ли данным на форме

    .. py:method:: save(commit=True)

        Сохраняет объект в БД и возвращает его

    .. py:method:: visible_fields()

        Возвращает список всех видимых полей формы


ModelForm
---------

.. py:class:: django.forms.ModelForm()

    Форма по модели, аналогичен форме :py:class:`django.forms.Form`,
    но автоматический работает с указанной моделью.

    .. code-block:: py

        class SomeForm(forms.ModelForm):
            class Meta:

                # модель, по которой будет строиться форма
                model = SomeModel

                # поля, которые должны быть в форме
                fields = ()

                # поля, которых не должно быть в форме
                exclude = ()

                # словарь, надписи для элементов
                labels = {
                    'field_name': 'label',
                }

                # словарь, вспомогательный текст для элементов
                help_texts = {
                    'field_name': 'help_text',
                }

                # словарь, виджеты для элементов
                widgets = {
                    'field_name': forms.HiddenInput,
                }

                # словарь сообщений для кодов ошибок
                # required, min_length, max_length, invalid_choice, invalid,
                # min_value, max_value
                error_messages = {
                    'field_name': {
                        'error_code': 'text',
                    },
                }


    .. code-block:: py

        class UserRegistrationForm(forms.ModelForm):

            password = forms.CharField(
                label='Password',
                widget=forms.PasswordInput,
            )
            password2 = forms.CharField(
                label='Repeat password',
                widget=forms.PasswordInput,
            )

            class Meta:
                model = User
                fields = ('username', 'first_name', 'email)

            def clean_password2(self):
                cd = self.cleaned_data
                if cd['password'] != cd['password2']:
                    raise forms.ValidationError('Passwords don\'t match.')
                return cd['password2']