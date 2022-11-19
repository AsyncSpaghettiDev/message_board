from django.urls import path
from .views import PageHomeView, PageAboutView

urlpatterns = [
    path("", PageHomeView.as_view(), name="home"),
    path("about/", PageAboutView.as_view(), name="about"),
]
