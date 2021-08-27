from django.shortcuts import render


def articles(request):
    articles_list = [('Article Number' + str(_)) for _ in range(10)]
    context = {
        'articles': articles_list
    }
    return render(request, 'articles/articles.html', context)
