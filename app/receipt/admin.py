"""
Admin classes for the models.
"""
from django.contrib import admin
from . import models


@admin.register(models.Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'printer_id', 'pdf_file']
    list_editable = ['status']
    list_per_page = 10
    list_filter = ['printer_id', 'type', 'status']


@admin.register(models.Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['name', 'check_type', 'api_key']
    list_per_page = 10
