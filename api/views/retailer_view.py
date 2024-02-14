from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Retailer
from ..serializers.retailer_serializer import RetailerSerializer

class RetailerList(APIView):
    def get(self,request, format=None):
        retailers = Retailer.objects.all()
        serializer = RetailerSerializer(retailers, many=True)
        return Response(serializer.data)

class RetailerCreate(APIView):
    def post(self, request, format=None):
        serializer = RetailerSerializer(data=request.data)
        if serializer.is_valid():
            created_retailer = serializer.save()
            return Response(f'Criado com sucesso. Id: {created_retailer.id}', status=status.HTTP_201_CREATED)
        return Response('Erro inesperado',status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetailerDetail(APIView):
    def __get_object(self, id):
        return Retailer.objects.filter(pk=id).first()
    
    def get(self, request, id, format=None):
        instance = self.__get_object(id)
        if not instance:
            return Response('Varejista não existe', status=status.HTTP_404_NOT_FOUND)
        serializer = RetailerSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        instance = instance = self.__get_object(id)
        if not instance:
            return Response('Objeto Varejista inexistente.', status=status.HTTP_404_NOT_FOUND)
        serializer = RetailerSerializer(instance=instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            updated_instance = serializer.save()
            return Response(f'Atualizado com sucesso. Id: {updated_instance.id}', status=status.HTTP_200_OK)
        
        return Response('Erro inesperado', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
