from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Post
#comment from mac
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'