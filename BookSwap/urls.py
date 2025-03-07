from django.contrib import admin
from django.urls import path, include  # Include the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the authentication URLs
    path('', include('books.urls')),  # Include your app's URLs
]
