from django.contrib import admin
from .models import Emp

# Admin model
class AdminEmp(admin.ModelAdmin):
    list_display=['id','name','loc','sal']

# Register your models here.
admin.site.register(Emp)    