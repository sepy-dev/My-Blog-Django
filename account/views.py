from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        USERNAME = request.POST.get('username')
        PASSWORD = request.POST.get('password')
        USER = authenticate(request, username=USERNAME, password=PASSWORD)
        if USER is not None:
            login(request, USER)
            return redirect("/")

    return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect("/")

def registration(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # بررسی وجود کاربر با این نام کاربری
        if User.objects.filter(username=username).exists():
            context['errors'].append("usereror")
        
        # بررسی تطابق رمزهای عبور
        if password1 != password2:
            context['errors'].append("passworderor")
        
        # بررسی قدرت رمز عبور (اضافه کردن اعتبارسنجی بیشتر)
        if len(password1) < 8:
            context['errors'].append("passworderor")
        
        if context['errors']:  # اگر خطایی وجود داشت
            print(context)
            return render(request, "account/registration.html", context)
        
        try:
            # ایجاد کاربر جدید
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=name
            )
            
            # ورود خودکار کاربر بعد از ثبت نام
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            
            return redirect('/')
            
        except Exception as e:
            context['errors'].append("خطایی در ثبت نام رخ داد")
            return render(request, "account/registration.html", context)
    
    return render(request, "account/registration.html")