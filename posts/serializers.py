from rest_framework import serializers

from config import settings
from users.serializers import UserSerializer

from .models import Post
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(
        source='author',
    )
    class Meta:
        model = Post
        Fields = ["id", "title", "content", "image", "likes", "created_at", "author", "is_likes"]
        def get_likes(self, obj):
            return obj.get_likes()
        def get_create_at(self,obj):
            return obj.created_at.strftime("%Y/%m/%d %H:%M")
        def get_image(self, obj):
            if obj.image:
                return settings.HOST + obj.image.url
            else:
                return ""
        def  get_is_likes(self, obj):
            request= self.context.get('request')
            if request.user.is_authenticated and Post.objects.filter(user = request.user,post = obj).exists():
                return True
            else:
                return False