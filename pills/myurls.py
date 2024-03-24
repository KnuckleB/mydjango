from django.contrib import admin
from django.urls import path
from pills import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('home/', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('login/', views.login, name='login'),
    path('member/', views.member, name='member'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
    path('users/', views.users, name='users'),
    path('add/', views.add, name='add'),
    path('edit/', views.add, name='add'),
    path('pay/', views.add, name='pay'),
    path('show/', views.add, name='show'),
    path('image/', views.add, name='image'),
    path('picture/', views.picture, name='picture'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
