from rest_framework import serializers
from ..models import Briefing

class BriefingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    retailer = serializers.StringRelatedField(read_only=True)
    release_date = serializers.DateTimeField(read_only=True)
    category_id = serializers.IntegerField()
    retailer_id = serializers.IntegerField()

    class Meta:
        model = Briefing
        fields = ['id', 'name','responsible','release_date','available','category_id', 'retailer_id', 'category', 'retailer']
    
    def validate_name(self, name):
        if not name:
            raise serializers.ValidationError('Insira um nome valido')
        return name

    def validate_responsible(self, responsible):
        if not responsible:
            raise serializers.ValidationError('Insira um responsavel valido')
        return responsible