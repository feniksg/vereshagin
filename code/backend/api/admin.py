from django.contrib import admin
from . import models

@admin.register(models.MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo')
    search_fields = ('title', 'text')


@admin.register(models.BiographyItem)
class BiographyItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'partro', 'gender', 'birth', 'death')
    search_fields = ('surname', 'name', 'partro')


@admin.register(models.ArtCategory)
class ArtCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')




@admin.register(models.ArtSeries)
class ArtSeriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.ArtItem)
class ArtItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'category', 'series')
    search_fields = ('title', 'short_desc', 'desc')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'away_link')
    search_fields = ('title', 'author')
