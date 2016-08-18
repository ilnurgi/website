rest_framework
==============

* api - пакет с апи приложения

    * __init__.py - пакет

    * serializers.py

    * views.py

    * urls.py

.. code-block:: sh

    pip install djangorestframework

.. code-block:: py

    # settings.py

    INSTALLED_APPS = (
        # ...,
        'rest_framework',
    )

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        ]
    }

.. toctree::
    :maxdepth: 1

    serializers
    generics
    viewsets
    permissions