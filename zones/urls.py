from django.urls import path

from . import views

urlpatterns = [
    path('/', views.SmokingZoneCreateListAPIView.as_view()),
    path('/<id:smoking_zone_id>/', views.SmokingZoneRetrieveUpdateDestroyAPIView.as_view()),
]