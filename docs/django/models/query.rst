Менеджер модели, запросы
========================

_set
----

.. py:method:: _set()

    Доступ к вторичной таблице

    .. code-block:: py

        class Category(models.Model):

            name = models.CharField(...)

        class Good(models.Model):

            category = models.ForeignKey(
                Category,
                on_delete=models.SET_NULL,
            )

        Category.good_set.count()


aggregate
---------

.. py:method:: aggregate()

    Агрегатная функция. Возвращает словарь со значениями агрегатных функции.

    Позволяет:

        * подсчитать сумму значений поля

        * подсчитать среднее арифметичское значений поля

        * ...

    .. code-block:: py

        # количесвто значение, Count(поле, уникальные)
        from django.db.models import Count

        # среднее арифметическое значений, Avg(поле)
        from django.db.models import Avg

        # сумма значений, Sum(поле)
        from django.db.models import Sum

        # максимальное значение, Max(поле)
        from django.db.models import Max

        # минимальное значение, Min(поле)
        from django.db.models import Min

        # отклонение значений, StdDev(поле, отклонение)
        from django.db.models import StdDev

        # дисперсия значений, Variance(поле, дисперсия)
        from django.db.models import Variance

        Goods.objects.aggregate(models.Max('created'), models.Min('created'))
        # { 'created__max': date , 'created__min': date }

all
---

.. py:method:: all()

    Возвращает QuerySet, записи запроса

    .. code-block:: py

        # все записи таблицы
        Good.objects.all()

        # только 5 элементов
        Good.objects.all()[:5]

        # записи с каким то условием
        Good.objects.filter(...).all()


count
-----

.. py:method:: count()

    Возвращает число, количесво записей в запросе

    .. code-block:: py

        # количесвто записей в таблице
        Good.objects.count()

        # количесвто записей в запросе после фильтрации
        Good.objects.filter(...).count()


create
------

.. py:method:: create()

    Создает и возврщает новый объект модели

    .. code-block:: py

        good = Good.objects.create(title="some_title")


distinct
--------

.. py:method:: distinct()

    Оставляет в запросе только уникальные записи

    .. code-block:: py

        Good.objects.distinct()

        Good.objects.distinct('name', 'category__name')


earliest
--------

.. py:method:: earliest()

    Возвращает обхект запроса с наименьшим значением параметра указанного поля


exclude
-------

.. py:method:: exclude(**kwargs)

    Возвращает QuerySet, исключая записи, которые удовлетворяют условиям.

    Аналогичен filter, только исключает записи из выборки.

    .. code-block:: py

        # количесвто записей исключая записи с имененм Pencil
        Good.objects.exclude(name='Pencil').count()

        # все товары кроме указанных
        car_goods = Good.objects.exclude(category__name='car')


exists
------

.. py:method:: exists()

    Возвращает булево, если есть хотябы одна запис в выборке

    .. code-block:: py

        Good.objects.exists()
        # True


filter
------

.. py:method:: filter(**kwargs)

    Возвращает QuerySet, с записями, которые удовлетворяют условиям

    .. code-block:: py

        # количесвто записей с имененм Pencil
        Good.objects.filter(name='Pencil').count()

        # фильтруем товары по названию категории
        # в данном случае, будет сделан джоин связанной таблицы
        car_goods = Good.objects.filter(category__name='car')


first
-----

.. py:method:: first()

    Возвращает первый элемент выборки

    .. code-block:: py

        Good.objects.filter(name='Pencil').first()


get
---

.. py:method:: get()

    Аналогичен фильтру, только возвращает один элемент таблицы

    Возбуждает исключения:

    * DoesNotExists - если записей не найдено

    * MultipleObjectsReturned - если найдено несколько записей

    .. py:method:: py

        try:
            Goods.objects.get()
        except Goods.DoesNotExists:
            pass
        except Goods.MultipleObjectsReturned:
            pass


last
----

.. py:method:: last()

    Возвращает последний элемент выборки

    .. code-block:: py

        Good.objects.filter(name='Pencil').last()


latest
------

.. py:method:: latest()

    Возвращает обхект запроса с наибольшим значением параметра указанного поля


order_by
--------

.. py:method:: order_by()

    Сортирует QuerySet

    .. code-block:: py

        Good.objects.order_by('name')

        Good.objects.order_by('name', 'created')

        Good.objects.order_by('name', '-created')

        Good.objects.order_by('category__name', '-created')


reverse
-------

.. py:method:: reverse()

    Сортирует QuerySet в обратном порядке

    .. code-block:: py

        Good.objects.order_by('name').reverse()

        Good.objects.order_by('name', 'created').reverse()

        Good.objects.order_by('name', '-created').reverse()

        Good.objects.order_by('category__name', '-created').reverse()


Модификаторы запроса
--------------------

* contains - значение поля должно содержать указанное нами

* endswith - значение поля должно заканчиваться на указанное нами

* day - значение поля должно быть равно указанному числу

* exact - значение поля должно быть равно указанному

* gt - значение поля должно быть больше указанного

* gte - значение поля должно быть больше или равно указанному

* hour - значение поля должно быть равно указанному часу

* icontains - значение поля должно содержать указанное нами, без учета регистра

* iendswith - значение поля должно заканчиваться на указанное нами, без учета регистра

* iexact - значение поля должно быть равно указанному, без учета регистра

* in - значение поля должно быть равно одному из указанных

    .. code-block:: py

        Good.objects.filter(category__name__in=['car', 'house'])

* isnull - булево, значение поля должно содержать значение

* istartswith - значение поля должно начинаться с указанного нами, без учета регистра

* lt - значение поля должно быть меньше указанного

    .. code-block:: py

        Good.objects.filter(created__lt=now)

* lte - значение поля должно быть меньше или равно указанному

* minute - значение поля должно быть равно указанной минуте

* month - значение поля должно быть равно указанному месяцу

* range - значение поля должно лежать в указанном диапазоне

    .. code-block:: py

        Good.objects.filter(created__range=(tomorrow, now))

* startswith - значение поля должно начинаться с указанного нами

* second - значение поля должно быть равно указанной секунде

* year - значение поля должно быть равно указанному году

    .. code-block:: py

        Good.objects.filter(created__year=now.year)

* week_day - значение поля должно быть равно указанному дню недели


F
-

>>> from django.db.models import F

Объект позволяет ссылаться на значение модели

.. code-block:: py

    Good.objects.filter(created__lt=F('modified'))

Q
-

>>> from django.db.models import Q

Критерии фильтрации



.. code-block:: py

    # записи, исключая по фильтру
    Good.objects.filter(~Q(created__lt=now))

    # записи по дате или категории
    Good.objects.filter(
        Q(created__lt=date) |
        Q(category__name='car'))

    # записи по дате и категории
    Good.objects.filter(
        Q(created__lt=date) &
        Q(category__name='car'))


FAQ
---

Как склеить два QuerySet

.. code-block:: py

    # плохо
    recent = list(posts) + list(comments)

    # хорошо
    from itertools import chain
    recent = chain(posts, comments)