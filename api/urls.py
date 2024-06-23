from django.urls import path
from . import views

urlpatterns = [
    path('', views.api1),
    path('altropercorso', views.api),
]