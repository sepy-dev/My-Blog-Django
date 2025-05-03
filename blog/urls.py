from django.urls import path
from .views import postdetale, post_list, category
app_name = "blog"
urlpatterns = [
    path('detale/<str:Slug>', postdetale, name='post'),
    path('postlist', post_list, name='post_list'),
    path('category/<int:pk>', category, name='category'),

]
