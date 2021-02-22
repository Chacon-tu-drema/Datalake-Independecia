from django.urls import path
from . import views

urlpatterns = [
    path('formulario1/', views.formulario, name='formulario1'),
]