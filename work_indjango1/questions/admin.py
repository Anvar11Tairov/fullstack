from django.contrib import admin
from .models import Services, Feddback, Fullfb, Staff
# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']
    search_fields = ['title']
    list_display_links = ['title']
admin.site.register(Services, ServicesAdmin)

class FeddbackAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'email', 'phone', 'text' ]
    search_fields = ['name']
    list_display_links = ['name']

admin.site.register(Feddback, FeddbackAdmin)

class FullfbAdmin(admin.ModelAdmin):
    list_display = ['id', 'name2', 'email2', 'text2']


admin.site.register(Fullfb,FullfbAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position', 'photo']
    list_display_links = ['name']

admin.site.register(Staff, StaffAdmin)