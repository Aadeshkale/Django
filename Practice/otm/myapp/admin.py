from django.contrib import admin
from myapp.models import *
# Register your models here.

class  AdminBook(admin.ModelAdmin):
    list_display=['id','name','year','price']

class AdminAuthor(admin.ModelAdmin):
    list_display=['book_id','name']

admin.site.register(Book,AdminBook)
admin.site.register(Author,AdminAuthor)