from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404

from blog.models import Post
# Create your views here.


def encode_url(url):
    """TODO: Docstring for encode_url.
    :returns: TODO

    """
    return url.replace(' ', '_')


def index(request):
    """TODO: Docstring for index.
    :returns: TODO

    """
    latest_posts = Post.objects.all().order_by('-created_at')
    popular_posts = Post.objects.order_by("-views")[:5]
    t = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
    }
    for post in latest_posts:
        post.url = encode_url(post.title)
    for popular_post in popular_posts:
        popular_post.url = encode_url(popular_post.title)
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, post_url):
    """TODO: Docstring for post.
    :returns: TODO

    """
    single_post = get_object_or_404(Post,
                                    title=post_url.replace('_', ' '))
    single_post.views += 1
    single_post.save()
    t = loader.get_template('blog/post.html')
    c = Context({'single_post': single_post, })
    return HttpResponse(t.render(c))
