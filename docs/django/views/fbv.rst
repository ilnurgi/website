Представления в виде функции
============================

.. code-block:: py

    from django.contrib.admin.decorators import login_required
    from django.http import HttpResponse
    from django.shortcuts import render

    @login_required
    def index(request, good_id):
        """
        :type request: HttpRequest
        """

        return render()

    def hello(request):
        return HttpResponse('Hello world')