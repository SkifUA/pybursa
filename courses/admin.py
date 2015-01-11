
from django.contrib import admin
from courses.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    
    save_as = True
    save_on_top = True
    date_hierarchy = 'date_start'
    list_display = ['name', 'tehnology', 'description', 'teacher', 'assistent', 'date_start', 'date_end']
    list_display_links = ['name', 'date_start', 'tehnology']
    ordering = ['date_start', 'name']
    list_filter = ['teacher', 'assistent', 'date_start']
    search_fields = ['name']
    
    prepopulated_fields = {"slug": ("name",)}

    radio_fields = {"tehnology": admin.HORIZONTAL}

