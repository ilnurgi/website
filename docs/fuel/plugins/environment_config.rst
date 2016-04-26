environment_config.yaml - переменные окружения, доступные для редактирования через веб
======================================================================================

attributes
----------

Содержит все переменные, для редактирования

.. code-block:: yaml

    attributes:
        metadata:
            role: 'other'
        ilnurgi_plugin_text:
            value: 'Set default value'
            label: 'Text field'
            description: 'Description for text field'
            weight: 25
            type: "text"


metadata
--------

Какая то метаинформация

    * group - группа в вебе, в которой должны отобразиться атрибуты

        * general
        * security
        * compute
        * network
        * storage
        * logging
        * openstack_services
        * other

    * restrictions - накладывает какую то логику на атрибут. По какому то условию можно что-то сделать.

        Поддерживаемые действия

        * condition - какое то улсовие
        * action - действие, если условие истинно
            * disable - атрибут не редактируем в вебе
            * hide - скрывает атрибут из веба
            * message - отображает сообщение
            * none - при наведении мышкой отобразит предупреждение
        * messages - отображает сообщение
        * strict - включает показ ошибок, если атрибуты в условии не доступны, иначе эти атрибуты просто равны null

        .. code-block:: yaml

            attribute: 
                metadata:
                    restrictions:
                        - condition: "not (cluster:net_provider == 'neutron' and networking_parameters:segmentation_type == 'vlan')"
                          message: "Please use Neutron with VLAN segmentation, the only network type supported with Contrail plugin."

.. code-block:: yaml

    attributes:
        metadata:
            group: 'other'

        ilnurgi_plugin_text:
            value: 'Set default value'
            label: 'Text field'
            description: 'Description for text field'
            weight: 25
            type: "text"


Описание атрибутов:


description
-----------

Это описание отобразится как description для поля изменения значение в вебе

.. code-block:: yaml

    attribute:
        description: 'Description for text field'


label
-----

Это описание отобразится как label в форме

.. code-block:: yaml

    attribute:
        label: 'Text field'


regex
-----

Регулярное выражение для валидации введенного значения

.. code-block:: yaml

    attribute:
        regex:
            source: '?\d+$'
            error: "error message"


restrictions
------------

Накладывает какую то логику на атрибут. По какому то условию можно что-то сделать.

Поддерживаемые действия

* condition - какое то улсовие
* action - действие, если условие истинно
    * disable - атрибут не редактируем в вебе
    * hide - скрывает атрибут из веба
    * message - отображает сообщение
    * none - при наведении мышкой отобразит предупреждение
* messages - отображает сообщение
* strict - включает показ ошибок, если атрибуты в условии не доступны, иначе эти атрибуты просто равны null

.. code-block:: yaml

    attribute: 
        restrictions:
            - condition: "settings:some-plugin.attribute.value != 'true'"
              action: "hide"
            - condition: "settings:common.libvirt_type.value != 'kvm'"
              message: "KVM only is supported"
            - condition: "not ('experimental' in version:feature_groups)"
              action: hide
            - condition: "settings:other_plugin == null or settings:other_plugin.metadata.enabled != true"
              strict: false
              message: "Other plugin must be installed and enabled"

type
-----

Тип атрибута. 

Для каждого типа в вебе рисуется свой контрол

    * text
    * checkbox
    * radio
    * password
    * select

.. code-block:: yaml

    attribute:
        type: 'text'


value
-----

Значение атрибута по умолчанию

.. code-block:: yaml

    attribute:
        value: 'Set default value'


values
------

Значения для выбора, например для radio, select

.. code-block:: yaml

    attribute:
        type: radio
        values: 
            - data: "true"
              label: "True"
              description: "description1"
            - data: "false"
              label: "False"
              description: "description2"


weight
------

Ширина для поля изменения значения

.. code-block:: yaml

    attribute:
        weight: 25