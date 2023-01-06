from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
