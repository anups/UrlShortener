
from django.urls import path
from . import views

app_name = "urlapp"

urlpatterns = [
    path('', views.url_form, name='url_form'),
]
