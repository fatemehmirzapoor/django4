# Generated by Django 3.0.14 on 2021-05-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210529_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
