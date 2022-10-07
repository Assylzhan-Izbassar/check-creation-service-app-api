"""
Serializers for receipt API models.
"""
from rest_framework import serializers
from .models import Printer, Check


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = [
            'api_key',
            'name',
            'check_type',
            'point_id',
        ]
        read_only_fields = ('api_key',)


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = [
            'id',
            'type',
            'order',
            'status',
            'pdf_file',
        ]
