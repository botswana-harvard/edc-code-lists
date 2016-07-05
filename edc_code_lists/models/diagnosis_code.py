from edc_base.model.models import BaseModel

from .code_list_model_mixin import CodeListModelMixin


class DiagnosisCode (CodeListModelMixin, BaseModel):

    class Meta:
        app_label = 'edc_code_lists'
        verbose_name = "Code"
