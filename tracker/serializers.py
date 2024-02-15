from rest_framework import serializers
from tracker.models import Habit
from tracker.validators import habit_validator


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для привычки """

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            habit_validator,
        ]
