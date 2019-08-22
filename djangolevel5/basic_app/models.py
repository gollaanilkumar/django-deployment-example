from django.db import models
from django.contrib.auth.models  import User

class User_Profile_info(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio=models.URLField(blank=True)

    profile_pics=models.ImageField(upload_to="profile_pics",blank=True)


    def __str__(self):
        return self.user.username

# Create your models here.
