from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from .models import Post, Comment, Category
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView

# Create your views here.


def index(request):
    #all_posts = Post.objects.all()
    all_published_posts = Post.published_posts.all()[:3]
    return render(request, 'blog/index.html', {'all_published_posts': all_published_posts})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(status=True, )
    user_comments = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comments = comment_form.save(commit=False)
            user_comments.post = post
            user_comments.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html',  {
        'post': post , 
        'comments': user_comments, 
        'comments': comments,
        'comment_form': comment_form
        })


class CategoryListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'cat_list'

    def get_queryset(self):
        context = {
            'cat': self.kwargs['category'],
            'posts': Post.published_posts.filter(category__name=self.kwargs['category'])
        }
        return context


def category_list(request):
    category_list = Category.objects.exclude(name='Default')
    context =  {'category_list': category_list,}
    return context