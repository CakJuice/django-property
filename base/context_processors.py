from .models import SiteSetting
from django.core.cache import cache


def site_info(request):
    ctx = {}
    if request.method == 'GET':
        if cache.has_key('settings'):
            ctx = cache.get('settings')
        else:
            settings = SiteSetting.objects.all()
            for setting in settings:
                ctx[setting.key] = setting.value
            cache.set('settings', ctx)

    return ctx
