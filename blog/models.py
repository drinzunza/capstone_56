from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=80)  # short text
    content = models.TextField()  # unlimited text
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # autofield
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title