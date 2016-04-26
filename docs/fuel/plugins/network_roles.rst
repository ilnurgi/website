network_roles.yaml - сетевые роли
---------------------------------

Необязательный файл

.. code-block:: yaml

    - id: "name_of_network_role"
      default_mapping: "public"
      properties:
          subnet: true
          gateway: false
          vip:
              - name: "test_a"
                alias: "alias_name"
                namespace: "haproxy"
                node_roles: ["primary-controller", "controller"]
              - name: "test_b"


default_mapping
---------------

Название сети по умолчанию чего-то там


properties
----------

Дополнительные свойства

    * subnet

    * gateway

    * vip - список virtual ip
        
        * name

        * alias

        * namespace

        * node_roles - список ролей нод, где vIP могут быть использованы