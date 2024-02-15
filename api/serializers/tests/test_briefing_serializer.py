from django.test import TestCase

from ...models import Category, Retailer, Briefing
from ..briefing_serializer import BriefingSerializer
    
class BriefingSerializerTest(TestCase):
    def test_valid_data(self):
        # arrange
        data = {
            'name': 'briefing 1',
            'responsible': 'Joao',
            'available': 1,
            'category_id': 1,
            'retailer_id': 1
        }
        serializer = BriefingSerializer(data=data)
        
        # act
        is_valid = serializer.is_valid()

        # assert
        self.assertTrue(is_valid)
    
    def test_invalid_data(self):
        data = {
            'available': 1,
            'category_id': 1,
            'retailer_id': 1
        }
        serializer = BriefingSerializer(data=data)
        
        # act
        is_valid = serializer.is_valid()
        errors = serializer.errors

        # assert
        self.assertFalse(is_valid)
        self.assertIn('name', errors)
        self.assertIn('responsible', errors)

    def test_save_valid_briefing(self):
        category = Category.objects.create(
            name="category1",
            description="category one"
        )
        retailer = Retailer.objects.create(
            name="retailer1"
        )

        data = {
            'name': 'briefing 1',
            'responsible': 'Joao',
            'available': 1,
            'category_id': category.id,
            'retailer_id': retailer.id
        }
        serializer = BriefingSerializer(data=data)
        
        serializer.is_valid()
        created_briefing = serializer.save()

        self.assertIsNotNone(created_briefing.id)

    def test_not_save_invalid_briefing(self):
        data = {
            'available': 1,
            'category_id': 1,
            'retailer_id': 1
        }
        serializer = BriefingSerializer(data=data)
        
        with self.assertRaises(Exception):
            serializer.is_valid()
            serializer.save()
        
        self.assertEqual(Briefing.objects.count(), 0)
 