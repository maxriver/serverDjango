from django.urls import path
from . import views

urlpatterns = [
    path('', views.api),
    path('altropercorso', views.api), # 3.121.138.195:8000/api/altropercorso
]