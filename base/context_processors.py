from .models import SiteSetting
from django.core.cache import cache


def site_info(request):
    if request.method == 'GET':
        ctx = {}
        if cache.has_key('settings'):
            ctx = cache.get('settings')
        else:
            settings = SiteSetting.objects.all()
            for setting in settings:
                ctx[setting.key] = setting.value
            cache.set('settings', ctx)

        return ctx
