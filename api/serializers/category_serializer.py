from ..models import Category
from rest_framework import  serializers

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
    
    def validate_name(self, name):
        if not name or name == '':
            raise serializers.ValidationError('Insira um nome valido')
        return name
    
    def validate_description(self, description):
        if not description or description == '':
            raise serializers.ValidationError('Insira uma descricao valida')
        return description



       