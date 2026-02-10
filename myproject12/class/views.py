from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Post  # Change from MyModel to Post

class PostListView(ListView):
    model = Post  # Change to Post
    template_name = 'class/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post  # Change to Post
    template_name = 'class/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post  # Change to Post
    template_name = 'class/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')  # Add this

class PostUpdateView(UpdateView):
    model = Post  # Change to Post
    template_name = 'class/post_form.html'
    fields = ['title', 'content']
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post  # Change to Post
    template_name = 'class/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')