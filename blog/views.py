from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post, Comment, Like
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .forms import PostForm, CommentForm, UserForm, LikeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#from urllib import quote_plus

# Create your views here.
def view_profile(request):
    try:
        query = request.GET.get("q")
        print(query+"cookies")
        posts = Post.objects.filter(author=query)
        print(query+"cookies")
    except Exception as e:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/view_profile.html', {'posts': posts})

#def post_filter_on_user(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

# I followed the djangogirls tutorial #perhaps change title to text?
def post_list(request):
    try:
        query = request.GET.get("q")
        print(query+"cookies")
        a = Post.objects.filter(text__contains=query).order_by('-published_date')
        b = Post.objects.filter(title__contains=query).order_by('-published_date')
        titletext = []
        if len(a) > 0:
            for ai in a:
                for bi in b:
                    if bi not in titletext:
                        titletext.append(bi)
                if ai not in titletext:
                    titletext.append(ai)
            posts = titletext
        elif len(b) > 0:
            for bi in b:
                for ai in a:
                    if ai not in titletext:
                        titletext.append(ai)
                if bi not in titletext:
                    titletext.append(bi)
            posts = titletext
        else:
            posts = titletext
    except Exception as e:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return redirect('post_list')

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
            return redirect('post_detail', pk=post.pk)
            #return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #share_string = quote_plus(post.text)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
            #return render(request, 'blog/post_detail.html', {'post': post})
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def add_like_to_post(request, pk):
    origin = request.GET.get("origin")
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            if Like.objects.filter(post=pk, author=request.user).exists():
                dislike = Like.objects.filter(post=pk, author=request.user)
                dislike.delete()
                #return True
                #return redirect('post_detail', pk=post.pk)
                return redirect(origin)

            else:
                like = form.save(commit=False)
                like.post = post
                like.author = request.user
                like.save()
                #return True
                return redirect(origin)
                #return redirect('post_detail', pk=post.pk)
                #return render(request, 'blog/post_detail.html', {'post': post})
    else:
        form = LikeForm()
    return render(request, 'blog/add_like_to_post.html', {'form': form})

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
