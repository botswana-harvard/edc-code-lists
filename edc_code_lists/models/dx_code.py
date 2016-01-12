from django.db import models
from .base_code_list import BaseCodeList


class DxCode (BaseCodeList):

    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    def __unicode__(self):
        return '%s: %s' % (self.code, self.short_name)

    class Meta:
        app_label = "edc_code_lists"
