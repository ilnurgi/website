Представления в виде функции
============================

.. code-block:: py

    from django.http import HttpResponse
    from django.shortcuts import render

    def index(request, good_id):
        """
        :type request: HttpRequest
        """

        return render()

    def hello(request):
        return HttpResponse('Hello world')