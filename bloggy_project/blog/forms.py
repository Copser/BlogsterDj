from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):

    """Docstring for PostForm.Creating AddPost Form so end-user can add
        posts utilizing Django's built in form handling features.
    """
    class Meta:
        """Docstring for Meta. """
        model = Post
        fields = ['title', 'content', 'tag', 'image']
