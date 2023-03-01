from .serializers import UserTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import User
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class UserObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer

class RegisterationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_BAD_REQUEST)

class UserManagementView(APIView):
    def register(self, request):
        pass
    
    def login(self, request):
        pass

    def logout(self, request):
        pass