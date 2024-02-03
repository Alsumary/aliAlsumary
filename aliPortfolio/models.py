from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class home(models.Model):
    title = models.CharField(max_length=50)
    smallContent = models.TextField(max_length=2000)
class abouts(models.Model):
    TitleText = models.CharField(max_length=50)
    aboutme = models.TextField(max_length=2000)
    counterOneName = models.CharField(max_length=30)
    counterOneNumber = models.IntegerField(default=0)
    counterTwoName = models.CharField(max_length=30)
    counterTwoNumber = models.IntegerField(default=0)
    counterThreeName = models.CharField(max_length=30)
    counterThreeNumber = models.IntegerField(default=0)
class information(models.Model):
    emailAddress = models.EmailField()
    instaAcc = models.CharField(max_length=1000)
    whatsNumber = models.CharField(max_length=1000)
    linkedinAcc = models.CharField(max_length=1000)
    facebookAcc = models.CharField(max_length=1000)

class skills(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title}"
    
class experience(models.Model):
    title = models.CharField(max_length=30)
    time = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    sort_date = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.title}"
    
class education(models.Model):
    title = models.CharField(max_length=30)
    time = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    sort_date = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.title}"
    
class photos(models.Model):
    link = models.TextField(max_length=1500)
    photoTitle = models.CharField(max_length=30, default='Photo', blank=True)

    def __str__(self):
        return f"{self.photoTitle}"

class gallerys(models.Model):
    pageTitle = models.CharField(max_length=30,db_index=True,default='Imagination Trumps Knowledge!')
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    mainPhoto = models.ForeignKey(photos, on_delete=models.CASCADE, blank=True, null=True, related_name="photos")
    photos = models.ManyToManyField(photos, blank=True)
    fullWidth = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    
class article(models.Model):
    pageTitle = models.CharField(max_length=30,db_index=True,default='Words Can Change The World!')
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=500)
    mainPhoto = models.ForeignKey(photos, on_delete=models.CASCADE, blank=True, null=True, related_name="mainPhoto")
    smallDetails = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"
    
