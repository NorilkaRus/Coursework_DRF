# Generated by Django 5.0 on 2024-02-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveIntegerField(choices=[(1, 'Каждый день'), (2, 'Каждая неделя')], default=1, verbose_name='периодичность'),
        ),
    ]
