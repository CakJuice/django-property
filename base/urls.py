from django.urls import path
from django.views.generic.base import TemplateView
from django_registration.backends.activation import views as registration_views

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    # custom url from django-registration
    path('activate/complete', TemplateView.as_view(template_name='django_registration/activation_complete.html'),
         name='django_registration_activation_complete'),
    path('activate/<str:activation_key>/', registration_views.ActivationView.as_view(),
         name='django_registration_activate'),
    path('signup/', views.CustomRegistrationView.as_view(), name='django_registration_register'),
    path('signup/complete/', TemplateView.as_view(template_name='django_registration/registration_complete.html'),
         name='django_registration_complete'),
    path('signup/closed/', TemplateView.as_view(template_name='django_registration/registration_closed.html'),
         name='django_registration_disallowed'),
]
