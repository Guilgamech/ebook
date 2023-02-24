from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.helpers.message import enviar_email_registro

from apps.user.models import User
from apps.user.serializers import LogoutSerializer, UserSerializer


class LogoutView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=None, status=status.HTTP_205_RESET_CONTENT)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    @action(detail=False, methods=["post"])
    def registrar(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            enviar_email_registro(user)
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

    def create(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().partial_update(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def list(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().list(request, *args, **kwargs)
        else:
            raise PermissionDenied()
