NovaClient
==========


.. py:class:: novaclient.client.Client(version, **kwargs)

    Клиент для работы с сервисом Nova.

    * version - версия API клиента

        :py:class:`novaclient.api_versions.APIVersion` или строка (1.1, 2, 2.х)

    * token - токен пользователя, из сервиса `keystone`

    * auth_token - токен пользователя, из сервиса `keystone`

    * auth_url - урл сервиса `nova`

    * bypass_url - урл сервиса `nova`

    * extensions - список расширений для клиента

    .. code-block:: py

        from novaclient.client import Client as NovaClient

        nova_client = NovaClient(
            version='2',
            token=auth_token,
            auth_token=auth_token,
            auth_url=nova_url,
            bypass_url=nova_url,
            extensions=[])

Ресурсы, управляемые клиентом
-----------------------------

.. toctree::
    :maxdepth: 1

    services