from django.shortcuts import render
from django.shortcuts import redirect
from blog.forms import CommentForm
from blog.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
  return render(request, "blog/index.html")

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
    # to fetch all the Post objects in the system, and send them to the index.html template


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
    if request.user.is_active:
      if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.content_object = post
          comment.creator = request.user
          comment.save()
          return redirect(request.path_info)

      else:
        comment_form = CommentForm()
    else:
      comment_form = None

return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )