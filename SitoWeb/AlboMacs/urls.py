from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('', views.index, name='index'),
    path('achievements', views.achievements, name='achievements'),
    path('achievement/<int:pk>/', views.achievement_detail, name='achievement_detail'),
    path('CourseProgram', views.course_program, name='courseprogram'),
    path('new/<int:pk>/', views.news_detail, name='news_detail'),
]