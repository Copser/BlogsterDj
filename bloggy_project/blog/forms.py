from django import forms
from blog.models import Post
from django_markdown.widgets import MarkdownWidget


class PostForm(forms.ModelForm):

    """Docstring for PostForm.Creating AddPost Form so end-user can add
        posts utilizing Django's built in form handling features.
    """
    content = forms.CharField(widget=MarkdownWidget())

    class Meta:
        """Docstring for Meta. """
        model = Post
        fields = ['title', 'content', 'tag', 'image']
