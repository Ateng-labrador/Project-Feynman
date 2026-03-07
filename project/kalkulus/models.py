from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, blank=True)
    body = models.TextField()
    email = models.EmailField(default='nama@tanya.com')
    addres = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return "{}".format(self.title)
