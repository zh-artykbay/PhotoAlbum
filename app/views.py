from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer, AlbumWithPhotosSerializer
from rest_framework import generics, filters
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend


class AlbumList(generics.ListAPIView):
    serializer_class = AlbumSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']

    def get_queryset(self):
        """
        This view should return a list of all the Albums
        for the currently authenticated user.
        """
        user = self.request.user
        return Album.objects.filter(author=user)


class AlbumCreate(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDelete(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoList(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['album', 'tags__name']
    ordering_fields = ['album', 'created']

    def get_queryset(self):
        """
        This view should return a list of all the Images
        for the currently authenticated user.
        """
        user = self.request.user
        return Photo.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PhotoCreate(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PhotoUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDelete(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetail(generics.RetrieveAPIView):
    permission_classes = [IsOwner]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


#returns Album list with images
#orders with images

class AlbumWithPhotosList(generics.ListAPIView):
    permission_classes = [IsOwner]
    serializer_class = AlbumWithPhotosSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Albums with Images
        for the currently authenticated user.
        """
        user = self.request.user
        return Album.objects.filter(author=user)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['photos']
