from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404

from blog.models import Post
# Create your views here.


def index(request):
    """TODO: Docstring for index.
    :returns: TODO

    """
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    c = Context({'latest_posts': latest_posts, })
    return HttpResponse(t.render(c))


def post(request, post_id):
    """TODO: Docstring for post.
    :returns: TODO

    """
    single_post = get_object_or_404(Post, pk=post_id)
    t = loader.get_template('blog/post.html')
    c = Context({'single_post': single_post, })
    return HttpResponse(t.render(c))
