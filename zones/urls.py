from django.urls import path

from . import views

urlpatterns = [
    path('', views.SmokingZoneCreateListAPIView.as_view()),
    path('<int:smoking_zone_id>/', views.SmokingZoneRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:smoking_zone_id>/reviews/', views.ReviewCreateAPIView.as_view()),
    path('<int:smoking_zone_id>/reviews/<int:review_id>/', views.ReviewDestroyAPIView.as_view()),
]