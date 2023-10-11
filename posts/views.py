from http import HTTPStatus
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response


from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics, status



class PostCreateView(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post
    serializer_class= PostSerializer

class PostMostView(generics.ListAPIView):
    queryset = Post.objects.all.order_by('-likes')
    serializer_class= PostSerializer

class PostRecentView(generics.ListAPIView):
    queryset = Post.objects.all.order_by('-created_at')
    serializer_class= PostSerializer

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post
    serializer_class = PostSerializer
    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(status= status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)