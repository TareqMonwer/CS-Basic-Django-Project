from django.db import models
from django.db.models.functions import Lower


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = [Lower('title')]
        verbose_name = "Post"
        verbose_name_plural = "Posts"