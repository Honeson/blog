from django import urls
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='blog_home'),
     path('<slug:slug>/', views.detail, name='blog_detail'),
     path('category/<category>/', views.CategoryListView.as_view(), name='category')
]
