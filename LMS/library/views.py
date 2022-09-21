from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from library.serializer import BookModelSerializer
from library.models import Book
from rest_framework.permissions import AllowAny,IsAuthenticated

class BookOperations(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = [IsAuthenticated, ]
        return super(self.__class__, self).get_permissions()
