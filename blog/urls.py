from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts, name="posts"),
    path('<int:id>', views.post_page, name="post_page"),
]