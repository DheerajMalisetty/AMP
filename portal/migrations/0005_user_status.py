# Generated by Django 2.0.6 on 2019-01-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_cod'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
