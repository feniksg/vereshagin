import django_filters
from django.utils import timezone
from . import models  # подставь правильный путь к твоим моделям

class MediaItemFilter(django_filters.FilterSet):
    # кастомный фильтр для виртуального поля `status`
    status = django_filters.CharFilter(method='filter_by_status')

    class Meta:
        model = models.MediaItem
        fields = ['category']  # ⚠️ только реальные поля модели

    def filter_by_status(self, queryset, name, value):
        now = timezone.now()

        if value == 'Прошло':
            return queryset.filter(created_at__date__lt=now.date())
        elif value == 'Идёт':
            return queryset.filter(created_at__date=now.date())
        elif value == 'Будет':
            return queryset.filter(created_at__date__gt=now.date())
        return queryset.none()
    
class BookFilter(django_filters.FilterSet):
    year__gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Год издания от')
    year__lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='Год издания до')

    class Meta:
        model = models.Book
        fields = ['year__gte', 'year__lte'] 
        
class ArtFilter(django_filters.FilterSet):
    year__gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label='Год издания от')
    year__lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label='Год издания до')
    
    class Meta:
        model = models.ArtItem
        fields = ['year__gte', 'year__lte', 'category', 'series'] 