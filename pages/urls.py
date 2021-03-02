from django.urls import path
from .views import HomePageView, FormPageView, SalirPageView

urlpatterns = [
    path('form',FormPageView.as_view(),name='form'),
    path('',HomePageView.as_view(),name='home'),
    path('exit',SalirPageView.as_view(),name='exit')
]