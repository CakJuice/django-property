from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_registration.backends.activation.views import RegistrationView


@cache_page(600)
def homepage(request):
    return render(request, 'base/homepage.html')

class CustomRegistrationView(RegistrationView):
    @method_decorator(cache_page(600))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
