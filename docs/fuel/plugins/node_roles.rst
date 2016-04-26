node_roles.yaml - описание ролей нод
------------------------------------

Необязательный файл

.. code-block:: yaml

    role_name:
    name: "Some plugin role"tasks
    description: "Some description"
    conflicts:
        - some_not_compatible_role
    limits:
        min: 1
    restrictions:
        - condition: "some logic condition"
          message: "Some message for restriction warning"