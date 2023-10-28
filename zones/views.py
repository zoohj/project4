from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from .models import *
from users.models import *
from .serializers import *

class SmokingZoneCreateListAPIView(generics.ListCreateAPIView):
    queryset = SmokingZone.objects.all()
    serializer_class = SmokingZoneSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.create(request, *args, **kwargs)

class SmokingZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmokingZone.objects.all()
    serializer_class = SmokingZoneSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'smoking_zone_id'

    def patch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(smoking_zone_id=self.kwargs['smoking_zone_id'])

class ReviewDestroyAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'review_id'

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)