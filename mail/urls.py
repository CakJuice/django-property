from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.mail_create, name='mail_create'),

    path('attachment/create/', views.attachment_create, name='attachment_create')
]