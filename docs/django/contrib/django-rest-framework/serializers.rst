Сериализаторы
=============

.. code-block:: py

    # serializers.py

    from rest_framework import serializers
    from ..models import Subject

    class RelatedObjectSerializer(serializers.ModelSerializer)

        class Meta:
            model = SomeModel
            fields = ('...', '...', )

    class SubjectSerializer(serializers.ModelSerializer)

        related_object = RelatedObjectSerializer(many=True, read_only=True)

        class Meta:
            model = Subject
            fields = ('id', 'title', 'slug', 'related_object')

.. py:class:: rest_framework.serializers.HyperlinkedModelSerializer()

.. py:class:: rest_framework.serializers.ModelSerializer()

.. py:class:: rest_framework.serializers.Serializer()
