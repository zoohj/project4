from django.urls import path
from posts import views
from django.views.decorators.csrf import csrf_exempt
from posts.views import *
app_name = "posts"

urlpatterns= [
    path('create/', PostCreateView.as_view()),
    path('detail/<int:id>/', PostDetailView.as_view()),
    path('most/', PostMostView.as_view()),
    path('recent/', PostRecentView.as_view()),
    path('delete/<int:id>/', PostDeleteView.as_view()),
]
