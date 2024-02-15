from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Vendor,Retailer
from ..serializers.vendor_serializer import VendorSerializer

class VendorList(APIView):
    def get(self,request, format=None):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

class VendorCreate(APIView):
    def post(self, request, format=None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            created_vendor = serializer.save()
            return Response(f'Criado com sucesso. Id: {created_vendor.id}', status=status.HTTP_201_CREATED)
        return Response('Erro inesperado',status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VendorDetail(APIView):
    def __get_object(self, id):
        return Vendor.objects.filter(pk=id).first()
    
    def __get_retailer(self, retailer_id):
        retailer = Retailer.objects.filter(pk=retailer_id).first()
        if not retailer:
            return None
        return retailer

    def put(self, request, id, format=None):
        instance = self.__get_object(id)
        if not instance:
            return Response('Fornecedor não existe', status=status.HTTP_404_NOT_FOUND)
        
        if 'retailer_id' in request.data.keys():
            retailer = self.__get_retailer(request.data.get('retailer_id'))
            if not retailer:
                return Response('Vajerista não existe', status=status.HTTP_404_NOT_FOUND)
            instance.retailer = retailer
            
        serializer = VendorSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_instance = serializer.save()
            return Response(f'Atualizado com sucesso. Id: {updated_instance.id}', status=status.HTTP_200_OK)
        return Response('Erro inesperado',status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            instance = self.__get_object(id)
            if not instance:
                return Response('Fornecedor não existe', status=status.HTTP_404_NOT_FOUND)
            serializer = VendorSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except: 
            return Response('Requisição inválida', status=status.HTTP_400_BAD_REQUEST)

