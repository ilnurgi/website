Представления в виде классов
============================

.. code-block:: py

    from django.contrib.admin.decorators import login_required
    from django.http import HttpResponse
    from django.utils.decorators import method_decorator
    from django.view.generic import View

    class IndexView(View):

        @method_decorator(login_required)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

        def get(self, request):
            return HttpResponse('Hello world')

.. code-block:: py

    from django.http import HttpResponse
    from django.view.generic import View

    class LoginRequiredMixin(object):

        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_authenticated():
                raise PermissionDenied()
            return super().dispatch(request, *args, **kwargs)

    class IndexView(LoginRequiredMixin, View):

        def get(self, request):
            return HttpResponse('Hello world')


ArchiveIndexView
----------------

.. py:class:: django.views.generic.ArchiveIndexView()

    Представление для вывода списка записей, отсортированных по убыванию значения даты.

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.dates.BaseArchiveIndexView`

    .. code-block:: py

        class SomeArchiveView(ArchiveView):
            model = SomeModel
            date_field = 'created'

    .. py:attribute:: template_name_suffix

        Суффикс для шаблона, по умолчанию `'_archive'`


CreateView
----------

.. py:class:: django.views.generic.CreateView()

    Представление для создания нового элемента модели

    Наследник:

        * :py:class:`django.views.generic.detail.SingleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.edit.BaseCreateView`

    .. code-block:: py

        class FeedView(CreateView):
            model = models.Post
            template_name = "feed.html"
            success_url = reverse_lazy("index")
            fields = []
            form_class = Form

            def form_valid(self, form):
                return super().form_valid(form)

    .. py:attribute:: template_name_suffix

        Суффикс для шаблона, по умолчанию `'_form'`


DateDetailView
--------------

.. py:class:: django.views.generic.DateDetailView()


DayArchiveView
--------------

.. py:class:: django.views.generic.DayArchiveView()

    Представление для списка записей по дням

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.dates.BaseDayArchiveView`

    .. code-block:: py

        class SomeDayArchiveView(DayArchiveView):

            model = SomeModel
            date_field = 'created'
            make_object_list = True

    .. py:attribute:: template_name_suffix

        Суфикс для шаблона, по умолчанию `"_archive_day"`


DeleteView
----------

.. py:class:: django.views.generic.DeleteView()

    Вьюха для удаления объекта из БД


DetailView
----------

.. py:class:: django.views.generic.DetailView()

    Вьюха для отображения информации объекта из БД

    Наследник:

        * :py:class:`django.views.generic.detail.SingleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.detail.BaseDetailView`

    .. code-block:: py

        class SomeDetailView(DetailView):
            model = SomeModel


FormView
--------

.. py:class:: django.views.generic.FormView()

    .. code-block:: py

        from django.core.urlresolvers import reverse_lazy

        class GenericFormView(generic.FormView):
            template_name = 'form.html'
            form_class = DetailsForm
            success_url = reverse_lazy("success")

            def get_form_kwargs(self):
                return super().get_form_kwargs()


ListView
--------

.. py:class:: django.views.generic.ListView()

    Представление отображает страницу списка объектов

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.list.BaseListView`

    Контекст:

        * object_list - список объектов указанной модели

        * paginator - объект для пагинации

    .. code-block:: py

        class PostListView(ListView):
            queryset = Post.objects.all()
            context_object_name = 'posts'
            paginate_by = 3
            template_name = 'list.html'

    .. code-block:: py

        class PostListView(ListView):
            model = Post
            template_name = 'list.html'

            def get_queryset(self):
                qs = super().get_queryset()
                return qs.filter(...)

    .. py:attribute:: model

        Модель для представления


    .. py:attribute:: paginate_by

        Количесвто записей на странице


    .. py:attribute:: template_name

        Путь к файлу шаблона, по умолчанию app_name/model_name_list.html


    .. py:attribute:: template_name_suffix

        Суффикс для файла шаблона, по умолчанию _list


    .. py:method:: get_queryset()

        Возвращает объект запросы БД


MonthArchiveView
----------------

.. py:class:: django.views.generic.MonthArchiveView()

    Представление списка записей за указанный год и месяц

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.dates.BaseMonthArchiveView`

    .. code-block:: py

        class SomeMonthArchiveView(MonthArchiveView):

            model = SomeModel
            date_field = 'created'
            make_object_list = True

    .. py:attribute:: template_name_suffix

        Суфикс для шаблона, по умолчанию `'_archive_month'`


