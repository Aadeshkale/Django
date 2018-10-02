from django.contrib import admin
from .models import Student,Author,Publisher,Book

# admin models

class AdminStudent(admin.ModelAdmin):
    list_display=['sname','sfee']
class AdminPublisher(admin.ModelAdmin):
    list_display=['pname','email']
class AdminAuthor(admin.ModelAdmin):
    list_display=['aname','aemail']
class AdminBook(admin.ModelAdmin):
    list_display=['bname','bprice']    


# Register your models here.

admin.site.register(Student,AdminStudent)
admin.site.register(Author,AdminAuthor)
admin.site.register(Publisher,AdminPublisher)
admin.site.register(Book,AdminBook)