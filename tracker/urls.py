from django.urls import path
from tracker.apps import TrackerConfig
from tracker.views import HabitListAPIView, HabitCreateAPIView, \
    HabitPublicListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView

app_name = TrackerConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit_update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit_delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),

]
