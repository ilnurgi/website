host - управление хостами
=========================

* `ensure` - состояние

    * `absent` - не должен существовать

* `host_aliases` - алиасы хоста

* `ip` - адрес хоста


.. code-block:: puppet

    host {
        'syslog':
            ip => '10.10.10.10'
    }


.. code-block:: puppet

    host { 
        'ntpserver.example.com':
            ip           => '10.100.10.50',
            host_aliases => 'timeserver',
    }


.. code-block:: puppet

    host { 
        'dashboard':
            ip           => '10.120.100.111',
            host_aliases => [ 'nagios', 'munin' ],
    }


.. code-block:: puppet

    host { 
        'syslog':
            ip => $::domain ? {
                /production/ => '10.10.10.10',
                /staging/    => '192.168.23.10',
                default      => '10.100.100.100',
            }
    }