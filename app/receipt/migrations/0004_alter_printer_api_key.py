# Generated by Django 3.2.16 on 2022-10-07 08:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0003_alter_printer_api_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='api_key',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
    ]
