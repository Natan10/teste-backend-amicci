from django.test import TestCase
from rest_framework import serializers

from ...models import Category
from ..category_serializer import CategorySerializer

class CategorySerializerTest(TestCase):
    def test_valid_data(self):
        # arrange
        data = {'name': 'category one', 'description': 'category one description'}
        serializer = CategorySerializer(data=data)
        
        # act
        is_valid = serializer.is_valid()

        # assert
        self.assertTrue(is_valid)
    
    def test_invalid_data(self):
        data = {'description': 'category one description'}
        serializer = CategorySerializer(data=data)
        
        # act
        is_valid = serializer.is_valid()
        errors = serializer.errors

        # assert
        self.assertFalse(is_valid)
        self.assertIn('name', errors)
 
    def test_save_valid_category(self):
        data = {'name': 'category one', 'description': 'category one description'}
        serializer = CategorySerializer(data=data)

        serializer.is_valid()
        created_instance = serializer.save()

        self.assertIsNotNone(created_instance.id)

    def test_not_save_invalid_category(self):
        data = {'description': 'category one description'}
        serializer = CategorySerializer(data=data)

        with self.assertRaises(Exception):
            serializer.is_valid()
            serializer.save()
        
        self.assertEqual(Category.objects.count(), 0)

