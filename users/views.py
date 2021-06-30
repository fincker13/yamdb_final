from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import SERVISE_EMAIL

from .models import User
from .permissions import IsSuperUserOrAdminOnly
from .serializers import AuthSerializer, ConfirmationSerializer, UserSerializer


class ConfirmationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        username = serializer.data['username']
        user_obj, user = User.objects.get_or_create(username=username,
                                                    email=email)
        confirmation_code = default_token_generator.make_token(user_obj)
        send_mail('Confirmation_code',
                  confirmation_code,
                  SERVISE_EMAIL,
                  [email])
        return Response(f'Код отправлен на {email}',
                        status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    serializer = AuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    user = get_object_or_404(User, email=email)
    confirmation_code = request.data.get('confirmation_code')
    if default_token_generator.check_token(user=user, token=confirmation_code):
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response({'confirmation_code': 'Неверный код подтверждения'},
                    status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    """ViewSet для работы с ползователями"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = (IsAuthenticated, IsSuperUserOrAdminOnly)
    pagination_class = PageNumberPagination

    @action(
        detail=False,
        permission_classes=(IsAuthenticated,),
        methods=['get', 'patch'],
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(instance=request.user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(instance=request.user,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=request.user.role)
        return Response(serializer.data, status=status.HTTP_200_OK)
