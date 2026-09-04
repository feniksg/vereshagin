from django.urls import path
from .views import (
    MediaCategoryViewSet,
    MediaItemViewSet,
    BiographyItemViewSet,
    ArtCategoryViewSet,
    ArtSeriesViewSet,
    ArtItemViewSet,
    BookViewSet,
)

urlpatterns = [
    # MediaCategory
    path('media-categories', MediaCategoryViewSet.as_view({'get': 'list'})),
    path('media-categories/<int:pk>', MediaCategoryViewSet.as_view({'get': 'retrieve'})),

    # MediaItem
    path('media-items', MediaItemViewSet.as_view({'get': 'list'})),
    path('media-items/<int:pk>', MediaItemViewSet.as_view({'get': 'retrieve'})),

    # BiographyItem
    path('biographies', BiographyItemViewSet.as_view({'get': 'list'})),
    path('biographies/<int:pk>', BiographyItemViewSet.as_view({'get': 'retrieve'})),

    # ArtCategory
    path('art-categories', ArtCategoryViewSet.as_view({'get': 'list'})),
    path('art-categories/<int:pk>', ArtCategoryViewSet.as_view({'get': 'retrieve'})),

    # ArtSeries
    path('art-series', ArtSeriesViewSet.as_view({'get': 'list'})),
    path('art-series/<int:pk>', ArtSeriesViewSet.as_view({'get': 'retrieve'})),

    # ArtItem
    path('art-items', ArtItemViewSet.as_view({'get': 'list'})),
    path('art-items/<int:pk>', ArtItemViewSet.as_view({'get': 'retrieve'})),

    # Book
    path('books', BookViewSet.as_view({'get': 'list'})),
    path('books/<int:pk>', BookViewSet.as_view({'get': 'retrieve'})),
]