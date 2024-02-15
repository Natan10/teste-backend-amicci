from rest_framework import  serializers

from ..models import Retailer,Vendor

class PartialVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'name', 'vendors']

    id = serializers.IntegerField(read_only=True)
    vendors = PartialVendorSerializer(many=True, read_only=True)
       
    def validate_name(self, name):
        if not name:
            raise serializers.ValidationError('Insira um nome valido')
        return name



       