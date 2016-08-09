Конспекты по django
===================

Структура django приложения

    * application - папка приложения

        * __init__.py - приложение - пакет

            .. code-block:: py

                # __init__.py

                default_app_config = 'app_name.apps.AppConfig'

        * admin.py - настройка админки

        * app.py - настройка приложения

            .. code-block:: py

                # app.py

                from django.apps import AppConfig

                class BlogConfig(AppConfig):
                    name = 'blog'
                    verbose_name = 'blog'

                    def ready(self):
                        import blog.signals

        * feeds.py - rss рассылка

        * forms.py - формы приложения

        * models.py - модели приложения

        * signals.py - сигналы

        * sitemaps.py - карта сайта

        * tests.py - тесты приложения

        * urls.py - маршруты, роутинг урлов

        * views.py - представления

        * migrations - пакет с миграциями приложения

            * __init__.py - пакет

        * templates - папка с шаблонами

            * index.html - какой то шаблон

        * templatetags - папка с самописными тегами для шаблонов

            * tag.py - какой то тег

        * static - папка со статикой

            * app.css - какая то статика


.. toctree::
    :maxdepth: 1

    settings
    models/index
    views/index
    forms/index
    templates
    urls
    signals
    contrib/index
    cli
    faq
    django-rest-framework/index
