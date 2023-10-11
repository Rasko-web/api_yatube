from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import GroupViewSet, PostViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts', PostViewSet)

v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
]
