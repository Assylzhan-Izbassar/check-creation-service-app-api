"""
View for retrieving new checks and download them.
"""
from email import header
from wsgiref import headers
import zipfile
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from receipt.models import Check


class NewChecks(APIView):
    def get(self, request, id, format=None):
        file_name = 'checks.zip'
        new_checks = Check.objects.filter(printer_id=id, status='P')

        check_pdfs = []
        for check in new_checks:
            check_pdfs.append(check.pdf_file.name)

        zf = file_compress(check_pdfs)

        response = HttpResponse(zf, headers={
            'Content-Type': 'application/zip',
            'Content-Disposition': 'attachment; filename="%s"' % file_name,
        })

        return response


def file_compress(files, output_zip='checks.zip'):
    with zipfile.ZipFile(output_zip, mode='w') as archive:
        for file in files:
            archive.write(file)

    with zipfile.ZipFile(output_zip, mode="r") as archive:
        archive.printdir()
    return archive
