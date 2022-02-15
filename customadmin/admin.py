from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html

from customadmin.models import Collegs
from django.db.models import Avg
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    # for multiple column 
    list_display  = ('name','good_or_not','total_students','branches','location','university','ranking','student_strength','is_certified')

    def good_or_not(self,obj):
        return obj.ranking <=4
    good_or_not.boolean = True
    good_or_not.short_description = 'Take Admission Or Not'


    def is_certified(self,obj):
        return obj.certified == 1
    is_certified.boolean = True
    is_certified.short_description = 'Certified Collage Or Not'

    def student_strength(self, obj):
        average_students = Collegs.objects.aggregate(Avg('total_students'))
        ans =None
        if(obj.total_students> average_students['total_students__avg']):
            ans= 'Above Average'
        else:
            ans= 'Below Average'
        return format_html("<b><i>{}</i></b>",ans)

    def make_certified(modeladmin, request, queryset):
        queryset.update(certified = 1)
        messages.success(request, "Certified The Selected Colleg Successfully !!")
  
    def make_noncertified(modeladmin, request, queryset):
        queryset.update(certified = 0)
        messages.success(request, "Removed Certificate Of The Selected Colleg Successfully !!")
  
    def filter_certified(modeladmin, request, queryset):
        queryset.filter(certified = 1)
        messages.success(request, "Filtered Certified Successfully !!")
    



    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    
    admin.site.add_action(make_certified, "Make Certified")
    admin.site.add_action(make_noncertified, "Make Non Cerfied")
    admin.site.add_action(filter_certified, "Filter Certified")

    

    # for filters
    list_filter = ('name','branches')

    # for searchin values use any lookups here
    search_fields=('name__icontains',)



admin.site.register(Collegs,CustomAdmin)
