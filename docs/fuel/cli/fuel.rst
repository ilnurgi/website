fuel - консольная утилита управления
====================================

* --env <env> <node????>

* --node <node1, node2,....>

* --provision - выделяет реусрсы для деплоя

* --deploy - деплоит окружение на ноды

    Логи деплоя можно посмотреть в /var/log/docker-logs/astute/astute.log

.. code-block:: sh

    fuel --env 1 node --provision --node 1,2
    fuel --env 1 node --deploy --node 1,2


deploy-changes
--------------

* --env, --env-id <env>

.. code-block:: sh

    fuel --env 1 deploy-changes


deployment - работа с деплоем
-----------------------------

* --dir <dir>
* --env, --env-id <env> - фильтрация по окружению
* --node <node, ...> - фильтрация по ноде
* --defualt - скачать дефолтный конфиг
* --delete - удалить деплой
* --download, -d
* --upload, -u


.. code-block:: sh

    # скачать дефолтный конфиг деплоя, скачается в папку deployment_1
    fuel deployment --default --env 1     

    fuel deployment --download --env 1
    
    fuel deployment --upload --env 1 --dir path/to/some/directory
    
    fuel deployment --upload --env 1 


environment, env - работа с окружениями
--------------------------

* --env, --env-id <env>
* --dir <dir>
* --name, --env-name <name> - название окружения
* --mode <mode> - ???
* --network-mode <mode> - ???
* --nst, --net-segment-type <gre,vlan,tun>
* --release, -rel <rel>
* --attributes
* --create, -c, --env-create
* --delete
* --deployment-tasks
* --download, -d
* --force, -f
* --list
* --set
* --update, --env-update
* --upload, -u

.. code-block:: sh
        
    fuel env
    fuel env --name test --rel 1 --mode multinode --network-mode nova --create
    fuel env --name MyEnv --rel 1 --net-segment-type vlan --create
    fuel env --name MyEnv --rel 1 --create

    fuel env --env 1 --attributes --download
    fuel env --env 1 --attributes --upload

    fuel env --env 1 --deployment-tasks --download
    fuel env --env 1 --deployment-tasks --upload

    fuel env --env 1 --update --release 1
    
    fuel env --env 1 --name NewEnvName --set
    
    fuel env --env 1 --force --delete
    


fuel-version - версия
---------------------

.. code-block:: sh

    fuel fuel-version


graph - работа с графами
------------------------

* --dir <dir> - папка, куда срендерится граф
* --end <task> - конечная точка обхода графа
* --env, --env-id <env>
* --parents-for <task> - вернуть родительскую задачу для задачи
* --render <input> - рендерит граф из DOT в PNG
* --remove <skipped,group,stage> - удаляет задачи из графа
* --skip <task, ...> - пропускаемые задачи
* --start <task> - начальная точка обхода графа
* --tasks <task, ...> - выполняемые задачи 
* --download, -d - скачивает граф
* --tred - фильтр, для уменьшения графа

.. code-block:: sh

    # скачать деплой граф
    fuel graph --env 1 --download
    fuel graph --env 1 --download --tasks A B C
    fuel graph --env 1 --download --skip X Y --end pre_deployment
    fuel graph --env 1 --download --skip X Y --start post_deployment
    fuel graph --render graph.gv
    fuel graph --render graph.gv --dir ./output/dir/
    fuel graph --render graph.gv --tred
    fuel graph --render graph.gv --dir ./output/dir/ --tred


health
------

* --check <check>
* --env, --env-id <env>
* --list, -l
* --force, -f

.. code-blcok:: sh

    fuel health --env 1 --check smoke,sanity
    fuel health --env 1 --list
    fuel health --env 1
    


network - работа с сетью
-------------------------

* --env <env>
* --dir <dir> - папка с данными сети
* --download, -d - скачать текущие конфиги
* --upload, -u - загрузить новые конфиги
* --verify, -v - проверить конфиги