RedirectView
------------

.. py:class:: django.views.generic.RedirectView()


TemplateView
------------

.. py:class:: django.views.generic.TemplateView()

    Представление возвращащает ответ, в виде отрендеренного шаблона.

    Наследник:

        * :py:class:`django.views.generic.base.TemplateResponseMixin`

        * :py:class:`django.views.generic.base.ContextMixin`

        * :py:class:`django.views.generic.View`

    .. code-block:: py

        class AboutView(TemplateView):

            template_name = 'about.html'

            def get_context_data(self, **kwargs):
                context = super().get_context_data()

                # self.request
                # self.args
                # self.kwargs

                return context

    .. py:attribute:: args

        Неименованные параметры обработки запроса

    .. py:attribute:: kwargs

        Именованные параметры обработки запроса

    .. py:attribute:: request

        Запрос

    .. py:attribute:: template_name

        Путь к шаблону


TodayArchiveView
----------------

.. py:class:: django.views.generic.TodayArchiveView()

    Представление для списка записей для текущей даты

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.dates.BaseTodayArchiveView`

    .. py:attribute:: template_name_suffix

        Суфикс для шаблона, по умолчанию `"_archive_day"`


UpdateView
----------

.. py:class:: django.views.generic.UpdateView()

    Представление для обновления объекта модели

    .. py:attribute:: fields

        Список полей модели, которые будут на форме

    .. py:attribute:: initial

        Словарь начальных данных для формы

    .. py:attribute:: success_url

        Адрес, на который будет пепрезод после успешного обновления

    .. py:attribute:: template_name_suffix

        Суффикс для шаблона, по умолчанию `'_form'`


WeekArchiveView
---------------

.. py:class:: django.views.generic.WeekArchiveView()


YearArchiveView
---------------

.. py:class:: django.views.generic.YearArchiveView()

    Представление выводит список записей, относящихся к указанному году.

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectTemplateResponseMixin`

        * :py:class:`django.views.generic.dates.BaseYearArchiveView`

    .. code-block:: py

        class SomeYearArchiveView(YearArchiveView):

            model = SomeModel
            date_field = 'created'
            make_object_list = True

    .. py:attribute:: template_name_suffix

        Суффикс для поиска шаблонов, по умолчанию `'_archive_year'`


Базовые классы
--------------

BaseArchiveIndexView
++++++++++++++++++++

.. py:class:: django.views.generic.dates.BaseArchiveIndexView()

    Базовый класс для архивных записей

    .. py:attribute:: context_object_name

        Название переменной в контексте, в котором будут содержаться записи


BaseCreateView
++++++++++++++

.. py:class:: django.views.generic.edit.BaseCreateView()

    Базовое представление для создания элемента модели

    Наследник:

        * :py:class:`django.views.generic.edit.ModelFormMixin`

        * :py:class:`django.views.generic.edit.ProcessFormView`


BaseDateListView
++++++++++++++++

