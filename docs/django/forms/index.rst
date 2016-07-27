Формы
=====

.. code-block:: py

    # forms.py
    # описание форм

    from django import forms

    class DetailsForm(forms.Form):

        name = forms.CharField(max_length=100)
        age = forms.IntegerField()

    class DetailsForm2(forms.Form):

        name = forms.CharField(max_length=100)
        age = forms.IntegerField()

        def __init__(self, *args, **kwargs):
            upgrade = kwargs.pop('upgrade', False)

            super().__init__(*args, **kwargs)

            if upgrade:
                self.fields["upgrade"] = forms.BooleanField(label="Upgrade")

    class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

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
            {{ field.errors }}
            {{ field.label_tag }}
            {{ field }}
        {% endfor %}
        <input type="submit">
    </form>

.. toctree::
    :maxdepth: 1

    forms
    fields
    widgets