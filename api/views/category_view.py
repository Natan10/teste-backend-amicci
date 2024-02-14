from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Category

from ..serializers.category_serializer import CategorySerializer

class CategoryList(APIView):
    def get(self,request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get(self, request, id, format=None):
        instance = Category.objects.filter(pk=id).first()
        if not instance:
            return Response('Categoria não existe',status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(instance=instance)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            created_category = serializer.save()
            return Response(f'Criada com sucesso. Id: {created_category.id}',status=status.HTTP_201_CREATED)
        return Response('Erro inesperado',status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id, format=None):
        instance = Category.objects.filter(pk=id).first()
        if not instance:
            return Response('Objeto Categoria inexistente.',status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated = serializer.save()
            return Response(f'Atualizado com sucesso. Id: {updated.id}',status=status.HTTP_200_OK)
        return Response('Erro inesperado',status=status.HTTP_500_INTERNAL_SERVER_ERROR)
