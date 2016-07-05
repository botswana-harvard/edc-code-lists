from django.db import models

from edc_base.model.models import BaseModel

from .code_list_model_mixin import CodeListModelMixin


class SsxCode (CodeListModelMixin, BaseModel):

    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"
