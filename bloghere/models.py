from django.db import models
from tinymce.models import HTMLField
import datetime
# Create your models here.


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=30)
    slug=models.CharField(max_length=150)
    timeStamp=models.DateTimeField(blank=True,null=True,default=datetime.datetime.now())
    content=models.TextField()
    image = models.ImageField(null=True)
    def __str__(self):
        return self.author

