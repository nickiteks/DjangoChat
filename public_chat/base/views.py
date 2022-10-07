from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db import models
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer,Post
from .serializers import PostSerializer
from .forms import CreateUserForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created')

    context = {'Posts':posts}
    return render(request, "index.html",context)

@api_view(['POST'])
def add_post(request):
    data = request.data
    print('Data',data)
    post = Post.objects.create(
        body=data['body']
    )

    serializer = PostSerializer(post, many = False)

    return Response(serializer.data)

def getPosts(request):
    posts = Post.objects.all()[:20]
    return JsonResponse({'Posts':list(posts.values())})


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user  =  User.objects.get(username = username)

            customer,created = Customer.objects.get_or_create(
                email=email,
                user=user,
                name=username
            )
            customer.save()
            
            return redirect('index')
    
    context = {'form':form}
    return render(request,'register.html',context)

