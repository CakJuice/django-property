from django.contrib.auth.models import User
from django.conf import settings


def get_admin_user():
    user_id = getattr(settings, 'ADMIN_USER_ID', 1)
    return User.objects.get(pk=user_id)
