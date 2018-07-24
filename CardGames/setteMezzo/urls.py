from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('carta/<int:pk>', views.carta_dett, name='carta')
]