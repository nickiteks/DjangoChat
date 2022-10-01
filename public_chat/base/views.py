from multiprocessing import context
from django.shortcuts import render
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

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