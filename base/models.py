from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    created_by = models.ForeignKey(User, on_delete='RESTRICT', related_name='+', verbose_name="Created By")
    updated_by = models.ForeignKey(User, on_delete='RESTRICT', related_name='+', verbose_name="Updated By")

    class Meta:
        abstract = True


class SiteSetting(BaseModel):
    key = models.CharField(max_length=64, unique=True, verbose_name="Key")
    value = models.CharField(max_length=200, verbose_name="Value", null=True, blank=True)
