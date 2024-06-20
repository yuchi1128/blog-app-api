from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:pk>/', views.article),
    path('', views.index)
]
