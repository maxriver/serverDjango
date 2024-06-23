from django.urls import path
from . import views

urlpatterns = [
    path('', views.api),
    path('altropercorso', views.api),
]