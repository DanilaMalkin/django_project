from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Articles
from .permissions import *
from .serializers import ArticlesSerializer

class ArticlesAPIList(generics.ListCreateAPIView):
    queryset = Articles.objects.filter(is_published=True)
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class MyArticlesAPIList(generics.ListCreateAPIView):
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        queryset = Articles.objects.filter(owner=user)
        return queryset


class ArticlesAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ArticlesAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ArticlesAPIDetailView(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    lookup_field = 'owner'
    def get_queryset(self):
        owner_id = self.kwargs['owner']
        queryset = Articles.objects.filter(owner_id=owner_id)
        return queryset



