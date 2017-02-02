# coding: utf-8

from django.contrib import admin

from .models import Post, DocsReferenc, File, Category, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = [
        "title", "category", "created", "modified", "published",
    ]

    list_filter = [
        "category"
    ]


class DocsReferencesAdmin(admin.ModelAdmin):

    list_display = [
        "socr", "url"
    ]


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Post, PostAdmin)
admin.site.register(DocsReferenc, DocsReferencesAdmin)
