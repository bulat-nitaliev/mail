from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from general.api.serializers import UserRegistrationSerializer, UserListSerializer
from general.models import User




class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    def get_serializer_class(self):
        if self.action == 'create':
           return UserRegistrationSerializer
        return UserListSerializer
    
