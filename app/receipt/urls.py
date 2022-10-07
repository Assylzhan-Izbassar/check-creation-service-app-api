"""
Configuring endpoints for views
"""
from django.urls import path
from . import views


urlpatterns = [
    path('printers/', views.PrinterList.as_view()),
    path('printers/<str:pk>/', views.PrinterDetail.as_view()),
    path('checks/', views.CheckList.as_view()),
    path('checks/<int:pk>/', views.CheckDetail.as_view()),
]
