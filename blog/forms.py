from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment, Like

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields = ('name', 'lifegoal',)
        fields = ('title', 'text', 'image')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = ()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
