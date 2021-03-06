# Generated by Django 3.1.3 on 2020-11-27 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20201125_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userreview',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='userreview',
            name='accuracy',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=5, verbose_name='Качество'),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='cost',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=5, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='reviewal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL, verbose_name='Респондент'),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='speed',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=5, verbose_name='Скорость'),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Сообщение')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_messages', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='main.offer', verbose_name='Предложение')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Чат-сообщение',
                'verbose_name_plural': 'Чат-сообщения',
                'ordering': ['-created'],
            },
        ),
    ]
