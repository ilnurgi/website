Женерики
========

.. code-block:: py

    # views.py

    from rest_framework.authentication import BasicAuthentication
    from rest_framework import generics
    from rest_framework.permissions import IsAuthenticated

    from ..models import Subject

    from .serializers import SubjectSerializer

    class SubjectListView(generics.ListAPIView):
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer

    class SubjectDetailView(generics.RetrieveAPIView):
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer
        authentication_classes = (BasicAuthentication,)
        permission_classes = (IsAuthenticated,)

.. code-block:: py

    # urls.py

    from django.conf.urls import url

    from . import views

    urlpatterns = [
        url(
            r'^subjects/$',
            views.SubjectListView.as_view(),
            name='subject_list',
        ),
        url(
            r'^subjects/(?P<pk>\d)/$',
            views.SubjectDetailView.as_view(),
            name='subject_detail',
        ),
    ]

.. py:class:: rest_framework.generics.APIView()

.. py:class:: rest_framework.generics.ListAPIView()

.. py:class:: rest_framework.generics.RetrieveAPIView()