from django.contrib import admin
from myapp.models import *

class AdminBook(admin.ModelAdmin):
    list_display=['id','name','author']

class AdminPublisher(admin.ModelAdmin):
    list_display=['id',"name",'book']

admin.site.register(Book,AdminBook)
admin.site.register(Publisher,AdminPublisher)