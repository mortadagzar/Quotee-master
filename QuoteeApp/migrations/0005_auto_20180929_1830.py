# Generated by Django 2.1.1 on 2018-09-30 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteeApp', '0004_input_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input_quote',
            name='sayer',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='input_quote',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
