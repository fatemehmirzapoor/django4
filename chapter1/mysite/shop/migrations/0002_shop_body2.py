# Generated by Django 3.0.14 on 2021-05-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='body2',
            field=models.TextField(default=''),
        ),
    ]
