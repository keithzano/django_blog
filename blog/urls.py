from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-create', PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]
