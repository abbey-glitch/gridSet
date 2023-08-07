from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", {"blogs":blogs})

def new(request):
    return HttpResponse('welcome to the page')
