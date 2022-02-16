#DJANGO REST FRAMEWORK
from turtle import title
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#SERIALIZER
from posts.serializers import CommentModelSerializer, PostModelSerializer

#MODELS
from posts.models import Post, Comment

"""class CommentViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentModelSerializer
    

    def get_queryset(self):
        pass"""        


class PostViewSet(viewsets.GenericViewSet, 
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

    """def get_queryset(self):
        #Get users posts
        search = self.request.query_params.get('search')
        if search:
            self.queryset = self.queryset.get(title=search)
        return self.queryset.filter(user=self.request.user)"""
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
