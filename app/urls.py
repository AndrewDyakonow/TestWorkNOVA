from django.urls import path
from app.apps import AppConfig
from app.views import endpoint, delete_docs

app_name = AppConfig.name

urlpatterns = [
   path('', endpoint, name='app_endpoint'),
   path('delete/', delete_docs, name='delete_endpoint'),
]
