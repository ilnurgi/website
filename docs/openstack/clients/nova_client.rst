Клиент сервиса `nova`
=====================

Получение клиента
-----------------

.. code-block:: py

    from novaclient.client import Client as NovaClient

    nova_client = NovaClient(

        # указываем версию клиента
        '2',

        # токен пользователя, из сервиса `keystone`
        token=auth_token,

        # токен пользователя, из сервиса `keystone`
        auth_token=auth_token,

        # урл сервиса `nova`
        auth_url=nova_url,

        # урл сервиса `nova`
        bypass_url=nova_url,

        # список расширений для клиента
        extensions=[])


Данный клиент имеет доступы к следующим ресурсам:

.. toctree::
   :maxdepth: 2

   resources/services