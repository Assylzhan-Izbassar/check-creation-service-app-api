"""
View for retrieving new checks and download them.
"""
import zipfile
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from receipt.models import Check
from receipt.tasks import send_to_print


FILE_ROOT_PATH = '/app/media/'
FILE_NAME = 'app.zip'


class NewChecks(APIView):
    def get(self, request, printer_id, format=None):
        new_checks = Check.objects.filter(printer_id=printer_id, status='P')

        if not new_checks:
            return Response(status=status.HTTP_404_NOT_FOUND)

        check_pdfs = []
        for check in new_checks:
            check_pdfs.append(check.pdf_file.name)

        response = HttpResponse(content_type='application/zip')

        with zipfile.ZipFile(
            response,
            mode='w',
            compression=zipfile.ZIP_DEFLATED
        ) as archive:
            for file in check_pdfs:
                archive.write(FILE_ROOT_PATH + file)

        response['Content-Disposition'] = f'attachment; filename={FILE_NAME}'

        send_to_print.apply_async((printer_id,))

        return response
