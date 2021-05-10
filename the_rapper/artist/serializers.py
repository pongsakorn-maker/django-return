from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = "_all_"
        fields = ['id', 'aka', 'name', 'age']

class ArtistSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['aka', 'name', 'age']