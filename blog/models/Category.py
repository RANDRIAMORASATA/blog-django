from django.db import models

# Create your models here.
#OneToMany et ManyToOne
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return "Categorie : " +self.name