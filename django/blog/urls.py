from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
        path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', include('blog.urls')),
]
