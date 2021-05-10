from rest_framework import viewsets, status
from .models import Single
from .serializers import SingleSerializer, SingleSerializerSave
from rest_framework.decorators import api_view
from rest_framework.response import Response


class SingleViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def all(self):
        if self.method == 'GET':
            single = Single.objects.all()
            single_serializer = SingleSerializer(single, many=True)
            return Response(single_serializer.data)

    @api_view(['POST'])
    def create(self):
        if self.method == 'POST':
            single_serializer = SingleSerializerSave(data=self.data, many=False)
            if single_serializer.is_valid():
                single_serializer.save()
                return Response(single_serializer.data, status=status.HTTP_201_CREATED)
            return Response(single_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#handle error