# Generated by Django 2.1.1 on 2018-09-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteeApp', '0009_auto_20180930_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input_quote',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
