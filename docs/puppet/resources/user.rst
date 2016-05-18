user - управление пользователями
================================


* `comment`

* `ensure` - состояние

    * `present` - должен существовать

    * `absent`

    * `role`

* `gid`

* `groups`

* `home` - домашняя папка

* `managehome` - создать домашнюю папку

    * true - создать

    * false - не создавать

* `password` - пароль

* `password_max_age`

* `password_min_age`

* `shell`

* `uid`


.. code-block:: puppet

    user {
        'ilnurgi':
            ensure           => present,            
            gid              => '501',
            home             => '/home/ilnurgi',
            password         => '!!',
            password_max_age => '99999',
            password_min_age => '0',
            shell            => '/bin/bash',
            uid              => '501',
            comment          => 'Judy Argyle',
            groups           => 'web',
    }