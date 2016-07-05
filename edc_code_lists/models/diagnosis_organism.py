from edc_base.model.models import BaseModel

from .code_list_model_mixin import CodeListModelMixin


class DiagnosisOrganism (CodeListModelMixin, BaseModel):

    class Meta:
        app_label = 'edc_code_lists'