.. code-block:: sh

    fuel network --verify --env 1 --dir .
    fuel network --download --env 1
    fuel network --upload --env 1 --dir . 


network-group
-------------

* --cidr <cidr>
* --env, --env-id <env>
* --gateway <gateway>
* --meta <meta>
* --name, --env-name <name>
* --network <network>
* --nodegroup, --node-group <nodegroup>
* --release, --rel <release>
* --vlan <vlan>
* --create, -c
* --delete
* --list, -l
* --set, -s

.. code-block:: sh

    fuel network-group --node-group 1 --name "new network" --release 2 --vlan 100 --cidr 10.0.0.0/24 --create 
    fuel network-group --node-group 2 --name "new network" --release 2 --vlan 100 --cidr 10.0.0.0/24 --gateway 10.0.0.1 --meta 'meta information in JSON format' --create
    fuel network-group --network 1 --name new_name --set 
    fuel network-group --list
    fuel network-group --node-group 1
    fuel network-group --delete --network 1
    fuel network-group --delete --network 2,3,4


network-template - сетевые шаблоны
----------------------------------

* --env <env>
* --dir <dir>
* --delete
* --download, -d
* --upload, -u

.. code-block:: sh

    fuel network-template --env 1 --delete
    fuel network-template --env 1 --download
    fuel network-template --env 1 --dir path/to/directory --upload


node - работа с нодами
----------------------

* --dir <dir>
* --end <task> - конечная задача деплоя
* --env, --env-id <env> - фильтрация по окружению
* --hostname <hostname>
* --name <name>
* --node <node, ...> - фильтрация по конкретным нодам
* --role, -r <role>
* --skip <task, ...>
* --start <task> - начальная задача деплоя
* --tasks <task, ...>
* --all
* --default
* --delete
* --delete-from-db
* --deploy
* --download, -d
* --disk
* --force, -f
* --list, -l - список нод
* --network, --net
* --provision - подготовить ноду к деплою ???
* --set, -s - задание свойств ноде
* --upload, -u

.. code-block:: sh

    fuel node --node-id 1 --name NewName

    fuel node --set --env 1 --node 1 --role controller
    fuel node --set --env 1 --node 2,3,4 --role compute,cinder
    
    # готовим ноду к деплою
    fuel node --provision --node-id 2 

    # деплоим ноду
    fuel node --deploy --node-id 2
    
    fuel node --node-id 1 --hostname ctrl-01
    
    # список всех нод    
    fuel node

    # список нод окружения
    fuel node --env-id 1

    # информация по конкретной ноде
    fuel node --node-id 80:ac

    fuel node remove --node-id 80:ac,5d:a2
    
    fuel node --disk --default --node-id 2
    fuel node --network --download --node-id 2--dir path/to/directory

    fuel node --network --upload --node-id 2
    fuel node --disk --upload --node-id 2 --dir path/to/directory
    
    fuel node remove --env 1 --node 2,3

    fuel node remove --node 2,3,6,7

    fuel node remove --env 1 --all
    
    fuel node --delete-from-db --node-id 1
    fuel node --delete-from-db --node-id 1 2
    fuel node --delete-from-db --force --node-id 1

    fuel node --node 2 --tasks hiera netconfig
    fuel node --node 2 --skip hiera netconfig
    fuel node --node 2 --skip rsync --end pre_deployment
    
    # запустить деплой ноды до указанной задачи
    fuel node --node 2 --end netconfig

    # запустить деплой с указанной задачи
    fuel node --node 2 --start post_deployment

    # выполнить деплой в промежутке указанных задач
    fuel node --node 2 --start hiera --end neutron

    # запустить деплой, но пропустить некоторые задачи
    fuel node --env 2 --node 3 --end post_deployment_end --skip firewall

    # запустить деплой, но выполнить только указанные задачи
    fuel node --env 2 --node 3 --tasks openstack-network-compute
        
    fuel node set --node 1 --env 1 --role controller
    fuel node set --node 2 --env 1 --role compute,cinder


