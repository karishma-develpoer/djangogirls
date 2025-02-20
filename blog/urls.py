from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    path('login/', views.user_login, name='login'),
    path('singup/', views.singup, name='singup'),
     path('userlogout/', views.userlogout, name='userlogout'),
     path('category/<int:category_id>/', views.post_list, name='post_list_by_category'),
    path('taguser/<int:taguser_id>/', views.post_list, name='post_list_by_taguser'),



]