from django.db import models

# Create your models for (contact us) here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=300)
     phone= models.CharField(max_length=15)
     email= models.CharField(max_length=300)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
        return self.name