from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from general.serializers import CookieTokenRefreshSerializer, MyTokenObtainPairSerializer
from datetime import timedelta

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
