from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'pub_date',)
    

admin.site.register(Book, BookAdmin)
