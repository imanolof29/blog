#DJANGO
from django.urls import path, include

#DJANGO REST FRAMEWORK
from rest_framework.routers import DefaultRouter

#VIEWS
from posts.views import PostViewSet

app_name = 'posts'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
#router.register(r'posts/<int:id>/comments/', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]