from django.contrib import admin

from ..models import DiagnosisCode
from ..models import DiagnosisOrganism
from ..models import DiagnosisSite


class CodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(DiagnosisCode, CodeAdmin)


class OrganismAdmin(admin.ModelAdmin):
    pass
admin.site.register(DiagnosisOrganism, OrganismAdmin)


class SiteAdmin(admin.ModelAdmin):
    pass
admin.site.register(DiagnosisSite, SiteAdmin)
