from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def postdetale(request, Slug):
    article = get_object_or_404(Article, Slug = Slug)
    if request.method == 'POST' and request.user.is_authenticated:
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        
        if body:  # بررسی وجود متن کامنت
            # ایجاد کامنت جدید
            new_comment = Comment(
                body=body,
                user=request.user,
                article=article
            )
            
            # اگر parent_id وجود دارد، کامنت والد را پیدا کنید
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id)
                    new_comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass  # اگر کامنت والد وجود نداشت، نادیده بگیر
            
            new_comment.save()
            return redirect(article.get_absolute_url())
    
    return render(request, 'blog/single_blog.html', {'article': article})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from .models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from .models import Article

def post_list(request):
    query = request.GET.get('q')
    
    # اگر q ارسال شده، فیلتر کنید با نام فیلدهای درست
    if query:
        articles = Article.objects.filter(
            Q(Title__icontains=query) |
            Q(Body__icontains=query)
        ).distinct()
    else:
        articles = Article.objects.all()
    
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'articles': page_obj.object_list,
        'page_obj': page_obj,
        'query': query,            # برای فرم و صفحه‌بندی
        'category': Category.objects.all(),  # یا هر queryset دیگری که استفاده می‌کنید
    }
    return render(request, 'blog/blog.html', context)


def category(request, pk):
    category_one = get_object_or_404(Category, id =pk)
    articleses = category_one.Articles.all()
    paginator = Paginator( articleses, 3)
    
    # دریافت شماره صفحه از پارامتر GET
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # اگر شماره صفحه معتبر نباشد، صفحه اول نمایش داده شود
        page_obj = paginator.page(1)
    except EmptyPage:
        # اگر صفحه خارج از محدوده باشد، آخرین صفحه نمایش داده شود
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'articles': page_obj.object_list, # لیست مقالات صفحه فعلی
        'page_obj': page_obj, # آبجکت صفحه برای مدیریت صفحه‌بندی
    }
    return render(request, 'blog/blog.html', context)

