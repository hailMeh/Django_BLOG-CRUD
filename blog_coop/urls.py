from django.urls import path
from .views import IndexAsView, BlogDetailView

urlpatterns = [
     path('', IndexAsView.as_view(), name='index'),
     path('post/<int:pk>/', BlogDetailView.as_view(), name='post-details')
]
