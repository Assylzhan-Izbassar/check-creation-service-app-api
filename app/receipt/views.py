"""
All views for the application.
"""
from rest_framework.generics \
    import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PrinterSerializer, CheckSerializer
from .models import Printer, Check


class PrinterList(ListCreateAPIView):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class PrinterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class CheckList(ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class CheckDetail(RetrieveUpdateDestroyAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
