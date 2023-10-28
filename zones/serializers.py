from rest_framework import serializers

from users.serializers import UserSerializer
from zones.models import *
from users.models import *

class SmokingZoneSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = SmokingZone
        fields = ['id', 'address', 'detail_address', 'image', 'reviews']

    def get_reviews(self, obj):
        reviews = Review.objects.filter(smoking_zone=obj)
        return ReviewSerializer(reviews, many=True).data

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'user']

    def create(self, validated_data):
        user = self.request.user
        review = Review.objects.create(user=user, **validated_data)
        return review