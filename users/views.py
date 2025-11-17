from rest_framework import generics
from .serializers import UserSignupSerializer
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    post=extend_schema(
        summary="Signup user",
        description="Register a new user",
        tags=["user"]
    )
)
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
