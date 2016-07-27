Формы
=====


Form
----

.. py:class:: django.forms.Form()

    Базовая форма

    .. py:attribute:: cleaned_data

        Данные формы

    .. py:attribute:: is_bound

        Возвращает булево, заполнена ли форма

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

    .. py:method:: is_valid()

        Возвращает булево, валидные ли данным на форме

    .. py:method:: save(commit=True)

        Сохраняет объект в БД и возвращает его


ModelForm
---------

.. py:class:: django.forms.ModelForm()

    Форма по модели

    .. code-block:: py

        class CommentForm(forms.ModelForm):
            class Meta:
                model = Comment
                fields = ('name', 'email')
                widgets = {
                    'url': forms.HiddenInput,
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