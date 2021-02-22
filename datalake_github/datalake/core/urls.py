from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name="core-home"),
  path('quienes/',views.quienes,name="core-quienes"),
  path('qya/',views.qya,name="core-qya"),
]