Пагинация
=========

.. code-block:: py

    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    def post_list(request):
        object_list = Post.objects.all()

        # 3 сообщения на страницу
        paginator = Paginator(object_list, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(
            request,
            'posts.html',
            {
                'page': page,
                'posts': posts,
            },
        )

.. code-block:: html

    <div class="pagination">
        <span class="step-links">
            {% if page.has_previous %}
                <a href="?page={{ page.previous_page_number }}">Previous</a>
            {% endif %}
                <span class="current">
                    Page {{ page.number }} of {{ page.paginator.num_pages }}.
                </span>
            {% if page.has_next %}
                <a href="?page={{ page.next_page_number }}">Next</a>
            {% endif %}
        </span>
    </div>

Paginator
---------

.. py:class:: django.core.paginator.Paginator()

    * orphans - минимальное количество позиции, допустимое на последней странице.

    * allow_empty_first_page - по умолчанию False,
      что вызовет исключение если список элементов пуст.
      Если True - ошибки не будет.

    .. code-block:: py

        paginator = Paginator(queryset, 3)

    .. py:attribute:: count

        Общее количесвто элементов в списке

    .. py:attribute:: num_pages

        Общее количесвто страниц

    .. py:attribute:: page_range

        Возвращает список, содержащий номера полученных страниц

        .. code-block:: py

            paginator.page_range
            # [1, 2, 3, ...]

    .. py:method:: page(page_number)

        Возвращает объект :py:class:`django.core.paginator.Page`,
        указанную страницу из списка.

        Возбуждает исключения:

        * :py:class:`django.core.paginator.InvalidPage` - если номер задан некорректно

        * :py:class:`django.core.paginator.PageNotAnInteger` - если номер задан некорректно

        * :py:class:`django.core.paginator.EmptyPage` - если обращение к несуществующей странице


Page
----

.. py:class:: django.core.paginator.Page()

    Объект, представляет страницу из пагинации

    .. py:attribute:: number

        Номер текущей страницы

    .. py:attribute:: paginator

        Возвращает :py:class:`django.core.paginator.Paginator`,
        которым была создана данная страница

    .. py:method:: end_index()

        Возвращает номер последней позиции

    .. py:method:: has_next()

        Возвращает булево, это не последняя страница

    .. py:method:: has_other_pages()

        Возвращает булево, это не единственная страница

    .. py:method:: has_previous()

        Возвращает булево, это не первая страница

    .. py:method:: next_page_number()

        Возвращает номер следующей страницы

        Возбуждает исключение :py:class:`django.core.paginator.InvalidPage`
        если это последняя страница

    .. py:method:: previous_page_number()

        Возвращает номер предыдущей страницы

        Возбуждает исключение :py:class:`django.core.paginator.InvalidPage`
        если это первая страница

    .. py:method:: start_index()

        Возвращает индекс первой страницы


InvalidPage
-----------

.. py:class:: django.core.paginator.InvalidPage()

    Исключение возникает, если номер задан некорректно


PageNotAnInteger
----------------

.. py:class:: django.core.paginator.PageNotAnInteger()

    Исключение возникает, если номер задан некорректно

    Наследник :py:class:`django.core.paginator.InvalidPage`


EmptyPage
---------

.. py:class:: django.core.paginator.EmptyPage()

    Исключение возникает, если обращение к несуществующей странице

    Наследник :py:class:`django.core.paginator.InvalidPage`
