from re import search
import re
from django.contrib import admin , messages
from .models import *
# Register your models here.

class ProjectInline(admin.TabularInline):
    model = Projet

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
    'last_name',
    'first_name'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )
    search_fields = ['last_name']
    #pour ajouter une autre critaire de recherche ['last_name',...]

    inlines = [ProjectInline]

class CoachAdmin(admin.ModelAdmin):
    list_display = (
    'last_name',
    'first_name'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )
    search_fields = ['first_name']

class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name="dure"
    title="durée"
    def lookups (self, request, model_admin):
        return(
            ('1 Month', 'less than 1 month'),
            ('3 Months', 'less than 3 months'),
            ('4 Months', 'greater than 3 months')
        )
    def queryset(self, requet, queryset):
        if self.value() == "1 Month":
            return queryset.filter(dure__lte = 30)
        if self.value() == "3 Month":
            return queryset.filter(dure__gt = 30,
                duree__lte = 90)
        if self.value() == "4 Months":
            return queryset.filter(dure__gt = 90)

def set_Valid(modeladmin, request, queryset):
    rows = queryset.update(isValid= True)
    if rows ==1:
        msg = "1 project was"
    else :
        msg = f"{rows} projects were"
    messages.success(request, message= f"{msg} successfully marked as valid")

set_Valid.short_description = "Validate"



class ProjectAdmin(admin.ModelAdmin):
    def set_inValid(modeladmin, request, queryset):
        number = queryset.filter(isValid= False)
        if number.count() > 0:
            messages.error(request, f"{number.count()} Projects already set to Not Valid")
        else:
            rows = queryset.update(isValid= False)
            if rows == 1 :
                msg ="1 project was"
            else :
                msg = f"{rows} projects were"
            messages.success(request, message=f"{msg} successfully marked as not Valid")
    set_inValid.short_description = "invalidate"
    actions = ['set_inValid', set_Valid]
    actions_on_bottom = True
    actions_on_top = True

    list_filter = (
        'creator',
        'isValid',
        ProjectDurationFilter
    )

    list_display = (
        'project_name',
        'dure',
        'supervisor',
        'creator',
        'isValid'
    )

    fieldsets = [
        (
            None ,
            {
                'fields': ('isValid',)
            }
        ),
        (
            'About',
            {
                'fields': (
                    'project_name',
                    ('creator', 'supervisor'),
                    'besoin',
                    'description'
                    )
            }
        ),
        (
            'Durations',
            {
                'classes':('collapse',),
                'fields' : (
                    'dure',
                    'temp_allocated'
                )
            }
        )
    ]
    #radio_fields = {'supervisor' : admin.VERTICAL}
    autocomplete_fields = ['supervisor']
    empty_value_display = '-empty'
    #readonly_fields=('besoin')

#admin.site.register(Student, StudentAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Projet, ProjectAdmin)
admin.site.register(MemberShip)