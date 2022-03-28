from django.urls import path
from .views import IndexAsView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView

urlpatterns = [
     path('', IndexAsView.as_view(), name='index'),
     path('post/<int:pk>/', BlogDetailView.as_view(), name='post_details'),
     path('post/new/', BlogCreateView.as_view(), name='post_new'),
     path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
     path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
