from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lapotomatis/', views.lapgen, name='report_gen'),
]

