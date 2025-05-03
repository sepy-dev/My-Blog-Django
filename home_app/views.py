from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from blog.models import Article

def home(request):
    articles = Article.objects.all().order_by('-Created')[:3]
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            
            # اینجا می‌توانید داده‌ها را ذخیره یا پردازش کنید
            print(f"نام: {name}, ایمیل: {email}, پیام: {text}")
            
            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'home_app/index.html', {
        'articles': articles,
        'user': request.user,
        'form': form  # تغییر نام متغیر به form به جای forms
    })
