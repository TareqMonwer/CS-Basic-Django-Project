import requests
from articles.models import Article

def get_json_articles(api_url='https://jsonplaceholder.typicode.com/posts'):
    articles_list = requests.get(api_url)
    return articles_list.json()


def get_articles():
    return Article.objects.all()
