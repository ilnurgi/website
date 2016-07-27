Другое
======

Отправка email сообщений
------------------------

.. code-block:: py

    from django.core.mail import send_mail

    send_mail(
        'Django mail',
        'This e-mail was sent with Django.',
        'your_account@gmail.com',
        ['your_account@gmail.com'],
        fail_silently=False)


django-taggit
-------------
.. code-block:: py

    # settings.py

    INSTALLED_APPS = (
        ...,
        'taggit',
    )

.. code-block:: py

    # models.py

    from taggit.managers import TaggableManager

    class Post(models.Model):

        tags = TaggableManager()

.. py:class:: taggit.managers.TaggableManager()

    .. py:method:: add()

        Добавляет теги

        .. code-block:: py

            post.tags.add('music', 'jazz', 'django')

    .. py:method:: all()

        Возвращает все теги

        .. code-block:: py

            post.tags.all()
            # [<Tag: jazz>, ...]

    .. py:method:: remove()

        Удаляет тег

        .. code-block:: py

            post.tags.remove('jazz')


python-social-auth
------------------

.. code-block:: py

    # settings.py

    INSTALLED_APPS = (
        ...,
        'social.apps.django_app.default',
    )

    # ========
    # Facebook
    # https://developers.facebook.com/apps/?action=create
    # ========
    AUTHENTICATION_BACKENDS += (
        'social.backends.facebook.Facebook2OAuth2',
    )
    SOCIAL_AUTH_FACEBOOK_KEY = 'XXX'
    SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX'
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

    # =======
    # Twitter
    # https://apps.twitter.com/app/new
    # =======
    AUTHENTICATION_BACKENDS += (
        'social.backends.twitter.TwitterOAuth',
    )
    SOCIAL_AUTH_TWITTER_KEY = 'XXX'
    SOCIAL_AUTH_TWITTER_SECRET = 'XXX'

    # =======
    # Google
    # https://console.developers.google.com/project
    # =======
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXX'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXX'


.. code-block:: py

    # urls.py

    url(
        'social-auth/',
        include('social.apps.django_app.urls', namespace='social')),

.. code-block:: html

    <div class="social">
        <ul>
            <li class="facebook">
                <a href="{% url "social:begin" "facebook" %}">
                    Sign in with Facebook</a></li>
            <li class="twitter">
                <a href="{% url "social:begin" "twitter" %}">
                    Login with Twitter</a></li>
            <li class="google">
                <a href="{% url "social:begin" "google" %}">
                    Login with Google</a></li>
        </ul>
    </div>


redis
-----

redis-server - старт сервера
redis-cli - консольное управление

.. code-block:: sh

    pip install redis

.. code-block:: sh

    # добавляем ключ в хранилище
    127.0.0.1:6379> SET name "ilnurgi"
    OK

    # получаем значение ключа
    127.0.0.1:6379> GET name
    "ilnurgi"

    # проверяем существование ключа
    127.0.0.1:6379> EXISTS name
    (integer) 1

    # ключ удалится из хранилища через 2 секунды
    127.0.0.1:6379> EXPIRE name 2
    (integer) 1
    127.0.0.1:6379> GET name
    (nil)

    127.0.0.1:6379> SET total 1
    OK
    127.0.0.1:6379> DEL total
    (integer) 1
    127.0.0.1:6379> GET total
    (nil)

.. code-block:: py

    # views.py

    import redis

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    value = r.get('foo')

    # увеличит значение на 1,
    # если ключа нет то создаст со значением 0 и вернет увеличенное значение
    value2 = r.incr('some_key')

.. code-block:: py

    # возвращает ключи словаря
    # 0 - минимальное значение ключа
    # -1 - максимальное значение,
    # desc - обратная сортировка
    value2 = r.zrange('some_key', 0, -1, desc=True)[:10]

celery
------

.. code-block:: sh

    pip install celery
    apt-get install rabbitmq

    # pip install flower
    # celery -A myshop flower
    # celery -A myshop worker -l info

.. code-block:: py

    # celery.py

    import os

    from celery import Celery

    from django.conf import settings

    app = Celery('myshop')
    app.config_from_object('django.conf:settings')
    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

.. code-block:: py

    # tasks.py

    from celery import task
    from django.core.mail import send_mail

    @task
    def send_mail_task(some_arg):
        # ...
        return send_mail(subject, message, admin_email, [some_email])

.. code-block:: py

    # views.py

    def some_view(request):

        # ...
        send_mail_task.delay(some_arg)
        # ...


django-paypal
-------------

.. code-block:: sh

    pip install django-paypal

.. code-block:: py

    # settings.py

    INSTALLED_APPS = (
        # ...
        'paypal.standard.ipn',
    )

    PAYPAL_RECEIVER_EMAIL = 'mypaypalemail@myshop.com'
    PAYPAL_TEST = True

.. code-block:: py

    # urls.py

    url(r'^paypal/', include('paypal.standard.ipn.urls')),

.. code-block:: py

    # views.py

    from decimal import Decimal

    from django.conf import settings
    from django.core.urlresolvers import reverse
    from django.shortcuts import render, get_object_or_404

    from paypal.standard.forms import PayPalPaymentsForm

    from orders.models import Order

    def payment_process(request):
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        host = request.get_host()

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': (
                '%.2f' % order.get_total_cost().quantize(Decimal('.01'))),
            'item_name': 'Order {}'.format(order.id),
            'invoice': str(order.id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
            'cancel_return': (
                'http://{}{}'.format(host, reverse('payment:canceled'))),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(
            request,
            'payment/process.html',
            {'order': order, 'form':form},
        )

.. code-block:: py

    # signals.py

    from django.shortcuts import get_object_or_404

    from paypal.standard.models import ST_PP_COMPLETED
    from paypal.standard.ipn.signals import valid_ipn_received

    from orders.models import Order

    def payment_notification(sender, **kwargs):
        ipn_obj = sender
        if ipn_obj.payment_status == ST_PP_COMPLETED:
            # payment was successful
            order = get_object_or_404(Order, id=ipn_obj.invoice)
            # mark the order as paid
            order.paid = True
            order.save()

    valid_ipn_received.connect(payment_notification)

translations
------------

.. code-block:: py

    from django.utils.translation import gettext as _
    from django.utils.translation import gettext_lazy, ngettext, ngettext_lazy

    output = _('Text to be translated.')
    output = gettext_lazy('Text to be translated.')

    output = ngettext(
        'there is %(count)d product',
        'there are %(count)d products',
        count) % {'count': count}