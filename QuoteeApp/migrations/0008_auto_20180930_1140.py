# Generated by Django 2.1.1 on 2018-09-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteeApp', '0007_auto_20180930_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input_quote',
            name='picture',
            field=models.ImageField(blank=True, default='media/images/no-image.png', upload_to='images'),
        ),
    ]
