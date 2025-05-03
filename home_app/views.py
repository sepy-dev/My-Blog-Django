from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.objects.all().order_by('-Created')[:3]

    return render(request, 'home_app/index.html', context={'articles':articles, 'user': request.user})

 