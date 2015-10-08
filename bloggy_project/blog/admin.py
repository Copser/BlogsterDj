from django.contrib import admin
from dajngo_markdown.admin import MarkdownModelAdmin
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):

    """Docstring for PostAdmin. """
    list_dispaly = ('title', 'created_at', 'views')


admin.site.register(Post, PostAdmin)
admin.site.register(MarkdownModelAdmin)
