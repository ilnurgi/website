exec - выполнить консольную команду
===================================

* `command` - команда, если не задана, то используется навзание ресурса

* `creates` - условие наличия файла, если файл существует, то команда не выполнится

* `cwd` - путь от которой запускается команда

* `environment` - переменные окружения выполнения команды

* `group` - группа, от имени которой выполняется команда

* `logoutput` - логирование выхлопа команды

    * `true` - включить
    
    * `false` - выключить

    * `'on_failure'` - по умолчанию, если есть ошибки

* `onlyif` - команда, если эта команда выполнится с ошибкой, то главная команда не будет выполняться

* `path` - пути для поиска команд. 

    Можно задать сразу несколько разделяя их двоеточием ':'

* `provider` - бекенд выполняемых задач

    * `posix` - 

    * `shell` - 

    * `windows` - 

* `refresh` - команда обновления, по умолчанию ресурс выполняется всегда, если например его кто нить дернет по обновлению. 

    Этот параметр задает особую команду именно для обновления.

* `refreshonly` - ресурс выполняется только в режиме обновления true/false

* `returns` - код возврата команды

* `timeout` - таймаут выполнения ресурса, в секундах

    По умолчанию 300.

    0 - выключить таймаут.

* `tries` - количесвто попыток выполнения команды, по умолчанию 1.

* `try_sleep` - время ожидания между попытками

* `umask`

* `unless`

* `user` - пользователь, от чьего имени запускается задача

.. code-block:: puppet

    exec {
        'refresh_cache':
            command => 'refresh_cache 8600',
            path    => '/usr/local/bin/:/bin/',
            # path  => [ '/usr/local/bin/', '/bin/' ]
    }


.. code-block:: puppet

    exec {
        'refresh_cache':
            command => 'mkdir /tmp/tmpdir'
    }


.. code-block:: puppet

    # если указанной папки не существует, то команда выполнится
    exec { 
        'create_needed_directory':
            command => '/bin/mkdir -p /tmp/needed/directory',
            creates => '/tmp/needed/directory'
    }


.. code-block:: puppet

    # команда выполнится если греп чего нить вернет
    exec { 
        'run_account_purger':
            command => '/usr/local/sbin/account_purger',
            onlyif  => 'grep -c old_account /etc/passwd',
    }


.. code-block:: puppet
  
    # команда выполнится если все команды что-то вернут
    exec { 
        'run_account_purger':
            command => '/usr/local/sbin/account_purger',
            onlyif  =>  [
                'grep -c old_account /etc/passwd',
                'test -d /home/old_account/'
            ]
    }