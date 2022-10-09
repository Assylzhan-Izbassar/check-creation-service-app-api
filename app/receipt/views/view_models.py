"""
All model views for the application.
"""
from rest_framework.generics \
    import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404, render
from receipt.serializers import PrinterSerializer, CheckSerializer
from receipt.models import Printer, Check


class PrinterList(ListCreateAPIView):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class PrinterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class CheckList(ListCreateAPIView):
    queryset = Check.objects.select_related('printer_id').all()
    serializer_class = CheckSerializer


class CheckDetail(RetrieveUpdateDestroyAPIView):
    queryset = Check.objects.select_related('printer_id').all()
    serializer_class = CheckSerializer

    def get(self, request, pk, format=None):
        """
        Render a detail check.
        """
        check = get_object_or_404(Check, pk=pk)
        return render(
            request,
            template_name='checks/check_detail.html',
            context={'check': check}
        )
