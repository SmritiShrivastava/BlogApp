from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView, name = "home"),
    path("signup", views.signUpView, name = "signup"),
    path("login", views.logInView, name = "login"),
    path("logout", views.logoutView, name = "logout"),
    path("write", views.writeBlog, name = "write"),
    path("profile", views.profilePage, name = "profile"),
    path("detail/<id>", views.detailView, name = "detail"),
    path("like/<id>", views.likeView, name = "like"),
    path("search", views.searchView, name = "search"),
]