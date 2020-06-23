from django.shortcuts import render
from .models import post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
posts=[
    {
        'user':'yukti',
        'tile':'profile 1',
        'content':'first post',
    },
    {
'user':'shruti',
        'tile':'profile 2',
        'content':'second post',
    }

]
def home(request):
    context={
        'posts':post.objects.all()
    }
    return render(request,'APP/home.html',context)


def about(request):
    return render(request,'APP/about.html',{'title':'About'})
