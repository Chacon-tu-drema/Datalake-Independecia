from django.urls import path
from . import views

urlpatterns = [
    path('formulario1/', views.formulario, name='formulario1'),
    path('formulario1/calles',views.autocompete_calles, name='autocompete_calles'),
    path('formulario1/pais',views.autocompete_pais, name='autocompete_pais'),
]