Сообщения
=========

.. code-block:: py

    from django.contrib import messages

    def some_view(request):

        # ...
        messages.success(request, 'Profile updated successfully')
        # ...


.. code-block:: html

    {% if messages %}
        <ul class="messages">
            {% for message in messages %}
                <li class="{{ message.tags }}">
                    {{ message|safe }}
                    <a href="#" class="close">✖</a>
                </li>
            {% endfor %}
        </ul>
    {% endif %}