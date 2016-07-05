from django.db import models

from edc_base.model.models import BaseModel

from .code_list_model_mixin import CodeListModelMixin


class DxCode (CodeListModelMixin, BaseModel):

    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    def __unicode__(self):
        return '%s: %s' % (self.code, self.short_name)

    class Meta:
        app_label = "edc_code_lists"
