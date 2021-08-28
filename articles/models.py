from django.db import models
from django.db.models.functions import Lower


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def is_spam(self):
        if not self.content:
            return True
        return False

    @classmethod
    def get_titles_that_contains_word(cls, word='tutorial'):
        articles = Article.objects.filter(
            title__icontains=word
        )
        return articles

    class Meta:
        ordering = [Lower('title')]