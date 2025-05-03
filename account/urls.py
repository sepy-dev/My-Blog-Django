from django.urls import path
from .views import user_login, user_logout, registration

app_name = "account"
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', registration, name='register'),

]