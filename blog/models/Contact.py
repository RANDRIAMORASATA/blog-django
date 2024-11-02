from django.db import models

class Contact(models.Model):
    civility = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    file = models.FileField(upload_to = "contacts/%Y/%m/%d", blank =True, null = True)
    message= models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return  ("Subject : " + self.subject)