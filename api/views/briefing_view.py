from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.briefing_serializer import BriefingSerializer
from ..models import Category, Retailer, Briefing

class BriefingCreate(APIView):
    def __check_category(self, category_id):
        return Category.objects.filter(pk=category_id).exists()
    
    def __check_retailer(self, retailer_id):
        return Retailer.objects.filter(pk=retailer_id).exists()

    def post(self, request):
        serializer = BriefingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            category_id = serializer.validated_data['category_id']
            retailer_id = serializer.validated_data['retailer_id']
            
            has_category = self.__check_category(category_id)
            has_retailer = self.__check_retailer(retailer_id)

            if has_category is False or has_retailer is False:
                return Response('Objeto Briefing inválido.', status=status.HTTP_400_BAD_REQUEST)

            created_briefing = serializer.save()
            return Response(f'Criado com sucesso. Id: {created_briefing.id}', status=status.HTTP_201_CREATED)
        return Response('Erro inesperado', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BriefingList(APIView):
    def get(self, request):
        instances = Briefing.objects.all()
        serializer = BriefingSerializer(instances,many=True)
        return Response(serializer.data)

class BriefingDetail(APIView):
    def __get_object(self, id):
        return Briefing.objects.filter(pk=id).first()

    def put(self, request, id):
        try:
            instance = self.__get_object(id)
            if not instance:
                return Response('Briefing não existe',status=status.HTTP_404_NOT_FOUND) 
            serializer = BriefingSerializer(instance=instance, data=request.data, partial=True)
            if serializer.is_valid():
                updated_instance = serializer.save()
                return Response(f'Atualizado com sucesso. Id: {updated_instance.id}', status=status.HTTP_200_OK)
            return Response('Objeto Briefing inválido.', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Erro inesperado', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, id):
        try:
            instance = self.__get_object(id)
            if not instance:
                return Response('Briefing não existe',status=status.HTTP_404_NOT_FOUND)
            serializer = BriefingSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response('Requisição inválida', status=status.HTTP_400_BAD_REQUEST)