from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Student
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Student.objects.all()
    serializer_class = RegisterSerializer
    
    