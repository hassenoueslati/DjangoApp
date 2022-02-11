from re import search
from django.contrib import admin
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

class ProjectAdmin(admin.ModelAdmin):
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