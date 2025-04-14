from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django import forms


def home_view(request):
    return render(request,"pages/home.html")

# Django Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# List View (Read All)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'pages/post_list.html', {'posts': posts})

# Detail View (Read One)
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'pages/post_detail.html', {'post': post})

# Create View
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'pages/post_form.html', {'form': form})

# Update View
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect(f'/{post.id}/')
    return render(request, 'pages/post_form.html', {'form': form})

# Delete View
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('/')
    return render(request, 'pages/post_confirm_delete.html', {'post': post})