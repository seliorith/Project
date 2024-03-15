from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('myapp.urls', namespace='backend')),
    path('', views.home, name='home'),
]
