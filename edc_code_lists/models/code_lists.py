from django.db import models

from edc_base.model.models import BaseModel

from .code_list_model_mixin import CodeListModelMixin


class WcsDxAdult(CodeListModelMixin, BaseModel):

    """WhoClinicalStagingDxAdult"""

    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=100,
        blank=True)

    class Meta:
        app_label = "edc_code_lists"


class WcsDxPed(CodeListModelMixin, BaseModel):

    """WhoClinicalStagingDxPediatric"""

    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=100,
        blank=True)

    class Meta:
        app_label = "edc_code_lists"


class MedicationCode (CodeListModelMixin, BaseModel):
    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"


class BodySiteCode (CodeListModelMixin, BaseModel):
    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"


class OrganismCode (CodeListModelMixin, BaseModel):
    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"


class ArvCode (CodeListModelMixin, BaseModel):
    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"


class ArvDoseStatus (CodeListModelMixin, BaseModel):
    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"


class ArvModificationCode (CodeListModelMixin, BaseModel):
    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    class Meta:
        app_label = "edc_code_lists"
