from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    Title = models.CharField( max_length=50)
    Date_Time = models.DateField( auto_now_add=True)
    def __str__(self):
        return self.Title

# Create your models here.
class Article(models.Model):
    Author = models.ForeignKey(User , on_delete=models.CASCADE, related_name='Articles') 
    category = models.ManyToManyField(Category, related_name='Articles')
    Title = models.CharField(max_length=80)
    Body = models.TextField()
    Image = models.ImageField()
    Created = models.DateField(auto_now_add=True)
    Updated = models.DateField(auto_now=True)
    Pb_Timezone = models.DateField( default= timezone.now())
    Slug = models.SlugField(null=True, blank= True , unique=True) 
    class Meta:
        ordering = ('-Created',)

    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        self.Slug = slugify(self.Title)
        super(Article,self).save()

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'Slug': self.Slug})

    def __str__(self):
        return f"{self.Title} - {self.Body[:30]}"
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True, related_name='replies')
    body = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]