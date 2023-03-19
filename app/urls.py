from django.contrib import admin
from django.urls import path,include
from .views import LoginPage,IndexPage,LogoutPage,DetailsPage,RegisterPage,UploadDetails
urlpatterns = [
    path("login/", LoginPage.as_view(),name="login"),
    path("logout/",LogoutPage.as_view(),name="logout"),
    path("details/",DetailsPage.as_view(),name="details"),
    path("",IndexPage.as_view()),
    path("register/", RegisterPage.as_view(), name="register"),
    path("upload/",UploadDetails.as_view(),name="upload"),
]
