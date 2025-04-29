from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirect root URL to the tracker app
    path('', include('tracker.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]