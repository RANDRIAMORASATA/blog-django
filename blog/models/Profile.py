from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return  ("User : " + self.description)