nodegroup
---------

* --env <env>
* --group <group>
* --name <name>
* --node <node, ...>
* --assign
* --create
* --delete
* --list

.. code-block:: sh

    fuel nodegroup
    fuel nodegroup --env 1 --name "group 1" --create
    
    fuel nodegroup --group 1 --delete 
    fuel nodegroup --group 2,3,4 --delete 
    
    fuel nodegroup --env-id 1
    
    fuel nodegroup --node 1 --group 1 --assign 
    fuel nodegroup --node 2,3,4 --group 1 --assign 


notify - работа с веб уведомлениями
-----------------------------------

* --send, -m [SEND ...]
* --topic - discover,done,error,warning,release

.. code-block:: sh

    fuel notifications --send "message" --topic done


notifications
-------------

* --all
* --mark-as-read, -r <mark-as-read, ...>
* --send <send>
* --topic <discover,done,error,warning,release>
* --list, -l

.. code-block:: sh
    
    fuel notifications --send "message" --topic done
    
    fuel notifications --mark-as-read 1 2
    fuel notifications -r 1 2
    
    fuel notifications
    fuel notifications --list


openstack-config - настройка опенстека
--------------------------------------

* --config-id <config-id>
* --env <env>
* --env-id <env-id>
* --file <file>
* --node <node>
* --node-id <node-id>
* --role <role>
* --delete - удалить конфиги
* --deleted - возвращать удаленые конфиги
* --download, -d - скачать текущие конфиги
* --execute - применить конфиги
* --force, -f - форсировать конфигурацию
* --list, -l - список конфигурации
* --upload

.. code-blosk:: sh

    # деплой конфигурации
    fuel openstack-config --execute --env 1
    fuel openstack-config --execute --env 1 --node 1
    fuel openstack-config --execute --env 1 --role controller
    fuel openstack-config --execute --env 1 --force

    # загрузка конфигурации из файла
    fuel openstack-config --upload --env 1 --file config.yaml
    fuel openstack-config --upload --env 1 --node 1 --file config.yaml
    fuel openstack-config --upload --env 1 --role controller --file config.yaml
    
    # удалить существующие конфиги
    fuel openstack-config --delete --config 1
    
    # список доступнх конфигурации
    fuel openstack-config --list --env 1
    fuel openstack-config --list --env 1 --node 1
    fuel openstack-config --list --env 1 --deleted
    
    # скачать существующие конфиги
    fuel openstack-config --download --config-id 1 --file config.yaml



plugins - работа с плагинами
----------------------------

* --downgrade <plugin_file> - откатывает установленный плагин

    Откатывать можно только минорные версии, например 2.0.1 можно откатить до 2.0.0, но нельзя до 1.0.0.

    .. versionadded:: package_version 2.0.0

* --force, -f - форсировать

* --install <plugin_file> - установка и регистрация плагина

    Плагин установится в /var/www/naigun/plugins/

* --list, -l - список всех зарегистрированных плагинов

* --plugin, --plugin-id <plugin, ...> - плагины

* --remove <plugin_name==plugin_version> - удаление и разрегистрация плагина

* --register <plugin_name==plugin_version> - регистрация плагина

* --sync - синхронизирует плагин с апи сервисами

* --update <plugin_file> - обновление установленного плагина

    Обновлять можно только минорные версии, например 2.0.0 можно обновить до 2.0.1, но нельзя до 2.1.0

    .. versionadded:: package_version 2.0.0

* --unregister <plugin_name==plugin_version> - разрегистрация плагина
    

