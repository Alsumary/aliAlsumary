from django.shortcuts import render
from .models import home, abouts, information, skills, experience, education, gallerys, photos, article
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

def index(request):
    homeDB = home.objects.get(pk=1)
    infoDB = information.objects.get(pk=1)
    return render(request, 'index.html',{
        'h': homeDB,
        'i': infoDB
    })

def about(request):
    aboutsDB = abouts.objects.get(pk=1)
    infoDB = information.objects.get(pk=1)
    experienceDB = experience.objects.order_by('-sort_date')
    educationDB = education.objects.order_by('-sort_date')
    skillsDB = skills.objects.all()
    return render(request, 'about.html',{
        'a': aboutsDB,
        'i': infoDB,
        'allSkills': skillsDB,
        'e': experienceDB,
        'edu': educationDB,
    })

def gallery(request):
    infoDB = information.objects.get(pk=1)
    galleryTitle = gallerys.objects.get(pk=1)
    gallery = gallerys.objects.all()
    return render(request, 'gallery.html',{
        'i': infoDB,
        'gT': galleryTitle,
        'gallery': gallery,
    })

def swipper(request, gallery_id):
        infoDB = information.objects.get(pk=1)
        galleryDB = gallerys.objects.get(pk=gallery_id)
        return render(request, 'sliders.html',{
        'i': infoDB,
        'gallery': galleryDB,
    })

def articles(request):
    infoDB = information.objects.get(pk=1)
    articlesTitle = article.objects.get(pk=1)
    articlesDB = article.objects.all()
    return render(request, 'articles.html',{
        'i': infoDB,
        'aT': articlesTitle,
        'articles': articlesDB,
    })