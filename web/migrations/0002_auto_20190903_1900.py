# Generated by Django 2.1.2 on 2019-09-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]