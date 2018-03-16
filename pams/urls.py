from django.urls import path
 
from . import views
 
# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'pams'
 
urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/chart.png/', views.chart, name='chart'),
]
