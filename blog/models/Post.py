from django.db import models
from django.contrib.auth.models import User
from blog.models import Category
from blog.models import Tag
from django.utils.text import slugify 
class Post(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)
    content = models.TextField()
    #un user peut avoir plusieur post mais un post pour un user OnToMany mais un un post ne peut u avoir un user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #un post peut avoir qu une category  mais une category peut avoir plusieur post
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isPublished = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to = "posts/%Y/%m/%d", blank =True, null = True)
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "Post : " +self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)