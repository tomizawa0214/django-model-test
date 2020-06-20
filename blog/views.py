from django.shortcuts import render
from django.views.generic import View
from .models import Post

class PostListView(View):
    def get(self, request, *args, **kwargs):
        # posts = Post.objects.all()
        posts = Post.objects.get(pk=2)
        return render(request, 'blog/post_list.html',{
            'posts': posts,
        })
