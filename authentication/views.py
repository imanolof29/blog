#DJANGO REST FRAMEWORK
from rest_framework import generics, authentication, permissions 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#SERIALIZER
from authentication.serializers import AuthTokenSerializer, UserModelSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user"""
    serializer_class = UserModelSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserModelSerializer
    authentication_class = (authentication.TokenAuthentication,)
    permission_class = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