.. code-block:: sh
    
    fuel plugins --unregister plugin-name==1.0.1

    fuel plugins --downgrade plugin-name-2.0-2.0.1-0.noarch.rpm

    fuel plugins --install plugin_name.rpm
        
    fuel plugins
    fuel plugins --list

    fuel plugins --remove plugin-name==1.0.1

    fuel plugins --register plugin-name==1.0.1

    fuel plugins --sync
    fuel plugins --sync --plugin-id=1,2

    fuel plugins --update plugin-name-2.0-2.0.1-0.noarch.rpm


provisioning - вычисленные значения оркестрации
-----------------------------------------------

* --env, --env-id <env>
* --dir <dir>
* --node <node, ...>
* --delete
* --download, -d
* --upload, -u
* --default

.. code-block:: sh

    fuel provisioning --env 1 --default
    fuel provisioning --env 1 --download
    fuel provisioning --env 1 --upload
    fuel provisioning --env 1 --node 1,2,3 --default 
    fuel provisioning --env 1 --dir path/to/some/directory --upload 


release, rel
------------

* --dir <dir>
* --filepattern, --fp, --file-pattern <filepattern>
* --release, --rel <release>
* --deployment-tasks
* --download, -d
* --list, -l
* --network, --net
* --sync-deployment-tasks
* --upload, -u

.. code-block:: sh

    fuel rel --deployment-tasks --download --rel 1
    fuel rel --deployment-tasks --upload--rel 1
        
    fuel rel --sync-deployment-tasks --dir /etc/puppet/2014.2-6.0/
    fuel rel --sync-deployment-tasks --fp '*tasks.yaml'

    fuel rel --sync-deployment-tasks

    fuel rel --network --download --rel 1
    fuel rel --network --upload --rel 2
    
    fuel release --list

    fuel release --rel 1


reset
-----

* --env, --env-id <env>

.. code-block:: sh

    fuel reset --env 1


role - работа с ролями
----------------------

* --file <file>
* --release, --rel <rel>
* --role <role>
* --create, -c, --env-create
* --delete
* --list, -l
* --update

.. code-block:: sh

    fuel role --rel 2
    name
    ---
    compute
    controller
    .....


    fuel role --rel 2 --role virt --file virt.yaml
    
    # создать роль из файла
    fuel role --rel 1 --file some.yaml --create 
    
    # обновить роль из файла
    fuel role --rel 1 --file some.yaml --update 
    
    # список ролей
    fuel role --rel 1
    
    # сохранить все роли в файл
    fuel role --rel 1 --role controller --file some.yaml
    
    # удалить роль
    fuel role --role controller --rel 1 --delete


settings
--------

* --env, --env-id <env>
* --dir <dir>
* --default
* --download, -d
* --upload, -u

.. code-block:: sh
    
    fuel settings --upload --env 1 --dir path/to/directory
    
    fuel settings --download --env 1
    
    fuel settings --default --env 1 --dir path/to/directory


snapshot
--------

* --dir <dir>
* --conf

.. code-block:: sh

    fuel snapshot
    fuel snapshot --dir path/to/directory
    fuel snapshot --conf > dump_conf.yaml
    fuel snapshot --conf --json
    fuel snapshot < conf.yaml


stop
----

* --env, --env-id <env>

.. code-block:: sh

    fuel stop --env 1


task
----

* --task, --task-id <task, ...>
* --delete
* --force, -f
* --list, -l
    
.. code-block:: sh

    fuel task

    fuel task --task-id 1,2,3
    
    fuel task --delete --task-id 1,2,3

    fuel task --delete -f --task-id 1,6


token 
-----

.. code-block:: sh

    fuel token


user
----

* --newpass, --new-pass <newpass>
* --change-password

.. code-block:: sh

    fuel user change-password


vmware-settings
---------------

* --dir <dir>
* --env, --env-id <env>
* --default
* --download, -d
* --upload, -u

.. code-block:: sh
    
    fuel vmware-settings --download --env 1
    
    fuel vmware-settings --default --env 1 --dir path/to/directory
    
    fuel vmware-settings --upload --env 1 --dir path/to/directory
