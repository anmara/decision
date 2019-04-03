# Generated by Django 2.1.4 on 2019-02-09 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20190208_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='Civil_Status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('spouse', 'Spouse')], default=0, max_length=7, verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='address',
            field=models.CharField(default=0, help_text='zone/street/barangay/province or city/house no.', max_length=100, verbose_name='Adress '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Phone Number '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architect',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architect',
            name='Civil_Status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('spouse', 'Spouse')], default=0, max_length=7, verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architect',
            name='Eligibilty',
            field=models.CharField(choices=[('none', 'None'), ('yes', 'License for ARC')], default=0, max_length=100, verbose_name='Eligibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architect',
            name='address',
            field=models.CharField(default=0, help_text='zone/street/barangay/province or city/house no.', max_length=100, verbose_name='Adress '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architect',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Phone Number '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civil_engr',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civil_engr',
            name='Civil_Status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('spouse', 'Spouse')], default=0, max_length=7, verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civil_engr',
            name='Eligibilty',
            field=models.CharField(choices=[('none', 'None'), ('yes', 'License for CE')], default=0, max_length=100, verbose_name='Eligibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civil_engr',
            name='address',
            field=models.CharField(default=0, help_text='zone/street/barangay/province or city/house no.', max_length=100, verbose_name='Adress '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civil_engr',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Phone Number '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronics_engr',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronics_engr',
            name='Civil_Status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('spouse', 'Spouse')], default=0, max_length=7, verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronics_engr',
            name='Eligibilty',
            field=models.CharField(choices=[('none', 'None'), ('yes', 'License for EE')], default=0, max_length=100, verbose_name='Eligibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronics_engr',
            name='address',
            field=models.CharField(default=0, help_text='zone/street/barangay/province or city/house no.', max_length=100, verbose_name='Adress '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronics_engr',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Phone Number '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mechanical_engr',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mechanical_engr',
            name='Civil_Status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('spouse', 'Spouse')], default=0, max_length=7, verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mechanical_engr',
            name='Eligibilty',
            field=models.CharField(choices=[('none', 'None'), ('yes', 'License for ME')], default=0, max_length=100, verbose_name='Eligibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mechanical_engr',
            name='address',
            field=models.CharField(default=0, help_text='zone/street/barangay/province or city/house no.', max_length=100, verbose_name='Adress '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mechanical_engr',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Phone Number '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurse',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurse',
            name='Civil_Status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('spouse', 'Spouse')], default=0, max_length=7, verbose_name='Civil Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurse',
            name='Eligibilty',
            field=models.CharField(choices=[('none', 'None'), ('yes', 'License for Nurse')], default=0, max_length=100, verbose_name='Eligibility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurse',
            name='address',
            field=models.CharField(default=0, help_text='zone/street/barangay/province or city/house no.', max_length=100, verbose_name='Adress '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurse',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Phone Number '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Academic',
            field=models.CharField(choices=[('85', 'Doctoral Degree'), ('65', 'Masters Degree'), ('45', 'Bachelors Degree')], default='', help_text='Highest academic degree or educational attainment in the field of study', max_length=4, verbose_name='Educational Qualification '),
        ),
        migrations.AlterField(
            model_name='architect',
            name='Academic',
            field=models.CharField(choices=[('85', 'Doctoral Degree'), ('65', 'Masters Degree'), ('45', 'Bachelors Degree')], default='', help_text='Highest academic degree or educational attainment in the field of study', max_length=4, verbose_name='Educational Qualification '),
        ),
        migrations.AlterField(
            model_name='civil_engr',
            name='Academic',
            field=models.CharField(choices=[('85', 'Doctoral Degree'), ('65', 'Masters Degree'), ('45', 'Bachelors Degree')], default='', help_text='Highest academic degree or educational attainment in the field of study', max_length=4, verbose_name='Educational Qualification '),
        ),
        migrations.AlterField(
            model_name='electronics_engr',
            name='Academic',
            field=models.CharField(choices=[('85', 'Doctoral Degree'), ('65', 'Masters Degree'), ('45', 'Bachelors Degree')], default='', help_text='Highest academic degree or educational attainment in the field of study', max_length=4, verbose_name='Educational Qualification '),
        ),
        migrations.AlterField(
            model_name='mechanical_engr',
            name='Academic',
            field=models.CharField(choices=[('85', 'Doctoral Degree'), ('65', 'Masters Degree'), ('45', 'Bachelors Degree')], default='', help_text='Highest academic degree or educational attainment in the field of study', max_length=4, verbose_name='Educational Qualification '),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='Academic',
            field=models.CharField(choices=[('85', 'Doctoral Degree'), ('65', 'Masters Degree'), ('45', 'Bachelors Degree')], default='', help_text='Highest academic degree or educational attainment in the field of study', max_length=4, verbose_name='Educational Qualification '),
        ),
    ]