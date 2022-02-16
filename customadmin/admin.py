from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html

from customadmin.models import Collegs
from django.db.models import Avg
# Register your models here.

from django.contrib.admin import ModelAdmin, SimpleListFilter


class CustomFilter(SimpleListFilter):
    title = "Students Count"  # a label for our filter
    parameter_name = "anything"  # you can put anything here

    def lookups(self, request, model_admin):
        # This is where you create filter options; we have two:
        return [
            ("above_400", "Above 400"),
            ("below_400", "Below 400"),
        ]

    def queryset(self, request, queryset):
        # This is where you process parameters selected by use via filter options:
        if self.value() == "above_400":
            # Get websites that have at least one page.
            return queryset.filter(total_students__gte=400)
        if self.value():
            # Get websites that don't have any pages.
            return queryset.filter(total_students__lte=400)



class CertifiedFilter(SimpleListFilter):
    title = "Certification"
    parameter_name = "anything"

    def lookups(self, request, model_admin):
        return [
            ("Certified", "Certified"),
            ("Not_Certified", "Not Certified"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "Certified":
            return queryset.filter(certified=1)
        if self.value():
            return queryset.filter(certified=0)



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
    list_filter = ('name','branches',CertifiedFilter,CustomFilter,)

    # for searchin values use any lookups here
    search_fields=('name__icontains',)


admin.site.register(Collegs,CustomAdmin)
