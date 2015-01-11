from django.contrib import admin
from django.db import models
from students.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    
    save_as = False
    save_on_top = True
    date_hierarchy = 'date_of_birth'
    list_display = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'package', 'dossier']
    list_display_links = ['name', 'surname', 'email']
    list_per_page = 3
    ordering = ['package', 'name']
    list_filter = ['package', 'email', 'phone']
    search_fields = ['name']
    
    prepopulated_fields = {"slug": ("name",)}

    filter_horizontal = ['courses']
    radio_fields = {"package": admin.HORIZONTAL}
    



