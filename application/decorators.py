# coding: utf-8

from django.shortcuts import redirect


def superuser_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return func(request, *args, **kwargs)
        return redirect('/')
    return wrapper


def superuser_required_in_view(func):
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return func(self, request, *args, **kwargs)
        return redirect('/')
    return wrapper

