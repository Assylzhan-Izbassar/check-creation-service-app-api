"""
Creating base models for receipt API.
"""
from django.db import models


CHECK_TYPE_KITCHEN = 'kitchen'
CHECK_TYPE_CLIENT = 'client'

CHECK_TYPE_CHOICES = [
    (CHECK_TYPE_KITCHEN, CHECK_TYPE_KITCHEN),
    (CHECK_TYPE_CLIENT, CHECK_TYPE_CLIENT),
]


class Printer(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(
        max_length=7,
        choices=CHECK_TYPE_CHOICES,
        default=CHECK_TYPE_CLIENT,
    )
    point_id = models.IntegerField()


class Check(models.Model):

    PRINTED_STATUS_PENDING = 'P'
    PRINTED_STATUS_COMPLETE = 'C'
    PRINTED_STATUS_FAILED = 'F'

    PRINTED_STATUS_CHOICES = [
        (PRINTED_STATUS_PENDING, 'Pending'),
        (PRINTED_STATUS_COMPLETE, 'Complete'),
        (PRINTED_STATUS_FAILED, 'Failed'),
    ]

    type = models.CharField(
        max_length=7,
        choices=CHECK_TYPE_CHOICES,
        default=CHECK_TYPE_CLIENT
    )
    order = models.JSONField()
    status = models.CharField(
        max_length=1,
        choices=PRINTED_STATUS_CHOICES,
        default=PRINTED_STATUS_PENDING,
    )
    pdf_file = models.FileField(upload_to='media/pdf')
    printer_id = models.ForeignKey(
        Printer,
        on_delete=models.SET_NULL,
    )