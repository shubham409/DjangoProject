from django.contrib import admin

from customadmin.models import Collegs

# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display  = ('name','total_students','branches','location','university')



admin.site.register(Collegs,CustomAdmin)
