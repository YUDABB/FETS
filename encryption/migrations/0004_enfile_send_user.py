# Generated by Django 4.1.7 on 2023-04-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0003_alter_enfile_file_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfile',
            name='send_user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]