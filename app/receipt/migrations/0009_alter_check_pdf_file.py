# Generated by Django 3.2.16 on 2022-10-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0008_alter_check_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
