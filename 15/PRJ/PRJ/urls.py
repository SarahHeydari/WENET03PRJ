
from django.contrib import admin
from django.urls import path
from WAPI import views  # Import the view directly from the users app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/AddPoint/', views.AddPoint, name='AddPoint'),  # Define the API endpoint
    path('api/CountPoint/', views.CountPoint, name='CountPoint'),
]

