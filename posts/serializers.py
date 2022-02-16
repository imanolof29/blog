#DJANGO REST FRAMEWORK
from rest_framework import serializers

#SERIALIZERS
from authentication.serializers import UserModelSerializer
#MODELS
from posts.models import Post, Comment

class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'user',)

class PostModelSerializer(serializers.ModelSerializer):

    user = UserModelSerializer(read_only=True)

    comments = CommentModelSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_at', 'comments', 'user',)
        read_only_fields = ('id', 'user',)


