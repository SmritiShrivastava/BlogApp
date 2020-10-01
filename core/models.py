from django.db import models
from django.contrib.auth.models import User

Gender_choices = (
    ("Male","Male"),
    ("Female","Female"),
    ("others","others")
)

# Create your models here.
class userProfiles(User):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    contactNumber = models.IntegerField(blank = True, null = True)
    created = models.DateTimeField(auto_now = True)
    gender = models.CharField(max_length=50, choices=Gender_choices)

class BlogModel(models.Model):
    blogTitle = models.CharField(max_length = 1000)
    blogDescription = models.CharField(max_length = 2000)
    blogImage = models.ImageField(upload_to = "images") 
    location = models.CharField(max_length = 4000, blank = True, null = True)
    blogContent = models.CharField(max_length = 50000)
    created = models.DateTimeField(auto_now = True)

    user = models.ForeignKey(userProfiles, on_delete = models.CASCADE)

    def __str__(self):
        string = str(self.blogTitle)+str(self.user.username)
        return string

class commentsModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete = models.CASCADE)
    user = models.ForeignKey(userProfiles, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 5000)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.blog.blogTitle
    

class likeModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete = models.CASCADE)
    user = models.ForeignKey(userProfiles, on_delete = models.CASCADE)
    like = models.IntegerField(default = 1)


    def __str__(self):
        return self.blog.blogTitle
