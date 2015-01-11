from django.contrib import admin
from dossier.models import Dossier

#admin.site.register(Dossier)
@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
            
    list_display = ['color', 'address']
    list_display_links = ['color', 'address']
    
    ordering = ['color']
    list_filter = ['address', 'color']

    filter_vertical = ['courses']
    radio_fields = {"color": admin.HORIZONTAL}
    
    