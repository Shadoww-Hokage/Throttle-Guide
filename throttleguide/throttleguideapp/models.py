from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
# Create your models here.

class Post(models.Model):
    
    type = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    
    cat = (('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatch BacK', 'Hatch Back'), ('Super Car', 'Super Car'), ('Coupe', 'Coupe'))
    
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=cat)
    manufacturer = models.CharField(max_length=200)
    released = models.IntegerField(null=True)
    mileage = models.CharField(max_length=200)
    rating = models.IntegerField(choices=type)
    engine = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
    caption = models.CharField(max_length=200)
    no_of_likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    
    def _str_self(self):
        return self.caption
    
    def increment_like(self):
        self.no_of_likes += 1
        self.save()




class Profile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile_img')
    bio = models.CharField(max_length=200, blank=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    no_of_followers = models.IntegerField(default=0)
    no_of_following = models.IntegerField(default=0)



class Likes(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)