from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import AppUser
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer
# Register new user
class RegisterView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserRegisterSerializer
# Login user and return DRF token
class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # create or get token
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "token": str(token.key),
            "user": {
                "id": str(user.user_id),
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_type": user.user_type,
                "phone_number": user.phone_number,
            }
        })
# Get user profile (Token required)
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user