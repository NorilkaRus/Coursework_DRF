from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    PERIODICITY_CHOICES = [
        (1, 'Каждый день'),
        (2, 'Каждая неделя')
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='user', verbose_name='пользователь')
    place = models.CharField(max_length=50, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=300, verbose_name='действие')
    nice = models.BooleanField(default=False, verbose_name='приятность')
    related_habit = models.ForeignKey(
        'self', on_delete=models.SET_NULL, **NULLABLE,
        related_name='main_habit', verbose_name='связанная привычка')
    periodicity = models.PositiveIntegerField(default=1, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    reward = models.CharField(max_length=300, **NULLABLE, verbose_name='вознаграждение')
    duration = models.DurationField(verbose_name='длительность выполнения')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    objects = models.Manager()

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)