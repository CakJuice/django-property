from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.mail_create, name='mail_create')
]