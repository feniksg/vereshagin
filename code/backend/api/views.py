from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import I10ResultsSetPagination, I100ResultsSetPagination
from . import models
from . import serializers
from .filters import MediaItemFilter, BookFilter, ArtFilter


class MediaCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.MediaCategory.objects.all()
    serializer_class = serializers.MediaCategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I10ResultsSetPagination


class MediaItemViewSet(viewsets.ModelViewSet):
    queryset = models.MediaItem.objects.all()
    serializer_class = serializers.MediaItemSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I10ResultsSetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend]
    filterset_class = MediaItemFilter


class BiographyItemViewSet(viewsets.ModelViewSet):
    queryset = models.BiographyItem.objects.all()
    serializer_class = serializers.BiographyItemSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I10ResultsSetPagination


class ArtCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ArtCategory.objects.all()
    serializer_class = serializers.ArtCategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I10ResultsSetPagination





class ArtSeriesViewSet(viewsets.ModelViewSet):
    queryset = models.ArtSeries.objects.all()
    serializer_class = serializers.ArtSeriesSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I10ResultsSetPagination


class ArtItemViewSet(viewsets.ModelViewSet):
    queryset = models.ArtItem.objects.all()
    serializer_class = serializers.ArtItemSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I100ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = I10ResultsSetPagination
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    filterset_class = BookFilter
    search_fields = ['title']
