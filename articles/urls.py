from django.urls import path
from articles.views import articles

app_name = 'articles'
urlpatterns = [
    path('', articles, name="articles"),
]