from django.contrib.auth.models import User
from django.db import models


class UserActivation(models.Model):
    user_id = models.ForeignKey(User, on_delete='CASCADE', related_name='activations', verbose_name="User")
    activation_key = models.CharField(max_length=32, verbose_name="Activation Key")
    expire = models.DateTimeField(verbose_name="Expire")

    @classmethod
    def send_user_activation(cls, user):
        import string, random
        from django.conf import settings
        from datetime import datetime, timedelta
        exp = getattr(settings, 'ACCOUNT_ACTIVATION_DAYS', 1)

        key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        cls.create(user_id=user, activation_key=key, expire=datetime.now() + timedelta(days=exp))


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

    def __str__(self):
        return self.key
