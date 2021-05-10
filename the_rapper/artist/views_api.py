from rest_framework import viewsets, status
from .models import Artist
from .serializers import ArtistSerializer, ArtistSerializerSave
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
    @api_view(['GET','POST'])
    def artist_list(self, format=None):
        if self.method == 'GET':
            artists = Artist.objects.all()
            artists_serializer = ArtistSerializer(artists, many=True)
            return Response(artists_serializer.data)
        elif self.method == 'POST':
            artists_serializer = ArtistSerializerSave(data=self.data)
            if artists_serializer.is_valid():
                artists_serializer.save()
                return Response(artists_serializer.data, status=status.HTTP_201_CREATED)
            return Response(artists_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET','PUT','DELETE'])
    def artist_detail(self, artistId):
        artist = Artist.objects.get(pk=artistId)
        if self.method == 'PUT':
            artists_serializer = ArtistSerializer(artist, data=self.data)
            if artists_serializer.is_valid():
                artists_serializer.save()
                return Response(artists_serializer.data, status=status.HTTP_201_CREATED)
            return Response(artists_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif self.method == 'GET':
            # artist = Artist.objects.get(pk=artistId)
            artists_serializer = ArtistSerializer(artist)
            return Response(artists_serializer.data)
        elif self.method == 'DELETE':
            # artist = Artist.objects.get(pk=artistId)
            artist.delete()
            return Response({'message': 'Artist was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # @api_view(['POST'])
    # def create(self):
    #     if self.method == 'POST':
    #         artists_serializer = ArtistSerializerSave(data=self.data, many=False)
    #         if artists_serializer.is_valid():
    #             artists_serializer.save()
    #             return Response(artists_serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(artists_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['PUT'])
    # def update(self, artistId):
    #     if self.method == 'PUT':
    #         artist = Artist.objects.get(pk=artistId)
    #         artists_serializer = ArtistSerializer(artist, data=self.data)
    #         if artists_serializer.is_valid():
    #             artists_serializer.save()
    #             return Response(artists_serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(artists_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['DELETE'])
    def remove(self, artistId):
        if self.method == 'DELETE':
            artist = Artist.objects.get(pk=artistId)
            artist.delete()
            return Response({'message': 'Artist was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # @api_view(['GET'])
    # def getById(self, artistId):
    #     if self.method == 'PUT':
    #         artist = Artist.objects.get(pk=artistId)
    #         artists_serializer = ArtistSerializer(artist)
    #         return Response(artists_serializer.data)

#handle error
