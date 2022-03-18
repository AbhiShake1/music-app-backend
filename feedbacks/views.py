from django.http import HttpRequest, HttpResponse
from .models import Post
from .forms import FeedbackForm
from django.shortcuts import get_object_or_404


# Create your views here.

def post_detail(request: HttpRequest, slug) -> HttpResponse:
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = feedback_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        feedback_form = FeedbackForm()

    return HttpResponse({'post': post,
                         'comments': comments,
                         'new_comment': new_comment,
                         'comment_form': feedback_form})
