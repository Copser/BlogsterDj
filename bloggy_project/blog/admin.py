from django.contrib import admin
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):

    """Docstring for PostAdmin. """
    list_dispaly = ('title', 'created_at')


admin.site.register(Post, PostAdmin)
