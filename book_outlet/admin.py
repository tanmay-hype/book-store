from django.contrib import admin

from.models import Book, Author, Address, Country
from book_outlet import models

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author",)
    list_display = ("title", "author", )



admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
# Register your models here.
