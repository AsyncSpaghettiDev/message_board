from django.urls import path
from .views import HomeView, AboutView, PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("list/", PostListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("create/", PostCreateView.as_view(), name="create"),
]
