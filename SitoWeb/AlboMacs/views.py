from django.shortcuts import render, get_object_or_404
from .models import Achievement, Course, New
from datetime import date

# Create your views here.


def index(request):
#    today = date.today()
    latest_news = New.objects.all()
    context = {
#        'page': 'Albo',
        'latest_news': latest_news,
    }
    return render(request, 'AlboMacs/index.html',context)

def achievements(request):
    ach = Achievement.objects.all()
#    today = date.today()
    context = {
        'Achievement': ach,
    }
    return render(request, 'AlboMacs/Achievements.html', context)

def achievement_detail(request, pk):
    e = Achievement.objects.get(pk=pk)
    context = {
        'achievement': e,
    }
    return render(request, 'AlboMacs/achievement_detail.html', context)

def news_detail(request, pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'AlboMacs/news_detail.html', {'news': new})

def course_program(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'AlboMacs/course.html', context)