# Generated by Django 2.1.4 on 2019-02-10 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0008_auto_20190210_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='Eligibility',
        ),
    ]
