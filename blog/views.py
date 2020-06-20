from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.db.models import Q

class PostListView(View):
    def get(self, request, *args, **kwargs):
        # posts = Post.objects.all()
        # posts = Post.objects.get(pk=2)
        # posts = Post.objects.filter(text='テスト')
        # posts = Post.objects.filter(title='ドラえもん', text='テスト')
        posts = Post.objects.filter(Q(title='スラムダンク') | Q(text='テスト'))
        return render(request, 'blog/post_list.html',{
            'posts': posts,
        })