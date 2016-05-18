package - управление системными пакетами
========================================

* `adminfile` - используется в Solaris

* `allow_virtual` - true/false, yes/no

* `allowcdrom`

* `category`

* `configfiles`

* `description`

* `ensure` - состояние 

    * 'installed' - должен быть установлен

    * 'latest' - должна быть установлена последняя версия пакета
    
    * 'absent' - пакет не должен быть установлен, но конфиги могут быть
    
    * 'purged' - пакет не должен быть установлен и конфигов не должно быть

    * `held`

* `flavor` - OpenBSD

* `install_options` - список опции для установки пакета

* `instance`

* `name` - название пакета, по умолчанию равен названию ресурса

* `package_settings`

* `platform`

* `provider` - поставщик пакетов

    * `aix`

    * `appdmg`

    * `apple`

    * `apt`

    * `aptitude`

    * `aptrpm` - поставщик apt

    * `blastwave`

    * `dnf`

    * `dpkg`

    * `fink`

    * `freebsd`

    * `gem` - поставщик руби пакетов

    * `hpux`

    * `macports`

    * `nim`

    * `openbsd`

    * `opkg`

    * `pacman`

    * `pip3`

    * `pip`

    * `pkg`

    * `pkgdmg`

    * `pkgin`

    * `pkgng`

    * `pkgutil`

    * `portage`

    * `ports`

    * `portupgrade`

    * `puppet_gem`

    * `rpm`

    * `rug`

    * `sun`

    * `sunfreeware`

    * `up2date`

    * `urpmi`

    * `windows`

    * `yum`

    * `zypper`

* `reinstall_on_refresh`

* `require` - зависимости пакета

* `responsefile`

* `root`

* `source` - путь, откуда можно взять пакет

* `status`

* `uninstall_options`

* `vendor`


.. code-block:: puppet
    
    # в системе должен быть пакет
    package {
        'mc':
            ensure => 'installed'
    }


.. code-block:: puppet
    
    # настройка глобальных параметров
    Package { ensure => 'installed' }

    package { 'screen': }
    package { 'strace': }
    package { 'sudo': }


.. code-block:: puppet

    package {   
        ['screen', 'strace', 'sudo']: 
            ensure => 'installed' 
    }
    