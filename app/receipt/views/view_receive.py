"""
View for the receiving Order JSON for the application.
"""
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from receipt.models import Check, Printer
from receipt.tasks import create_pdf_file


class ReceiveOrder(APIView):
    def post(self, request, format=None):
        order = json.loads(request.body.decode('utf-8'))
        point_id = order['point_id']
        printers = get_list_or_404(Printer, point_id=point_id)

        if Check.objects.filter(order=order).count() > 0:
            return Response(
                {'order_id': order['id']},
                status=status.HTTP_208_ALREADY_REPORTED
            )

        for printer in printers:
            new_check = Check.objects.create(
                type=printer.check_type,
                order=order,
                printer_id=printer,
            )
            create_pdf_file.apply_async((new_check.id, ))

        return Response(status=status.HTTP_201_CREATED)
