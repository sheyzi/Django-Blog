from django.contrib.auth.models import User
from django.db import models
from tinymce import models as tinymce_models


class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    short_description = models.TextField()
    content = tinymce_models.HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post <{self.title}>"
