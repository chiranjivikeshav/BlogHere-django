from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact' ),
    path('signup', views.signUp, name="signUp"),
    path('login', views.userLogin, name="login"),
    path('logout', views.userLogout, name="logout"),
    path('search', views.search, name="search"),
    path('AddBlog',views.writeBlog,name="AddBlog"),
]
