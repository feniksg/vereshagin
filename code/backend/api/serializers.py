from rest_framework import serializers
from . import models

class MediaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaCategory
        fields = '__all__'


class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaItem
        fields = ['id', 'created_at', 'title', 'text', 'photo', 'category', 'status']
        
    


class BiographyItemSerializer(serializers.ModelSerializer):
    childrens = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.BiographyItem
        fields = '__all__'


class ArtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArtCategory
        fields = '__all__'




class ArtSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArtSeries
        fields = '__all__'


class ArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArtItem
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
