from django.db import models

from uuslug import uuslug
from django_markdown.models import MarkdownField


# Create your models here.
class Post(models.Model):

    """Docstring for Post. """
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
#    content = models.TextField()
    body = MarkdownField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        """TODO: Docstring for __unicode__.
        :returns: TODO

        """
        return self.title

    def save(self, *args, **kwargs):
        """TODO: Docstring for save.

        :*arg: TODO
        :returns: TODO

        """
        self.slug = uuslug(self.title, instance=self,
                           max_length=100)
        super(Post, self).save(*args, **kwargs)
