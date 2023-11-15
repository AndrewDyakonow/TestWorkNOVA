from django.urls import path
from app.apps import AppConfig
from app.views import endpoint

app_name = AppConfig.name

urlpatterns = [
   path('', endpoint, name='app_endpoint'),
]
