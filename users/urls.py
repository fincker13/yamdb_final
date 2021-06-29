from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ConfirmationAPIView, UsersViewSet, get_token

router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet)

auth_urlpatterns = [
    path('email/', ConfirmationAPIView.as_view(), name='confirmation'),
    path('token/', get_token, name='get_token'),
]

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include(auth_urlpatterns)),
]
