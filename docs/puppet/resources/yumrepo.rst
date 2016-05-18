yumrepo - управелние пакетным менеджером yum
============================================

Позволяет управлять подключенными репозиториями, посредством изменения /etc/yum.conf

* `baseurl` — URL данного репозитория. 

    * `absent` - удалит данные репозиторий из файла полностью

* `cost` — cтоимость данного репозитория. 

    * `absent` - удалит данные репозиторий из файла полностью

* `descr`

* `enabled`

* `enablegroups`

* `exclude`

* `failovermethod`

* `gpgcheck`

* `gpgkey`

* `http_caching`

* `include`

* `includepkgs`

* `keepalive`

* `metadata_expire`

* `mirrorlist`

* `name`

* `priority`

* `protect`

* `proxy`

* `proxy_password`

* `proxy_username`

* `timeout`

.. code-block:: puppet

    yumrepo {
        'company_app_repo':
            enabled  => 1,
            descr    => 'Repo description',
            baseurl  => 'http://repos.example.org/apps',

            /*
             * 'absent' - удалить репозитории из пакетного менеджера
             */
            gpgcheck => 0
    }