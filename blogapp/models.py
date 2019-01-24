from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    detail=models.TextField()
    profile_picture=models.FileField()
    def __str__(self):
        return self.name.username

class Catagory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Artical(models.Model):
    artical_author=models.ForeignKey(Author, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField()
    image=models.FileField()
    tk=models.TextField()
    posted_on=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.title