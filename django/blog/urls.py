from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
]
