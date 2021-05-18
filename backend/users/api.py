from users.models import User
from rest_framework import viewsets, permissions
from .serializers import userSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = userSerializer