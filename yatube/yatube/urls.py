from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='post')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls'))
]
