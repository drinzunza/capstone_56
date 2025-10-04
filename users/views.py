from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.
class UserLogin(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse_lazy("post_list")
    

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "users/signup.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # change the way the records are saved
        user = form.save(commit=False)
        passw = form.cleaned_data["password"]
        user.set_password(passw) # encrypts the password
        user.save()

        return super().form_valid(form)


        
    