from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='login'),
    path('Home',views.index,name='home'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
]
