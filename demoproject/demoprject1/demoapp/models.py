from django.db import models

# Create your models here.
class news(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    details=models.TextField()

    def __str__(self):
        return self.name

class work(models.Model):
    image=models.ImageField('pics')
    name=models.CharField(max_length=250)
    details=models.TextField()

    def __str__(self):
        return self.name
