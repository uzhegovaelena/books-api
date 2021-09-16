from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'favorites', 'reviews', 'rating', 'date')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'author')
    list_editable = ('favorites',)
    list_filter = ('favorites', 'rating')




admin.site.register(Book, BookAdmin)
