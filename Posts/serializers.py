from rest_framework import serializers
from .models import  Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

   

