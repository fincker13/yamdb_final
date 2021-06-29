from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_v1.views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                          ReviewViewSet, TitleViewSet)

v1_router = DefaultRouter()
v1_router.register('categories', CategoriesViewSet, basename='categories')
v1_router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
v1_router.register('genres', GenresViewSet, basename='genres')
v1_router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
v1_router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('', include(v1_router.urls)),
]
