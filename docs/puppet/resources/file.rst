file - управление папками и директориями
========================================

Ресур используется для управления файлами и папками.

Имеет следующие атрибуты:

* `backup` - куда бекапить файл, если он существует

    * `false` - не бекапить

    * `puppet` - значение по умолчанию, бэкапится в какую то специальную папку папета

* `checksum` - алгоритм проверки контрольной суммы

    * `md5` - по умолчанию

    * `md5lite`

    * `sha256`

    * `sha256lite`

    * `mtime`

    * `ctime`

    * `none`

* `checksum_value` - значение контрольной суммы, используется только для md5 и sha256

* `content` - содержимое ресурса

* `ctime` - время создания файла

* `ensure` - состояние

    * `direcory` - папка

    * `link` - создать ярлык/симлинк на файл

    * `present` - файл должен существовать

    * `absent` - файл не должен существовать

    * `file` - файл

* `force` - форсировать действие, например удаление директории с поддиректориями: true/false, yes/no

* `group` - группа пользователей, владельцы

* `ignore` - игнорируемые файлы при рекурсивной обработке каталога

* `links` - как обрабатывать символьные ссылки во время обработки файлов

    * `follow` - скопировать указанный по ссылке файл

    * `manage` - скопировать саму ссылку

    * `ignore` - ничего не делать

* `mode` - права на файл, всегда указывать строкой

* `mtime` - время изменения

* `notify` - уведомить кого-то об изменении ресурса

* `owner` - пользователь, владелец

* `path` - путь к файлу ресурса, по умолчанию равен названию ресурса

* `provider` - бекенд для ресурса

    * `posix`

    * `windows`

* `purge` - удалять ли файлы из директории которых нет на мастере, когда `rescue => true`

    * `true` - в директории будут только те файлы что есть на мастере, остальные удалятся

    * `false` - синхронизирует те файлы, что есть на сервере, остальные останутся без изменений

* `replace` - заменить, если ресурс уже существует

    * `no`

* `require` - зависимости ресурса

* `recurse` - обрабатывать директорию ркурсивно, когда `ensure => 'directory'`

    * `true`

    * `false`

    * `remote` - перебрать каталог рекурсивно на сервере

* `recurselimit` - максимальная глубина рекурсии

* `replace`

* `selinux_ignore_defaults`

* `selrange`

* `selrole`

* `seltype`

* `seluser`

* `show_diff` - отображать различия файлов

* `source` - исходник ресурса

* `source_permissions` - как обрабатывать права на копируемые ресурсы

    * `use` - применить права и владельцев копируемого ресурса

    * `use_when_creating` - применить права и владельца если копируемого файла ещё не существует

    * `ignore` - ничего не делать

* `sourceselect` - задает правила копирования при рекурсивном копировании директории

    * `all` - копируются все файлы из всех доступных источников

    * `first` - по умолчанию, копируется файлы из первого достпного источника

* `target` - путь к символьгной ссылке, если `ensure => 'link'`

* `type`

* `validate_cmd`

* `validate_replacement`


.. code-block:: puppet
    
    # создать папку
    file {
        '/direcory/path':
            ensure => 'directory'
    }


.. code-block:: puppet
    
    # создать файл если его не существует
    file { 
        '/tmp/hello-file':
            ensure  => 'present',
            replace => 'no',
            content => "From Puppet\n",
            mode    => '0644',
    }


.. code-block:: puppet
    
    # создать много директории
    file {
        ['/home/ilnurgi/webiste', '/home/ilnurgi/website/logs/']:
            ensure => 'directory'
    }


.. code-block:: puppet
    
    # уведомление сервиса, при изменнии ресурса
    file {
        '/etc/ssh/sshd_config':
            notify  => Service['sshd'],  # this sets up the relationship
            mode    => '0600',
            owner   => 'root',
            group   => 'root',
            require => Package['openssh-server'],
            content => template('ssh/sshd_config.erb')          
    }


.. code-block:: puppet

    File {
        ensure => 'present',
        owner  => 'root',
        group  => 'root',
        mode   => '0644',
    }

    file {
        '/etc/cobbler/modules.conf':
            content => template('cobbler/modules.conf');
        '/etc/cobbler/dhcp.template':
            content => template('cobbler/dhcp.template');
        '/etc/cobbler/users.digest':
            source => 'puppet:///modules/cobbler/users.digest.live',
            mode   => '0660';
    }


.. code-block:: puppet
    
    file { 
        '/tmp/fakefile':
            content => file('/etc/puppet/modules/yourmodulename/files/fakefile')
    }


.. code-block:: puppet
    
    file { 
        '/tmp/fakefile':
            content =>  file(
                "yourmodulename/fakefile.${::hostname}",
                'yourmodulename/fakefile'
            )
    }