from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class Comments(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        post = models.ForeignKey('Post', on_delete=models.CASCADE)
        content = models.TextField()
        note = models.IntegerField()
        createdAt = models.DateTimeField(auto_now_add=True)
        updateAt = models.DateTimeField(auto_now=True)

        def __str__(self) -> str:
            return self.content
        
  