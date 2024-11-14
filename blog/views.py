from django.shortcuts import render
from .models import Post

def posts(request):
    first_post = Post.objects.first()
    posts = Post.objects.all()
    return render(request, 'blogs.html', 
                  {'posts': posts,
                   'first_post': first_post})

def post_page(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog.html', {'post': post})