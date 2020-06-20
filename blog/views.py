from django.shortcuts import render
from django.views.generic import View

class PostListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/post_list.html',{})
