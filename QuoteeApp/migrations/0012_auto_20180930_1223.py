# Generated by Django 2.1.1 on 2018-09-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteeApp', '0011_auto_20180930_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input_quote',
            name='picture',
        ),
        migrations.AddField(
            model_name='input_quote',
            name='picture_ME',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
