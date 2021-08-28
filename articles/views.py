from django.shortcuts import render
from articles.utils import get_json_articles


def articles(request):
    context = {
        'articles': get_json_articles()
    }
    return render(request, 'articles/index.html', context)
