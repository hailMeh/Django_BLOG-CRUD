from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class IndexAsView(ListView):
    template_name = 'index.html'
    model = Post


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
