precise-bbcode - bb коды
========================

.. code-block:: py

    # settings.py

    INSTALLED_APPS = (
        ...
        'precise_bbcode',
    )

.. code-block:: py

    # views.py

    from precissebbcode.parser import get_parser

    parser = get_parser()

    html = parser.render(content)

.. code-block:: html

    {% load bbcode_tags %}

    {% bbcode record.content %}

    {{ record.content|bbcode }}

Кофнигурирование
----------------

BBCODE_ALLOW_SMILIES
++++++++++++++++++++

Булево, выключить графические смайлы

BBCODE_ESCAPE_HTML
++++++++++++++++++

Список недопустимых символов,
которые должны быть заменены соответсвующими литералами HTML.

    .. code-block:: py

        BBCODE_ESCAPE_HTML = (
            ('&', '&amp;'),
            ...
        )

BBCODE_NEWLINE
++++++++++++++

HTML тег для разбиения текста на абзацы

По умолчанию "<br>"

SMILIES_UPLOAD_TO
+++++++++++++++++

Имя папки, в которой хранятся файлы смайлов

По умолчанию "precise_bbcode/smilies"


BBCodeTextField
---------------

.. py:class:: precise_bbcode.fields.BBCodeTextField()

    Поле модели для хранения bb code текста.

    .. code-block:: py

        class SomeModel(models.Model):

            content = BBCodeTextField()

    .. py:attribute:: rendered

        HTML содержимое


Наборы bb кодов
---------------

* b - strong - текст полужирный

* i - em - текст курсивый

* u - u - подчеркнутый текст

* s - strike - зачеркнутый текст

* center - текст по центру

    .. code-block:: html

        <!--
        [center]текст[/center]
        -->
        <div style="text-align: center;">текст</div>

* code - текст с сохранением форматирования

    .. code-block:: html

        <!--
        [code]текст[/code]
        -->
        <code>текст</code>

* color - текст в указанный цвет

    .. code-block:: html

        <!--
        [color=red]текст[/color]
        [color=#fff]текст[/color]
        -->
        <span style="color: red">текст</span>

* quote - текст цитата

    .. code-block:: html

        <!--
        [quote=red]текст[/quote]
        -->
        <blockquote></blockquote>

* list - список маркированный

    .. code-block:: html

        <!--
        [list]
            [*]элемент списка
            [*]элемент списка
        [/list]
        -->

        <ul></ul>

    .. code-block:: html

        <!-- 1, 01, i, I, a, A -->
        <!--
        [list=1]
            [*]нумерованный элемент списка
            [*]нумерованный элемент списка
        [/list]
        -->
        <ul style="list-style-type: decimal;">
            <li></li>
        </ul>

* url - ссылка

    .. code-block:: html

        <!--
        [url]ilnurgi1.ru[/url]
        [url=http://ilnurgi1.ru]ilnurgi1.ru[/url]
        -->
        <a href="http://ilnurgi1.ru">текст</a>

* img - картинка

    .. code-block:: html

        <!--
        [img]ilnurgi1.ru[/img]
        -->
        <img src="ilnurgi1.ru" alt="">