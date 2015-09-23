from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from blog.models import Post
from blog.forms import PostForm
# Create your views here.


def get_popular_posts():
    """TODO: Docstring for encode_url.
    :returns: TODO

    """
    popular_posts = Post.objects.order_by("-views")[:5]
    return popular_posts


def index(request):
    """TODO: Docstring for index.
    :returns: TODO

    """
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):
    """TODO: Docstring for post.
    :returns: TODO

    """
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1
    single_post.save()
    t = loader.get_template('blog/post.html')
    context_dict = {
        'single_post': single_post,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def add_post(request):
    """TODO: Docstring for add_post.
    :returns: TODO

    """
    context = RequestContext(request)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():   # is the form valid?
            form.save(commit=True)   # if yes, save it to database
            return redirect(index)
        else:
            print form.errors   # no? dispaly errors to end user
    else:
        form = PostForm()
    return render_to_response("blog/add_post.html", {'form': form},
                              context)
