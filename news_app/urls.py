from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('news_category/<str:category>/', views.news_category, name="news_category")
]
