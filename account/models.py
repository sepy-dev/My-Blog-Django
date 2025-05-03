from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fther_name = models.CharField(max_length=26)
    melicode = models.CharField(max_length=10)
    image = models.ImageField( upload_to="profile/images")
    def __str__(self):
        return self.user.username