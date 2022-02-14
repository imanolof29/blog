#DJANGO REST FRAMEWORK
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#SERIALIZER
from posts.serializers import PostModelDetailSerializer, PostModelSerializer

#MODELS
from posts.models import Post


class PostViewSet(viewsets.GenericViewSet, 
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        #Get users posts
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
