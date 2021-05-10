from rest_framework import serializers
from .models import Single


class SingleSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    class Meta:
        model = Single
        fields = ['name', 'youtube_views', 'artist']

# set return artist with aka
    def get_artist(self, instance):
        return instance.artist.aka


class SingleSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = ['name', 'youtube_views', 'artist']
