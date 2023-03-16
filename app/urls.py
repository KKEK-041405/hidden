from django.contrib import admin
from django.urls import path,include
from .views import LoginPage,IndexPage,LogoutPage,DetailsPage
urlpatterns = [
    path("login", LoginPage.as_view()),
    path("logout",LogoutPage.as_view()),
    path("details",DetailsPage.as_view()),
    path("",IndexPage.as_view()),
]
