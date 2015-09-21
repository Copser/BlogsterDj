from django.db import models


# Create your models here.
class Post(models.Model):

    """Docstring for Post. """
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
