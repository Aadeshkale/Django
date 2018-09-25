from django.contrib import admin
from .models import Std,Sproxy
# admmin model
class AdminStd(admin.ModelAdmin):
    list_display=['sid','name','loc']

class AdminSproxy(admin.ModelAdmin):
    list_display=['sid','name','loc']


# Register your models here.
admin.site.register(Std,AdminStd)
admin.site.register(Sproxy,AdminSproxy)