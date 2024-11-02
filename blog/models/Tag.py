from django.db import models
#from blog.models import Post

# Create your models here.
#ManyToMany avec Post  
class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    # post = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return "Tag : "+self.name