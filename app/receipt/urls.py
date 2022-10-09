"""
Configuring endpoints for views
"""
from django.urls import path
from .views import view_models, view_receive


urlpatterns = [
    path('printers/', view_models.PrinterList.as_view()),
    path('printers/<str:pk>/', view_models.PrinterDetail.as_view()),
    path('checks/', view_models.CheckList.as_view()),
    path('checks/<int:pk>/', view_models.CheckDetail.as_view()),
    path('checks/create_pdf/', view_receive.ReceiveOrder.as_view()),
]
