from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.db.models import Q
from django.db.models import Sum

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all() # すべてのレコードを取得
        # posts = Post.objects.get(pk=2) # idが2番のレコードを取得
        # posts = Post.objects.filter(text="テスト") # textが"テスト"に完全一致するレコードを取得
        # posts = Post.objects.filter(title="ONE PIECE") # textが"テスト"に完全一致するレコードを取得
        # posts = Post.objects.filter(title="ドラえもん", text="テスト") # titleが"ドラえもん"かつtextが"テスト"に完全一致するレコードを取得
        # posts = Post.objects.filter(title__in=["ドラえもん", "スラムダンク"]) # titleが"ドラえもん"または"スラムダンク"と完全一致するレコードを取得
        # posts = Post.objects.filter(Q(title="スラムダンク") | Q(text="テスト")) #titleが2スラムダンク"またはtextが"テスト"と完全一致するレコードを取得
        # posts = Post.objects.filter(pk__gt=2) #idが2より大きいレコードを取得
        # posts = Post.objects.filter(pk__lt=3) #idが3より小さいレコードを取得
        # posts = Post.objects.filter(pk__gte=3) #idが3以上のレコードを取得
        # posts = Post.objects.filter(pk__lte=1) #idが1以下のレコードを取得
        # posts = Post.objects.filter(pk__range=(2, 3)) #idが2から3までのレコードを取得
        # posts = Post.objects.filter(published_data__isnull=True) #published_dataがNULL（空白）のレコードを取得
        # posts = Post.objects.filter(title__exact="ONE PIECE") #titleが"ONE PIECE"（大文字小文字区別あり）のレコードを取得
        # posts = Post.objects.filter(title__iexact="one piece") #titleが"one piece"（大文字小文字区別なし）のレコードを取得
        # posts = Post.objects.filter(title__startswith="ONE") #titleが"ONE"で始まる（大文字小文字区別あり）レコードを取得
        # posts = Post.objects.filter(title__istartswith="one") #titleが"one"で始まる（大文字小文字区別なし）レコードを取得
        # posts = Post.objects.filter(title__contains="PI") #titleに"PI"が含まれる（大文字小文字区別あり）レコードを取得
        # posts = Post.objects.filter(title__icontains="pi") #titleに"pi"が含まれる（大文字小文字区別なし）レコードを取得
        # posts = Post.objects.filter(title__endswith="CE") #titleが"CE"で終わる（大文字小文字区別あり）レコードを取得
        # posts = Post.objects.filter(title__iendswith="ce") #titleが"ce"で終わる（大文字小文字区別なし）レコードを取得
        # posts = Post.objects.order_by("id") #昇順でソートして取得
        # posts = Post.objects.order_by("-id") #降順でソートして取得
        # posts = Post.objects.filter(title__icontains="ン").order_by("-id") #titleに"ン"が含まれるレコードを降順でソートして取得
        # posts = Post.objects.values() #すべてのレコードを辞書で取得
        # posts = Post.objects.values_list("title", flat=True) #titleをすべてリストで取得
        # posts = Post.objects.select_related("author").all() #すべてのレコードをリストで結合して取得
        # posts = Post.objects.count() #レコードの件数を取得
        # posts = Post.objects.aggregate(posts=Sum("id")) #idの合計値を取得
        # posts = Post.objects.latest("created_date") #最新のレコード（title）を取得
        # posts = Post.objects.earliest("created_date") #最古のレコード（title）を取得
        posts = Post.objects.filter(title="ドラえもん").exists() #titleが"ドラえもん"に完全一致するレコードが存在するかを取得=True
        return render(request, 'blog/post_list.html',{
            'posts': posts,
        })