from django.urls import path
from articles.views import articles


urlpatterns = [
    path('', articles),
]