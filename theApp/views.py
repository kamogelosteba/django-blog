from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from . import models
#from .forms import PostForm
from django.urls import reverse_lazy



# Create your views here.

#def home(request):
 #   return render(request,'home.html', {} )


class HomeView(ListView):
    model=models.Post
    ordering = ['-created_at']
    template_name='theApp/home.html'


class ArticleView(DetailView):
    model= models.Post
    templete_name='theApp/detail.html'

class AddPost(CreateView):
    model=models.Post
    #form_class= PostForm
    template_name='theApp/add_post.html'
    fields = '__all__'

class EditPost(UpdateView):
    model=models.Post
    template_name='theApp/edit_post.html'
    fields = ['title','title_tag','content']

class DeletePost(DeleteView):
    model = models.Post
    template_name = 'theApp/delete_post.html'
    success_url = reverse_lazy('home')
