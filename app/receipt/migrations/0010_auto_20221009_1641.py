# Generated by Django 3.2.16 on 2022-10-09 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0009_alter_check_pdf_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='printer',
            options={'ordering': ['name']},
        ),
    ]
