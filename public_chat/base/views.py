from multiprocessing import context
from django.shortcuts import render
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {'Posts':posts}
    return render(request, "index.html",context)

@api_view
def add_post(request):
    data = request.data
    print('Data',data)
    post = Post.objects.create(
        bodu=data.body
    )

    return Response('Data was subnitted')