Ресурсы
=======

.. code-block:: puppet

    # задаем глобальные параметра для ресурса
    Package { ensure => 'installed' }

    # ресурсы будут использровать глобальные параметры
    package { 'screen': }
    package { 'strace': }
    package { 'sudo': }


.. toctree::
    :maxdepth: 1

    cron
    exec
    file
    group
    host 
    notify   
    package
    schedule
    service
    user
    yumrepo