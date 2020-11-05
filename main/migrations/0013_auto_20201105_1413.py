# Generated by Django 3.1.3 on 2020-11-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_offer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(blank=True, choices=[('n', 'Новое'), ('a', 'Принято'), ('d', 'Выполнено')], db_index=True, default='n', max_length=1, null=True, verbose_name='Статус'),
        ),
    ]
