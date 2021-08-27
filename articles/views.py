from django.shortcuts import render
from articles.utils import get_articles


def articles(request):
    context = {
        'articles': get_articles()
    }
    return render(request, 'articles/articles.html', context)
