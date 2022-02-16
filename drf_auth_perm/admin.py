from django.contrib import admin

from drf_auth_perm.models import Students

# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','branch']