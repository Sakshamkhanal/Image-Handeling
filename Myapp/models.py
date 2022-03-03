from django.db import models

# Create your models here.
class Image(models.Model):
    text = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to ="MyImage")
    date = models.DateTimeField(auto_now_add=True)