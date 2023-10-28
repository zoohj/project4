from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from .models import *
from posts.models import *
from zones.models import *
from .serializers import *
from posts.serializers import *
from zones.serializers import *

class UserSignUpAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def retrieve(self, request, user_id):
        instance = User.objects.get(id=user_id)
        serializer = UserSerializer(instance)
        post_serializer = PostSerializer(Post.objects.filter(author=instance), many=True)
        review_serializer = ReviewSerializer(Review.objects.filter(user=instance), many=True)
        data = {'user': serializer.data, 'posts': post_serializer.data, 'reviews': review_serializer.data}
        return Response(data)

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
