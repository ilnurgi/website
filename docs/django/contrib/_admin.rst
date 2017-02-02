Админка
=======

.. code-block:: py

    from django.contrib import admin

    # регистрация модели в админке
    admin.site.register(Good, GoodAdmin)

.. code-block:: py

    from django.contrib import admin
    from django.contrib.auth.models import User

    from .models import Profile

    class UserAdmin(admin.UserAdmin):
        inlines = [UserProfileInline]
        list_display = ('name', 'created')
        searching_fields = ['name']
        ordering = ['name']

    admin.site.unregister(User)
    admin.site.register(User, UserAdmin)

    admin.site.site_header = "Admin panel Header"

ModelAdmin
----------

.. py:class:: django.contrib.admin.ModelAdmin()

    Объект настраивающий внешний вид админки для модели

    .. code-block:: py

        def export_to_csv(modeladmin, request, queryset):
            # ...
            fields = [
                field for field in opts.get_fields()
                if not field.many_to_many and not field.one_to_many]
            # ...
            return response
        export_to_csv.short_description = 'Export to csv'

        def order_pdf(obj):
            return '<a href={}>PDF</a>'.format(
                reverse('', args=[]))
        order_pdf.allow_tags = True
        order_pdf.short_description = 'PDF bill'

        class PostAdmin(admin.ModelAdmin):

            list_display = ('id', 'title', order_pdf)
            list_filter = ('status', 'created', 'publish', 'author')
            search_fields = ('title', 'body')
            prepopulated_fields = {'slug': ('title',)}
            raw_id_fields = ('author',)
            date_hierarchy = 'publish'
            ordering = ['status', 'publish']
            actions = [export_to_csv]

    .. py:attribute:: actions_on_bottom

        Булево, список действий снизу

    .. py:attribute:: actions_on_top

        Булево, список действий сверху

    .. py:attribute:: date_hierarchy

        Поле, по которому также можно фильтровать объекты в разрезе дат

    .. py:attribute:: exclude

        Список полей модели, которые необходимо скрыть

    .. py:attribute:: fields

        Список полей модели, которые можно редактировать

        .. code-block:: py

            fields = ("content", )

        .. code-block:: py

            fields = (
                # эти два поля будут расположены по горизонтали
                ("name", "content"),
            )

    .. py:attribute:: fieldsets

        Группирует поля модели

        .. code-block:: py

            fieldsets = (
                (
                    None,
                    {
                        "fields": (("name", "category"),),
                        "classes": (("collapse", ), ),
                    },
                ),
            )

    .. py:attribute:: list_display

        Список полей, которые отображаются на странице списка объектов

    .. py:attribute:: list_display_links

        Список полей, по которым можно перейти на страницы редактирования

    .. py:attribute:: list_editable

        Список полей, которые можно редактировать прямо в списке

    .. py:attribute:: list_filter

        Список полей, по которым можно отфильтровать объекты на странице списка объектов

    .. py:attribute:: list_max_show_all

        Макисмальное количесвто элементов, после которого появится кнопка отобразить все

    .. py:attribute:: list_per_page

        Пагинация

    .. py:attribute:: ordering

        Список полей, по которым отсртировываются список объектов на стрице списка объектов

    .. py:attribute:: populated_fields

    .. py:attribute:: preserve_filters

        Булево, запоминать фильтрацию списка при редактировании элемента

    .. py:attribute:: radio_fields

        .. code-block:: py

            radio_fields = {
                "category": admin.VERTICAL,
            }

    .. py:attribute:: raw_id_fields

    .. py:attribute:: readonly_fields

        Список полей, только для чтения

    .. py:attribute:: save_as

        Булево, включить кнопку сохранить как новый объект

    .. py:attribute:: save_on_top

        Булево, кнопки сохранить и удалить в верху страницы
        
    .. py:attribute:: search_fields

        Список полей, по которым можно произвести поиск объектов на странице ссписка объектов


StackedInLine
-------------

Вложенный набор форм, в которых элементы управления распологаются один за другим по вертикали

.. py:class:: django.contrib.admin.StackedInLine()

    .. code-block:: py

        class UserProfileInline(admin.StackedInLine):
            model = Profile

    .. py:attribute:: can_delete

        Булево, возможность удалять записи

    .. py:attribute:: exclude

    .. py:attribute:: extra

        Максимальное количесвто выводимых пустых форм для создания новых записей

    .. py:attribute:: fields

    .. py:attribute:: fieldsets

    .. py:attribute:: model

        Вторичная модель

    .. py:attribute:: max_num

        Максимальное количесвто форм в наборе

    .. py:attribute:: ordering

    .. py:attribute:: radio_fields

    .. py:attribute:: readonly_fields

    .. py:attribute:: verbose_name

        Надпись для формы

    .. py:attribute:: verbose_name_plural

        Надпись для всего набора форм

TabularInline
-------------

Вложенный набор форм, организованный в виде таблицы.

.. py:class:: django.contrib.admin.TabularInline()

    .. code-block:: py

        class OrderItemInline(admin.TabularInline):

            model = OrderItem
            raw_id_fields = ['product']

        class OrderAdmin(admin.ModelAdmin):
            list_display = [
                'id', 'first_name', 'last_name', 'email', 'address',
                'postal_code', 'city', 'paid', 'created', 'updated',
            ]
            list_filter = ['paid', 'created', 'updated']
            inlines = [OrderItemInline]

    .. py:attribute:: can_delete

        Булево, возможность удалять записи

    .. py:attribute:: exclude

    .. py:attribute:: extra

        Максимальное количесвто выводимых пустых форм для создания новых записей

    .. py:attribute:: fields

    .. py:attribute:: fieldsets

    .. py:attribute:: model

        Вторичная модель

    .. py:attribute:: max_num

        Максимальное количесвто форм в наборе

    .. py:attribute:: ordering

    .. py:attribute:: radio_fields

    .. py:attribute:: readonly_fields

    .. py:attribute:: verbose_name

        Надпись для формы

    .. py:attribute:: verbose_name_plural

        Надпись для всего набора форм

