from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db import models
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import Customer,Post
from .serializers import PostSerializer
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created')
    context = {'Posts':posts}
    return render(request, "index.html",context)

@api_view(['POST'])
def add_post(request):
    data = request.data
    post = Post.objects.create(
        body=data['body'],
        customer = Customer.objects.get(id = data['user'])
    )

    serializer = PostSerializer(post, many = False)

    return Response(serializer.data)

def getPosts(request):
    posts = Post.objects.all()[:20]
    user_list = []
    for post in posts:
        user_list.append(post.customer.name)
    return JsonResponse({'Posts':list(posts.values()),'Users':list(user_list)})


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
            
            return redirect('login')
    
    context = {'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'incorrect')

    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


