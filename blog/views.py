from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .forms import PostForm, CommentForm, UserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def view_profile(request):
    try:
        query = request.GET.get("q")
        print(query+"cookies")
        num = request.user.id
        print(num)

        posts = Post.objects.filter(author=num)
        print(query+"cookies")
    except Exception as e:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/view_profile.html', {'posts': posts})

#def post_filter_on_user(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

# I followed the djangogirls tutorial
def post_list(request):
    try:
        query = request.GET.get("q")
        print(query+"cookies")
        posts = Post.objects.filter(title__contains=query).order_by('-published_date')
    except Exception as e:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
            return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            #return redirect('post_detail', pk=post.pk)
            return render(request, 'blog/post_detail.html', {'post': post})
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def create_account(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserForm()
    return render(request, 'blog/create_account.html', {'form': form})


#For creating the API i followed thenewbostons tutorial
#Lists all posts or create a new one
#posts/
class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self):
        pass
