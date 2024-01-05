# gpacalculator/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gpaapp/', include('gpaapp.urls')),
    # Add other URL patterns as needed
]

