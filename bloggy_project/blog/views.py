from django.http import HttpResponse
from django.template import Context, loader

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
