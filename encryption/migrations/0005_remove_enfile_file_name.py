# Generated by Django 4.1.7 on 2023-04-15 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0004_enfile_send_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfile',
            name='file_name',
        ),
    ]
