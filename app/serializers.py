from rest_framework import serializers
from .models import Album, Photo
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Album
        read_only_fields = ('author', 'created')


class PhotoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        fields = '__all__'
        model = Photo
        read_only_fields = ('author', 'created')


class AlbumWithPhotosSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Album
        read_only_fields = ('author', 'created')