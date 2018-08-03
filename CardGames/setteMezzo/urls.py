from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carta/<int:pk>', views.carta_dett, name='carta'),
    path('carta/<int:pk>/new/', views.new_topic, name = 'new_topic'),
]