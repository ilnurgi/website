Viewsets
========

.. code-block:: py

    # views.py

    from rest_framework import viewsets
    from rest_framework.decorators import detail_route

    from .serializers import SomeSerializer

    class SomeModelViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = SomeModel.objects.all()
        serializer_class = SomeSerializer

        def list(self):
            return super().list()

        def retrieve(self):
            return super().retrieve()

        @detail_route(
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
        def enroll(self, request, *args, **kwargs):
            obj = self.get_object()
            # ...
            return Response({'some_attr': True})

.. code-block:: py

    # urls.py

    from django.conf.urls import url, include

    from rest_framework import routers

    from . import views

    router = routers.DefaultRouter()
    router.register('some', views.SomeViewSet)

    urlpatterns = [
        # ...
        url(r'^', include(router.urls)),
    ]