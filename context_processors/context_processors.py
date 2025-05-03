from blog.models import Article, Category

def recent_post(request):
    recent = Article.objects.order_by('-Created')[:3]
    category = Category.objects.all()[:3]

    return {'recent': recent, 'category' : category}