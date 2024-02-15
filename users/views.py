from django.shortcuts import render
from rest_framework import generics
from users.serializers import UserListSerializer, UserCreateSerializer
from users.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView, TemplateView, View
from django.urls import reverse_lazy, reverse
# Create your views here.


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserLogin(LoginView):
    pass


class UserLogout(LogoutView):
    pass


# class RegisterView(CreateView):
#     model = User
#     form_class = RegisterForm
#     success_url = reverse_lazy('tracker/index.html')
#
#     def form_valid(self, form):
#         user = form.save()
#         user.is_active=False
#         user.save()


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
