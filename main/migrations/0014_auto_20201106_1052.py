# Generated by Django 3.1.3 on 2020-11-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201105_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_amount',
            field=models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Сделаю за'),
        ),
    ]