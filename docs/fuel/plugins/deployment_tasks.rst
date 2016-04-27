deployment_tasks.yaml - описание задач
======================================

Данный файлик описывает задачи плагина

.. code-block:: yaml

    - id: task
      type: puppet
      groups: [primary-controller]
      required_for: [keystone]
      requires: [database]
      parameters:
        puppet_manifest: /etc/puppet/modules/osnailyfacter/modular/keystone/db.pp
        puppet_modules: /etc/puppet/modules
        timeout: 1800


groups
------

Описывает группу ролей, на котором будет выполняться указанная таска.

Используется в main группе развертывания

.. warning::

    Не может быть использовано совместно с role
    
.. code-block:: yaml
    
    groups: [primary-controller]


parameters
----------

Описывает дополнительные параметры задачи
    
    * timeout - таймаут выполнения задачи, по умолчанию 300 секунд

    * cmd - для задач, с типом shell, описывает выполняемую задачу
        
        .. code-block:: yaml

            type: shell
            parameters:
                # файл возьмет из папки указанной в metadata.yaml -> releases.deployment_scripts_path
                cmd: shell deploy.sh 

        .. code-block:: yaml
            
            type: shell
            parameters:
                cmd: echo all > /tmp/plugin.all
    
    * puppet_manifest - для задач, с типом puppet, путь к папет манифесту задачи
        
        .. code-block:: yaml
            
            type: puppet
            parameters:
                # Файл должен лежать в папке metadata.yaml -> releases.deployment_scripts_path
                puppet_manifest: puppet/manifests/site.pp
    
    * puppet_modules - для задач, с типом puppet, путь к модулям
        
        .. code-block:: yaml

            type: puppet
            parameters:
                puppet_modules: puppet/modules

    * strategy - стратегия выполняемой задача
        
        Используется для групповых задач

        * amount - макисмальное количесвто задач, выполняемых паралельно
            
            .. code-block:: yaml

                type: group
                parameters:
                    strategy:
                        amount: 6

        * type - тип стратегии

            * parallel - выполнить задачи парарельно

            * one-by-one - выполнить задачи один за другим


reexecute_on
------------

Список чего то, когда таска должна быть запущена повторно

.. code-block:: yaml

    # данная задача выполнится всегда, когда изменится деплой
    - id: my-task
      groups: [primary-controller, controller]
      reexecute_on: [deploy_changes]

requires
--------

Описывает задачи, которые должны быть выполнены перед выполнением данной задачи

.. code-block:: yaml

    requires: [database]


required_for
------------

Описывает задачи, для которых необходима текущая задача

.. code-block:: yaml

    required_for: [keystone]


role
----

Описывает роль, на котором будет выполняться указанная таска. 
    
Используется в группах развертывания pre|post_deployment

.. warning::

    Не может быть использовано совместно с groups
    
.. note::

    Можно задать звездочкой
    

.. code-block:: yaml
    
    role: [controller]

.. code-block:: yaml

    role: '*''

stage
-----

Описывает более детально этап, когда необходимо выполнить задачу

возможные этапы - hw_configuratio, disk_partitioning, network_configuration, software_installation
существующие этапы - pre_deployment, post_deployment
новый этап - monitoring

    Используют конвенцию диапзанов для деплоя
    0 - 999 - настройка железа
    1000 - 1999 зарезервировано на будущее
    2000 - 2999 настройка разделов диска и образов
    3000 - 3999 зарезервировано на будущее
    4000 - 4999 настройка сети
    5000 - 5999 зарезервировано на будущее
    6000 - 6999 деплои софта
    7000 - 7999 зарезервировано на будущее
    8000 - 8999 слежение за деплоем

.. code-block:: yaml

    stage: post_deployment/100

tasks
-----

Список задач, которые выполнит данная задача

Используется для групповой задачи

.. code-block:: yaml
    
    type: group
    tasks: [fuel_pkgs, hiera, globals, tools, logging] 

* type - описывает тип задачи
    
    * group - задача выполняет группу задач

    * pyppet - задача выполняет папит манифест

    * reboot - задача перезагружает ноду

    * shell - задача выполняет какую то шел команду