Сообщения
=========

Система уведомлений пользователей о событии

.. code-block:: py

    from django.contrib import messages

    def some_view(request):

        # ...
        messages.success(request, 'Some message')
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


add_message
-----------

.. py:method:: django.contrib.messages.add_message(request, level, message)

    Добавляет сообщение с указанным уровнем в ответ.

    .. code-block::

        message.add_message(
            request,
            message.SUCCESS
        )

debug
-----

.. py:method:: django.contrib.messages.debug(request, message)

    Добавляет отладочное сообщение


info
----

.. py:method:: django.contrib.messages.info(request, message)

    Добавляет информационное сообщение


success
-------

.. py:method:: django.contrib.messages.success(request, message)

    Добавляет сообщение об успешном выолнений опреации


warning
-------

.. py:method:: django.contrib.messages.warning(request, message)

    Добавляет сообщение с предупрежденеием


error
-----

.. py:method:: django.contrib.messages.error(request, message)

    Добавляет сообщение с ошибкой


SuccessMessageMixin
-------------------

.. py:class:: django.contrib.messages.views.SuccessMessageMixin()

    Миксин для предствалений, реализующий вывод сообщений

    .. py:attribute:: success_message

        Строка с текстом об успешном выполненном действий


Уровни сообщений
----------------

DEBUG
+++++

.. py:attribute:::: django.contrib.messages.DEBUG

    Отладочное сообщение


INFO
++++

.. py:attribute:::: django.contrib.messages.INFO

    Инофрмационное сообщение сообщение


SUCCESS
+++++++

.. py:attribute:::: django.contrib.messages.SUCCESS

    Сообщение об успешном выолнении опреации


WARNING
+++++++

.. py:attribute:::: django.contrib.messages.WARNING

    Предупреждение


ERROR
+++++

.. py:attribute:::: django.contrib.messages.ERROR

    Ошибка