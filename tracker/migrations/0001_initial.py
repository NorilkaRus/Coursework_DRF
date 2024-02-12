# Generated by Django 5.0 on 2024-02-12 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=300, verbose_name='действие')),
                ('nice', models.BooleanField(default=False, verbose_name='приятность')),
                ('periodicity', models.PositiveIntegerField(choices=[(1, 'Каждые 12 часов'), (2, 'Каждый день'), (3, 'Каждые 3 дня'), (4, 'Каждая неделя')], default=1, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=300, null=True, verbose_name='вознаграждение')),
                ('duration', models.DurationField(verbose_name='длительность выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_habit', to='tracker.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ('pk',),
            },
        ),
    ]
