from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("list/", PostListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("create/", PostCreateView.as_view(), name="create"),
]
