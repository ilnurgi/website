volumes.yaml - описание дисков
==============================

.. code-block:: yaml

    volumes:
      - id: "role_volume_name"
        type: "vg"
        min_size: {generator: "calc_min_os_size"}
        label: "Role specific volume"
        items:
          - mount: "/"
            type: "lv"
            name: "root"
            size: {generator: "calc_total_root_vg"}
            file_system: "ext4"
          - mount: "swap"
            type: "lv"
            name: "swap"
            size: {generator: "calc_swap_size"}
            file_system: "swap"
    volumes_roles_mapping:
      role_name:
        - {allocate_size: "min", id: "os"}
        - {allocate_size: "all", id: "role_volume_name"}  