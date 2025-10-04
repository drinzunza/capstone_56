from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""


class PostList(ListView):
    model = Post
    template_name = "blog/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm() # create a new form and send it to html

        return context


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create.html"
    success_url = reverse_lazy('post_list')


class PostDetail(DetailView):
    model = Post
    template_name = "blog/details.html"