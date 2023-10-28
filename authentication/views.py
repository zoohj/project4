from django.shortcuts import render
from rest_framework import generics

class UserSignUpDestroyView(generics.GenericAPIView):
    def post(self, request):
        pass

    def delete(self, request):
        pass

class EmailCodeSendingAPIView(generics.GenericAPIView):
    def post(self, request):
        pass

class EmailCodeCheckAPIView(generics.GenericAPIView):
    def post(self, request):
        pass

class PasswordUpdateAPIView(generics.GenericAPIView):
    def post(self, request):
        pass