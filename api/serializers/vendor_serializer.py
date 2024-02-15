from rest_framework import serializers
from ..models import Vendor, Retailer

class PartialRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'name']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name','retailer', 'retailer_id']
    
    id = serializers.IntegerField(read_only=True)
    retailer = PartialRetailerSerializer(read_only=True)
