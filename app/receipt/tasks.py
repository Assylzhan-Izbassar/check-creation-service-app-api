"""
Task for creating pdf file from html document.
"""
import os
import json
import base64
import requests
from celery import shared_task
from django.template import loader
from django.shortcuts import get_object_or_404
from receipt.models import Check


WK_HOST = os.environ.get('WK_HOST')
WK_PORT = os.environ.get('WK_PORT')


@shared_task
def create_pdf_file(check_id):
    check = get_object_or_404(Check, pk=check_id)
    file_name = '{}_{}'.format(check.order['id'], check.type)
    url = 'http://{}:{}/'.format(WK_HOST, WK_PORT)

    template = loader.get_template('checks/check_detail.html')

    file = template.render({'check': check})
    file_encode = file.encode('utf-8')

    data = {
        'contents': base64.b64encode(file_encode).decode(),
    }
    headers = {'Content-Type': 'application/json', }
    response = requests.post(url, data=json.dumps(data), headers=headers)

    file_dir = '/app/media/pdf/{}.pdf'.format(file_name)

    with open(file_dir, 'wb+') as f:
        f.write(response.content)

    check.pdf_file.name = 'pdf/{}.pdf'.format(file_name)
    check.save()


@shared_task
def send_to_print(printer_id):
    checks = Check.objects.filter(printer_id=printer_id, status='P')
    for check in list(checks):
        check.status = 'C'
        check.save()
