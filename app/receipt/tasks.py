"""
Task for creating pdf file from html document.
"""
import os
import json
import requests
from celery import shared_task


WK_HOST = os.environ.get('WK_HOST')
WK_PORT = os.environ.get('WK_PORT')


@shared_task
def create_pdf_file(check_id):
    url = 'http://{WK_HOST}:{WK_PORT}/'
    file = open('/receipt/templates/checks/check_detail.html') \
        .read() \
        .encode('base64')
    data = {
        'contents': file,
    }
    headers = {'Content-Type': 'application/json', }
    response = requests.post(url, data=json.dump(data), headers=headers)

    with open('media/pdf/file.pdf', 'wb') as f:
        f.write(response.content)
