from django.contrib import admin

from ..models import DxCode, WcsDxAdult, WcsDxPed


class DxCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'short_name')
    search_fields = ('code', 'short_name', 'long_name')
admin.site.register(DxCode, DxCodeAdmin)


class WcsDxAdultAdmin(admin.ModelAdmin):
    list_display = ('code', 'short_name')
    search_fields = ('code', 'short_name', 'long_name')
admin.site.register(WcsDxAdult, WcsDxAdultAdmin)


class WcsDxPedAdmin(admin.ModelAdmin):
    list_display = ('code', 'short_name')
    search_fields = ('code', 'short_name', 'long_name')
admin.site.register(WcsDxPed, WcsDxPedAdmin)
