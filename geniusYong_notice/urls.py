from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.crawl.urls', namespace="crawl")),
    path('admin/', admin.site.urls),
]
