from django.db import models


class CodeListModelMixin(models.Model):

    code = models.CharField(
        verbose_name="Code",
        max_length=15,
        unique=True)

    short_name = models.CharField(
        verbose_name="Name",
        max_length=35)

    long_name = models.CharField(
        verbose_name="Long Name",
        max_length=255,
        blank=True)

    def __str__(self):
        return "{}".format(self.short_name)

    class Meta:
        abstract = True
