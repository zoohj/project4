from django.urls import path
from . import views

urlpatterns= [
    path('<int:user_id>/', views.UserRetrieveDestroyAPIView.as_view()),
    path('signup/', views.UserSignUpAPIView.as_view()),
]