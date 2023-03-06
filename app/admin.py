from django.contrib import admin
from .models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'link']
    list_filter = ['collector', 'publish', 'created', 'updated']
    search_fields = ['name', 'link']
    ordering = ['-publish']
