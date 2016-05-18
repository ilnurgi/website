service - управление службами
=============================

* `binary` — путь к службе (демону). 

    Используется только в системах, которые не поддерживают init скрипт.
    
* `enable` - служба стартует при запуске системы

    * `true`

    * `false`

    * `manual`

* `ensure` - состояние

    * `'running'` - запущен
    
    * `'stopped'` - отсановлен

* `start`

* `stop`

* `restart`

* `status`


.. code-block:: puppet

    service {
        'cron':
            ensure => 'running'
    }