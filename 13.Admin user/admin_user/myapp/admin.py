from django.contrib import admin
from .models import Emp


class AdminEmp(admin.ModelAdmin):
    list_display=['id','name','loc','address']

admin.site.register(Emp,AdminEmp)