from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from tracker.models import Habit
from tracker.models import User
# Create your tests here.


class HabitTestCase(APITestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(email='norilkarus@gmail.com')
        self.user.set_password('norilkarus')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        response = self.client.post('/users/token/', {"email": "norilkarus@gmail.com", "password": "norilkarus"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        data_habit = {
            'user': self.user.pk,
            'action': 'Eat',
            'nice': True,
            'periodicity': 'Каждый день',
        }

        response = self.client.post(
            '/habits/habit_create/',
            data=data_habit
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 2, 'user': 2, 'place': None, 'time': None,
             'action': 'Eat', 'nice': True, 'periodicity': 'Каждый день', 'duration': '00:02:00',
             'is_public': False, 'related_habit': None, 'reward': None}
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):

        self.maxDiff = None

        response = self.client.post('/users/token/', {"email": "norilkarus@gmail.com", "password": "norilkarus"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        Habit.objects.create(
            user=self.user,
            action='Eat',
            nice=True,
            periodicity='Каждый день',
        )

        response = self.client.get(
            '/habits/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': 5, 'user': 5,
                          'place': None,
                          'time': None, 'action': 'Eat',
                          'nice': True,
                          'periodicity': 'Каждый день',
                          'duration': '00:02:00',
                          'is_public': True, 'related_habit': None,
                          'reward': None}]}
        )

    def test_detail_habit(self):

        response = self.client.post('/users/token/', {"email": "norilkarus@gmail.com", "password": "norilkarus"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            user=self.user,
            action='Eat',
            nice=True,
            periodicity='Каждый день'
        )

        response = self.client.get(
            reverse('habits:habit_detail', kwargs={'pk': habit.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 4, 'user': 4, 'place': None, 'time': None,
             'action': 'Eat', 'nice': True, 'periodicity': 'Каждый день', 'duration': '00:02:00',
             'is_public': True, 'related_habit': None, 'reward': None}
        )

    def test_change_habit(self):

        response = self.client.post('/users/token/', {"email": "norilkarus@gmail.com", "password": "norilkarus"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            user=self.user,
            action='Eat',
            nice=True,
            periodicity='Каждый день'
        )

        data_habit_change = {
            'name': 'Test_1',
        }

        response = self.client.patch(
            reverse('habits:habit_change', kwargs={'pk': habit.pk}),
            data=data_habit_change
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'user': 1, 'place': None, 'time': None,
             'action': 'Eat', 'nice': True, 'periodicity': 'Каждый день', 'duration': '00:02:00',
             'is_public': True, 'related_habit': None, 'reward': None}
        )

    def test_delete_habit(self):

        response = self.client.post('/users/token/', {"email": "norilkarus@gmail.com", "password": "norilkarus"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            user=self.user,
            action='Eat',
            nice=True,
            periodicity='Каждый день'
        )

        # получаем детали привычки
        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': habit.pk})
        )

        # проверяем ответ на получение привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
