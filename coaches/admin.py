from django.contrib import admin
from coaches.models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'name_cours', 'job_title',
                   'job_status', 'dossier']
    list_display_links = ['name', 'surname', 'email']
    ordering = ['surname', 'name']
    list_filter = ['email', 'phone', 'name_cours']
        
    radio_fields = {"job_title": admin.HORIZONTAL}