from django.shortcuts import render
from django.http import HttpRequest
from .models import Post
from django.contrib.auth.models import User
def creat100(requests):
    me = User.objects.get(username='admin')
    p=Post.objects.create(author=me, title='fotbal_omid{i}', text='fotbal_omid baxt')
    # p=Post()
    # p.title='fotbal_omid'
    # p.text='fotbal_omid baxt'
    # p.author=
    
    p.publish()
    return HttpRequest("Done")

# Create your views here.
