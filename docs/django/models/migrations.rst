Миграции
========

.. code-block:: sh

    python manage.py makemigration app_name
    python manage.py migrate app_name
    python manage.py dumpdata app_name --indent=2
    python manage.py loaddata data.json

.. code-block:: py

    def forwards_func(apps, schema_editor):
        # ...
        Model = apps.get_model('shop', model)
        # ...

    def backwards_func(apps, schema_editor):

        # ...
        Model = apps.get_model('shop', model)
        # ...

    class Migration(migrations.Migration):
        dependencies = [
            ('shop', '0002_add_translation_model'),
        ]
        operations = [
            migrations.RunPython(forwards_func, backwards_func),
        ]
