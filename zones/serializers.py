from rest_framework import serializers

# from users.serializers import UserSerializer
from zones.models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        # user = UserSerializer(source='user')

        models = Review
        fields = ['content, rating, user']
        extra_kwargs = {
            'id': {'write_only': True},
        }


class SmokingZoneSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        models = SmokingZone
        fields = '__all__'
        extra_kwargs = {
            'id': {'write_only': True},
            'image': {'required': False},
        }