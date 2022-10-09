"""
Serializers for receipt API models.
"""
from rest_framework import serializers
from .models import Printer, Check


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = [
            'id',
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
            'pdf_path',
            'printer_id',
        ]
        read_only_fields = ('pdf_file',)

    pdf_path = serializers.SerializerMethodField(method_name='get_path_name')

    def get_path_name(self, check: Check):
        return check.pdf_file.name
