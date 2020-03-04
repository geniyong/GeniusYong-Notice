from django.urls import path

from apps.crawl.views import MainView

app_name = 'crawl'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]