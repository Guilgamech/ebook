
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Books
from .serializers import BookSerializer, BookReadSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    read_serializer_class = BookReadSerializer
    permission_classes = (IsAuthenticated,)


