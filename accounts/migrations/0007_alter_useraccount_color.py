# Generated by Django 4.2.4 on 2023-10-26 13:10

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_useraccount_backgroundcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='color',
            field=colorfield.fields.ColorField(default='#3a3b3c', image_field=None, max_length=25, samples=None),
        ),
    ]
