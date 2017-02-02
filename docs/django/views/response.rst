Ответы
======

Http404
-------

.. py:class:: django.http.Http404()

    Исключение генерируется если страница не найдена

    .. code-block:: py

        def index(request, good_id):
            try:
                good = Goods.objects.get(id=good_id)
            except Good.DoesNotExists:
                raise Http404()
            ...


render
------

.. py:method:: django.shortcuts.render(**kwargs)

    Возвращает строку, отрендеренная html страница

    * request - :py:class:`HttpRequest`, запрос

    * template_name - строка, путь к файлу шаблона относительно папки с шаблонами приложения

    * context=None - контекст, который будет передаваться в шаблон

    * context_instance=_context_instance_undefined -

    * content_type=None -

    * status=None -

    * current_app=_current_app_undefined -

    * dirs=_dirs_undefined -

    * dictionary=_dictionary_undefined -

    * using=None -