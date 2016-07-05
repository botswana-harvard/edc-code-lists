from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models import DiagnosisCode, DiagnosisOrganism, DiagnosisSite, DxCode, WcsDxAdult, WcsDxPed


class EdcCodeListsAdminSite(AdminSite):
    site_header = 'Code Lists'
    site_title = 'Code Lists'
    index_title = 'Code Lists Administration'
    site_url = '/'
edc_code_lists_admin = EdcCodeListsAdminSite(name='edc_code_lists_admin')


@admin.register(DiagnosisCode, site=edc_code_lists_admin)
class DiagnosisCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(DiagnosisOrganism, site=edc_code_lists_admin)
class DiagnosisOrganismAdmin(admin.ModelAdmin):
    pass


@admin.register(DiagnosisSite, site=edc_code_lists_admin)
class DiagnosisSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(DxCode, site=edc_code_lists_admin)
class DxCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'short_name')
    search_fields = ('code', 'short_name', 'long_name')


@admin.register(WcsDxAdult, site=edc_code_lists_admin)
class WcsDxAdultAdmin(admin.ModelAdmin):
    list_display = ('code', 'short_name')
    search_fields = ('code', 'short_name', 'long_name')


@admin.register(WcsDxPed, site=edc_code_lists_admin)
class WcsDxPedAdmin(admin.ModelAdmin):
    list_display = ('code', 'short_name')
    search_fields = ('code', 'short_name', 'long_name')
