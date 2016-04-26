metadata.yaml - метаданные плагина
==================================

Описывает метаданные плгина


authors
-------

.. warning::

    Авторы не должны содержать запятых

.. code-block:: yaml

    authors: ['ilnurgi']


description
-----------

Описание плагина

.. code-block:: yaml
    
    description: Please describe your plugin here


fuel_version
------------

Список версии фуела, которые поддерживает данный плагин

.. code-block:: yaml

    fuel_version: ['8.0']


groups
------

* network
* storage
* storage::cinder
* storage::glance
* hypervisor
* monitoring

.. code-block:: yaml

    groups: ['storage::cinder']


homepage
--------

.. code-block:: yaml

    homepage: 'http://ilnurgi1.ru'


is_hotpluggable
---------------

Включает возможность деплоя данного плагина на уже развернутое окружение

.. code-block:: yaml

    is_hotpluggable: true


licenses
--------

.. code-block:: yaml

    licenses: ['Apache License Version 2.0']


name
----

Название плагина

.. code-block:: yaml

    name: ilnurgi_plugin


package_version
---------------

Версия пакетов плагина, которую использует фуел в работе

.. code-block:: yaml

    package_version: '4.0.0'


releases
--------

Список версии опенстека поддерживаемых плагином
    
    * deployment_scripts_path - путь к папке со скриптами для деплоя

    * mode - ha|multinode 

    * os - название дустрибутива линукс, поддерживаемый плагином

    * repository_path - путь к папке 

    * version - версия опенстека, поддерживаемой плагином

.. code-block:: yaml

    releases:
      - os: ubuntu
        version: liberty-8.0
        mode: ['ha']
        deployment_scripts_path: deployment_scripts/
        repository_path: repositories/ubuntu


title
-----

Человекочитаемое название плагина для веба

.. code-block:: yaml

    title: Title for ilnurgi_plugin plugin


version
-------

Версия плагина

.. code-block:: yaml

    version: '1.0.0'