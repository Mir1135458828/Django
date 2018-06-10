from django.shortcuts import render
from .models import Banner, Post, BlogCategory,Comment,FriendlyLink,Tags
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#搜索
class Search(View):
    def post(self,request):

        kw = request.POST.get('keyword')
        post_list = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw))
        for i in post_list:
            i.content = i.content[:100] + '......'

        # 最新评论文章
        comment_list = Comment.objects.order_by('-pub_date')
        new_comment_list = []
        for i in comment_list:
            if i.post not in new_comment_list:
                new_comment_list.append(i.post)
        # 标签
        tags_list = Tags.objects.all()

        ctx = {
            'article_list': post_list,
            'new_comment_list': new_comment_list,
            'tags_list': tags_list,
        }
        return render(request, 'list.html', ctx)


def index(request):
    num = 0
    banner_list = Banner.objects.all()
    #取出所有的文章  按照时间的倒叙展示
    article_list = Post.objects.order_by('-pub_date')
    #显示部分   不显示全部
    for i in article_list:
        i.content = i.content[:100] + '......'

    #取出推荐的文章
    recomment_list = Post.objects.filter(is_recomment=True)
    # 显示部分   不显示全部
    for j in recomment_list:
        j.content = j.content[:50] + '......'

    #分类
    blogCategory_list = BlogCategory.objects.all()

    #最新评论文章
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for i in comment_list:
        if i.post not in new_comment_list:
            new_comment_list.append(i.post)
    #友情链接
    friendlyLink_list = FriendlyLink.objects.all()

    #分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(article_list, per_page=2, request=request)
    article_list = p.page(page)

    ctx = {
        'banner_list': banner_list,
        'article_list': article_list,
        'recomment_list': recomment_list,
        'blogCategory_list':blogCategory_list,
        'new_comment_list':new_comment_list,
        'friendlyLink_list':friendlyLink_list,
    }
    return render(request, 'index.html', ctx)

def lists(request, tid = -1, cid = -1):
    tid = int(tid)
    cid = int(cid)
    article_list = None
    if tid != -1:
        article_list = Post.objects.filter(tags=tid)
    elif cid != -1:
        article_list = Post.objects.filter(category=cid)
    else:
        # 取出所有的文章  按照时间的倒叙展示
        article_list = Post.objects.order_by('-pub_date')
    # 显内容部分   不显示全部
    for i in article_list:
        i.content = i.content[:100] + '......'

    # 最新评论文章
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for i in comment_list:
        if i.post not in new_comment_list:
            new_comment_list.append(i.post)
    #标签
    tags_list = Tags.objects.all()


    ctx = {
        'article_list': article_list,
        'new_comment_list': new_comment_list,
        'tags_list':tags_list,
    }

    return render(request, 'list.html', ctx)


def detail(request, id):
    tag_list = Tags.objects.all()
    post = Post.objects.get(pk=id)

    # 最新评论文章
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for i in comment_list:
        if i.post not in new_comment_list:
            new_comment_list.append(i.post)

    #取出推荐的文章
    recomment_list = Post.objects.filter(is_recomment=True)
    ctx = {
        'post': post,
        'tag_list':tag_list,
        'recomment_list':recomment_list,
        'new_comment_list':new_comment_list,
    }
    return render(request, 'show.html', ctx)
