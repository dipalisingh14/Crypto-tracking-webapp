from django.contrib import admin
from django.urls import path, include
from meme import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("product", views.product, name='product'), 
    path("contact", views.contact, name='contact'),  
    path("login",views.login, name='login'),
    path("signup",views.signup,name='signup'),
    path("loggedin",views.loggedin,name="loggedin"),
    path("loggedout",views.loggedout,name="loggedout"),
    path("dataupload",views.dataupload,name="dataupload"),
]
