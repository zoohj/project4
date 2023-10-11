from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from .models import *
from .serializers import *

class SmokingZoneCreateListAPIView(generics.ListCreateAPIView):
    queryset = SmokingZone
    serializer_class = SmokingZoneSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.create(request, *args, **kwargs)

class SmokingZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmokingZone
    serializer_class = SmokingZoneSerializer

    def patch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review
    serializer_class = ReviewSerializer

class ReviewDestroyAPIView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'error': 'Only staff are allowed to access. '}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)