.. py:class:: django.views.generic.dates.BaseDateListView()

    Базовый класс для списка записей с учетом дат

    В контекте положит:

        * latest - список записей вывода

        * date_list - список всех годов

        * параметры пагинации из :py:class:`django.views.generic.list.MultipleObjectMixin`

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectMixin`

        * :py:class:`django.views.generic.dates.DateMixin`

        * :py:class:`django.views.generic.base.View`


BaseDayArchiveView
++++++++++++++++++

.. py:class:: django.views.generic.dates.BaseDayArchiveView()

    Базовый класс для представлений по дням

    В контекст положит:

        * day - текущая дата

        * previous_day - предыдущая дата

        * next_day - следующая дата

        * previous_month - предыдущий месяц

        * next_month - следующий месяц

    Наследник:

        * :py:class:`django.views.generic.dates.YearMixin`

        * :py:class:`django.views.generic.dates.MonthMixin`

        * :py:class:`django.views.generic.dates.DayMixin`

        * :py:class:`django.views.generic.dates.BaseDateListView`


BaseDetailView
++++++++++++++

.. py:class:: django.views.generic.detail.BaseDetailView()

    Базовый класс для представления объекта

    В контекст положит:

        * object - объект

    Наследник:

        * :py:class:`django.views.generic.detail.SingleObjectMixin`

        * :py:class:`django.views.generic.View`

    .. py:attribute:: object

        Объект для представления


BaseListView
++++++++++++

.. py:class:: django.views.generic.list.BaseListView()

    Базовый класс для представления списка объектов

    Наследник:

        * :py:class:`django.views.generic.list.MultipleObjectMixin`

        * :py:class:`django.views.generic.View`


BaseMonthArchiveView
++++++++++++++++++++

.. py:class:: django.views.generic.dates.BaseMonthArchiveView()

    Базовый класс для представления списка объектов за указанный месяц

    В контекст положит:

        * month - текущий месяц

        * next_month - следующий месяц

        * previous_month - предыдущий месяц

    Наследник:

        * :py:class:`django.views.generic.dates.YearMixin`

        * :py:class:`django.views.generic.dates.MonthMixin`

        * :py:class:`django.views.generic.dates.BaseDateListView`


BaseTodayArchiveView
++++++++++++++++++++

.. py:class:: django.views.generic.dates.BaseTodayArchiveView()

    Базовый клас для представления списка элементов за сегодня

    Наследник:

        * :py:class:`django.views.generic.dates.BaseDayArchiveView`


BaseYearArchiveView
+++++++++++++++++++

.. py:class:: django.views.generic.dates.BaseYearArchiveView()

    Базовый класс для представлении списка элементов по годам

    В контекст положит:

        * date_list - список дат

        * year - указанный год

        * next_year - следующий год

        * previous_year - прошлый год

    Наследник:

        * :py:class:`django.views.generic.dates.YearMixin`

        * :py:class:`django.views.generic.dates.BaseDateListView`

    .. py:attribute:: date_list_period

        'month'

    .. py:attribute:: make_object_list

        False

View
++++

.. py:class:: django.views.generic.View()

    Базовый класс для всех предсавлений

    Поддерживает методы запроса (get, post, put, patch, delete, head, options,
    trace) для обработки запроса, т.е. можно просто объявить метод класса
    по однойменному методу, который будет соответсвенно обрабатывать метод запроса.

    .. py:method:: as_view(**initkwargs)

        Возвращает экземпляр класса представления, обработчико запросов


Миксины
-------

ContextMixin
++++++++++++

.. py:class:: django.views.generic.base.ContextMixin()

    Миксин, для поддержки контекста в представлениях

    .. py:method:: get_context_data(**kwargs)

        Возвращает контекст для представления


DateMixin
+++++++++

.. py:class:: django.views.generic.dates.DateMixin()

    .. py:attribute:: allow_future

        Булево, использовать и будущие записи

    .. py:attribute:: date_field

        Имя поля модели, на основе которого будет строиться сортировка

    .. py:attribute:: model

        Модель, по которому будут фильтровать записи


DayMixin
++++++++

.. py:class:: django.views.generic.dates.DayMixin()

    Миксин для поддержки дня

    .. py:attribute:: day_format

        Формат для даты, по умолчанию `'%d'`

    .. py:attribute:: day

        День


FormMixin
+++++++++

.. py:class:: django.views.generic.edit.FormMixin()

    Миксин для создания форм

    .. py:attribute:: initial

        Начальные данные формы

    .. py:attribute:: form_class

        Класс формы

    .. py:attribute:: success_url

        Урл, на которой переходим в результате успешного сохранения

    .. py:attribute:: prefix

    .. py:method:: get_form_kwargs()

        Возвращает параметры для формы


ModelFormMixin
++++++++++++++

.. py:class:: django.views.generic.edit.ModelFormMixin()

    Миксин создает форму по модели

    Наследник:

        * :py:class:`django.views.generic.edit.FormMixin`

        * :py:class:`django.views.generic.detail.SingleObjectMixin`

    .. py:attribute:: fields

        Поля модели, которые будут на форме


MonthMixin
++++++++++

.. py:class:: django.views.generic.dates.MonthMixin()

    Миксин для поддержки фильтрации по месяцу

    .. py:attribute:: month_format

        Формат для месяца, по умолчанию `'%b'`

    .. py:attribute:: month

        Месяц


MultipleObjectMixin
+++++++++++++++++++

.. py:class:: django.views.generic.list.MultipleObjectMixin()

    Миксин для поддержки просмотра множества объектов, имеет пагинацию.

    В контексте положит:

        * paginator - объект,пагинатор

        * page_obj - объект, страница

        * is_paginated - булево, имеется ли более 1 страницы

        * object_list - queryset элементов представления

    .. py:attribute:: allow_empty

        Булево, пустая страница

    .. py:attribute:: queryset

        QuerySet для представления.

        Не обязательный параметр, можно просто задать модель.

    .. py:attribute:: model

        Модель, с объектами которого производится манипуляция.

        Не обязательный параметр, можно просто задать QuerySet.

    .. py:attribute:: paginate_by

        Количесвто элементов на странице

    .. py:attribute:: paginate_orphans

        Количество элементов на последней странице

    .. py:attribute:: context_object_name

        Название объекта в контексте, по умолчанию `'object_list'`

    .. py:attribute:: paginator_class

        Класс, реализующий пагинацию,
        по умолчанию :py:class:`django.core.paginator.Paginator`

    .. py:attribute:: page_kwarg

        Название переменной в контексте, для страницы, по умолчанию `'page'`

    .. py:attribute:: ordering

        Сортировка элементов  представления


MultipleObjectTemplateResponseMixin
+++++++++++++++++++++++++++++++++++

.. py:class:: django.views.generic.list.MultipleObjectTemplateResponseMixin()

    Миксин позволяет брать в качестве шаблона шаблон,
    по пути `app_name/model_name_list.html`

    Наследник :py:class:`django.views.generic.base.TemplateResponseMixin`

    .. py:attribute:: template_name_suffix

        Суффикс для шаблона списка, по умолчанию `'_list'`


ProcessFormView
+++++++++++++++

.. py:class:: django.views.generic.edit.ProcessFormView()

    Помещает в контекст форму

    Наследник:

        * :py:class:`django.views.generic.View`


SingleObjectMixin
+++++++++++++++++

.. py:class:: django.views.generic.detail.SingleObjectMixin()

    Миксин для представления одного объекта

    .. py:attribute:: model

        Модель, откуда будет браться объект, или можно задать просто кверисет

    .. py:attribute:: queryset

        QuerySet для выборки объекта, можно просто задать модель

    .. py:attribute:: slug_field

        Название слаг поля, по которому можно получить объект из БД,
        по умолчанию `'slug'`

    .. py:attribute:: context_object_name

        Название переменной в контексте, по умолчанию `'object'`

    .. py:attribute:: slug_url_kwarg

        Название переменной в запросе, которая содержит слаг поле,
        по умолчанию `'slug'`

    .. py:attribute:: pk_url_kwarg

        Название переменной в запросе, которая содержит первичный ключ объекта,
        по умолчанию `'pk'`

    .. py:attribute:: query_pk_and_slug

        Использовать слаг филд для получения объекта


SingleObjectTemplateResponseMixin
+++++++++++++++++++++++++++++++++

.. py:class:: django.views.generic.detail.SingleObjectTemplateResponseMixin()

    Миксин позволяет брать в качестве шаблона шаблон,
    по пути `app_name/model_name_detail.html`, из самого объекта

    Наследник :py:class:`django.views.generic.base.TemplateResponseMixin`

    .. py:attribute:: model

        Модель, для которой обрабатывается представление,
        шаблон будет браться по пути `app_name/model_name_detail.html`

        Не обязательный параметр

    .. py:attribute:: template_name_field

        Название атрибута в объекте, который отображает представление,
        в котором указан путь к шаблону

        Не обязательный параметр

    .. py:attribute:: template_name_suffix

        Суффикс для шаблона списка, по умолчанию `'_detail'`


TemplateResponseMixin
+++++++++++++++++++++

.. py:class:: django.views.generic.base.TemplateResponseMixin()

    Миксин, возвращает отрендеренный шаблон для запроса

    .. py:attribute:: template_name

        Путь к шаблону

    .. py:attribute:: template_engine

        Шаблонизатор, по умолчанию дефолтный

    .. py:attribute:: response_class

        Класс ответа, по умолчанию :py:class:`django.template.response.TemplateResponse`

    .. py:attribute:: content_type

    .. py:method:: render_to_response(context, **response_kwargs)

        Возвращает ответ на запрос


YearMixin
+++++++++

.. py:class:: django.views.generic.dates.YearMixin()

    Миксин для представлении списка по годам

    .. py:attribute:: year_format

        Строка, формат по которому будет распозноваться полученное значение года.

        По умолчанию `'%Y'`

    .. py:attribute:: year

        Год в виде строки