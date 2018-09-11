from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_registration.backends.activation.views import RegistrationView


@cache_page(settings.CACHE_TTL)
def homepage(request):
    return render(request, 'base/homepage.html')


class CustomRegistrationView(RegistrationView):
    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
