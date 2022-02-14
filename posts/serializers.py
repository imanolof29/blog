#DJANGO REST FRAMEWORK
from rest_framework import serializers

#SERIALIZERS
from authentication.serializers import UserModelSerializer
#MODELS
from posts.models import Post

class PostModelSerializer(serializers.ModelSerializer):

    user = UserModelSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_at', 'user',)
        read_only_fields = ('id', 'user',)

class PostModelDetailSerializer(PostModelSerializer):

    posts = PostModelSerializer(many=True, read_only=True)