from django.contrib import admin
from menu.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'named_url', 'menu_name']
    list_filter = ['menu_name']
    search_fields = ['title']


admin.site.register(MenuItem, MenuItemAdmin)
