Шаблоны
=======

.. code-block:: html

    <title>{{ title }}</title>

.. code-block:: html

    <div>{{ cats.0.name }}</div>

.. code-block:: html

    <!-- вывести текст без замены html символов, т.е. как есть -->
    {% autoescape on %}
        {{ some_html }}
    {% endautoescape %}

.. code-block:: html

    <!-- выключить шаблонизацию для учатска -->
    {% verbatim %}
        {{ some_html }}
    {% endverbatim %}

.. code-block:: html

    <!-- вывести первое непустое и не нулевое значение -->
    {% firstof val1 val2 val3 %}

.. code-block:: html

    {% with cat=good.category %}
        {{ cat.id }}
    {% endwith %}

.. code-block:: html

    {# коментарии #}

.. code-block:: html

    <script>
        var csrftoken = $.cookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        });
    </script>



Циклы
-----

.. code-block:: html

    <ul>
        {% for good in goods %}
            <li>{{ good.name }}</li>
            {{ forloop.counter }} - номер теущей итерации начиная с 1
            {{ forloop.counter0 }} - номер теущей итерации начиная с 0
            {{ forloop.revcounter }} - номер теущей итерации с конца, начиная с 1
            {{ forloop.revcounter0 }} - номер теущей итерации с конца, начиная с 0
            {{ forloop.first }} - булево, первая итерация
            {{ forloop.last }} - булево, последняя итерация
            {{ forloop.parentloop }} - родительский цикл
        {% empty %}
            <!-- блок исполнится если список пустой -->
            ...
        {% endfor %}
    </ul>

.. code-block:: html

    <!-- генератор, который возвращает новое значение при каждом обращении -->
    {% cycle 'normal' 'alternate' %}


Условия
-------

.. code-block:: html

    {% if good.id == 1 %}
        ...
    {% elif good.id == 2%}
        ...
    {% else %}
        ...
    {% endif %}

.. code-block:: html

    <!-- работает быстрее чем обычный if -->
    {% ifequal good.id 1 %}
        ...
    {% endifequal %}

.. code-block:: html

    <!-- работает быстрее чем обычный if -->
    {% ifnotequal good.id 1%}
        ...
    {% endifnotequal %}


Фильтры
-------

.. code-block:: html

    <!-- сложение -->
    {{ good.some_attr|add:2 }}

    <!-- первый символ в верхний регистр -->
    {{ good.some_attr|capfirst }}

    <!-- удаляет из строка указанную подстроку -->
    {{ good.some_attr|cut:"cut" }}

    <!-- дефолтное значение если значение пустое -->
    {{ good.some_attr|default:"default" }}

    <!-- дефолтное значение если значение None -->
    {{ good.some_attr|default_if_none:"0" }}

    <!-- проверяет, делится ли число на указанное без остатка -->
    {{ good.some_attr|devisibleby:"0" }}

    <!-- заменяте недопустимые символы html -->
    {{ good.some_attr|escape }}

    <!-- преобразует значение для javascript сценариев -->
    {{ good.some_attr|escapejs }}

    <!-- первый элемент списка -->
    {{ good.some_attr|first }}

Числа

.. code-block:: html

    <!-- округление -->
    {{ good.some_attr|floatformat:"0" }}
    <!-- 35 -->
    {{ good.some_attr|floatformat:"3" }}
    <!-- 35 -->
    {{ good.some_attr|floatformat:"-3" }}
    <!-- 35.000 -->

Дата и время

.. code-block:: html

    <!-- форматирует дату по формату -->
    {{ good.some_attr|date:"j.d.y" }}
    {{ good.some_attr|date:"date_format" }}

    {% if some_date|date:"L" %}
        високосный год
    {% endif %}

    <!-- форматирует время по формату -->
    {{ good.some_attr|time:"time_format" }}
    {{ good.some_attr|time:"G:i" }}

.. code-block:: html

    <!-- последний элемент списка -->
    {{ good.some_attr|last }}

    <!-- размер списка -->
    {{ good.some_attr|length }}

    <!-- помещает занчение в <p> и заменяет переводы каретки на <br> -->
    {{ good.some_attr|linebreaks }}

    <!-- заменяем перевод каретки на <br> -->
    {{ good.some_attr|linebreaksbr }}

    <!-- преобразует значение в нижний регистр -->
    {{ good.some_attr|lower }}

    <!-- возвращает случайное значение из указанных -->
    {{ good.some_attr|random }}

    <!-- отключает преобразование недопустимых символов html -->
    {{ good.some_attr|safe }}

    <!-- удаляет все html теги -->
    {{ good.some_attr|striptags }}

    <!-- срез списка -->
    {{ good.some_attr|slice:"1:5" }}

    <!-- преобразует все первые буквы слов в значений в верхний регистр -->
    {{ good.some_attr|title }}

    <!-- обрезает строку до указанных количеств символов -->
    {{ good.some_attr|truncatechars:"100" }}

    <!-- обрезает строку до указанных количеств слов -->
    {{ good.some_attr|truncatewords:"10" }}

    <!-- обрезает строку до указанных количеств слов с учетом html -->
    {{ good.some_attr|truncatewords_html:"10" }}

    <!-- преобразует в верхний регистр -->
    {{ good.some_attr|upper }}

    <!--  -->
    {{ good.some_attr|urlencode }}

    <!-- количество слов в знгачении -->
    {{ good.some_attr|wordcount }}

    <!-- если True - Yes, False - No, None - None -->
    {{ good.some_attr|yesno:"Yes,No,None" }}

.. code-block:: html

    <!-- примение группы фильтров для элементов -->
    {% filter linebreaksbr|striptags %}
        {{ good.some_attr1 }}
        {{ good.some_attr2 }}
    {% endfilter %}


Наследование и блоки шаблонов
-----------------------------

.. code-block:: html

    {% extends "base.html" %}

    {% include "_navbar.html" with active_link = "link2" %}

    {% block content %}
    {% endblock %}


Статика
-------

.. code-block:: html

    {% load staticfiles %}

    <link href="{% static "app.css" %}" rel="stylesheet">


Свои теги и фильтры
-------------------

.. code-block:: py

    # templatetags/blog_tags.py

    from django import template
    from django.utils.safestring import mark_safe

    import markdown

    register = template.Library()

    @register.simple_tag
    def total_posts():
        return 5

    @register.filter(name='markdown')
    def markdown_format(text):
        return mark_safe(markdown.markdown(text))

.. code-block:: html

    {% load blog_tags %}

    {% total_posts %}

    {{ post.text|markdown }}


Локализация
-----------

.. code-block:: html

    {% load i18n %}

    {% trans "Text" %}

    {% trans "Text" as text%}
    <h1>{{ text }}</h1>

    {% blocktrans %}
        Hello {{ name }}!
    {% endblocktrans %}

    {% blocktrans with name=user.name|capfirst %}
        Hello {{ name }}!
    {% endblocktrans %}


.. code-block:: html

    {% get_current_language as LANGUAGE_CODE %}
    {% get_available_languages as LANGUAGES %}
    {% get_language_info_list for LANGUAGES as languages %}

    <div class="languages">
        <p>{% trans "Language" %}:</p>
        <ul class="languages">
            {% for language in languages %}
                <li>
                    <a href="/{{ language.code }}/"
                        {% if language.code == LANGUAGE_CODE %}
                            class="selected"
                        {% endif %}>
                        {{ language.name_local }}
                    </a>
                </li>
            {% endfor %}
        </ul>
    </div>


Кеширование
-----------

.. code-block:: html

    {% load_cache %}

    {% cache 300 fragment_name %}
    {% endcache %}