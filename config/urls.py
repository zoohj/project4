from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('zones/', include('zones.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)