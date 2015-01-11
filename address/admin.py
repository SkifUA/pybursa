from django.contrib import admin
from address.models import Addres

#admin.site.register(Addres)

@admin.register(Addres)
class AddresAdmin(admin.ModelAdmin):
    
    list_display = ['post_index', 'country', 'region', 'area', 'street', 'build']
    list_display_links = ['post_index', 'country', 'region']
    ordering = ['country', 'region']
    list_filter = ['country', 'region']
    