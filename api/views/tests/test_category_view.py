from django.test import TestCase
from faker import Faker

from ...models import Category

fake_data = Faker()

class CategoryViewTest(TestCase):

    def setUp(self) -> None:
        for _ in range(1,5):
            Category.objects.create(name=fake_data.company(), description=fake_data.sentence(nb_words=5))
        return super().setUp()

    def test_category_list_returns_200(self):
        # arrange
        
        # act
        response = self.client.get(f'/api/categories/')
        data = response.data
      
        # assert
        self.assertEqual(len(data), 4)
        self.assertEqual(response.status_code, 200)

    def test_get_category_by_valid_id_returns200(self):
        id = 1
        category = Category.objects.filter(pk=id).first()
        response = self.client.get(f'/api/category/{id}')
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], category.name)

    def test_get_category_by_invalid_id_returns404(self):
        response = self.client.get(f'/api/category/2000')
        self.assertEqual(response.status_code, 404)
     
    def test_create_valid_category_returns201(self):
        payload = {
            'name': fake_data.company(),
            'description': fake_data.sentence()
        }
        response = self.client.post(f'/api/category/',payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 5)
        
    def test_create_invalid_category_returns400(self):
        payload = {
            'description': fake_data.sentence()
        }
        response = self.client.post(f'/api/category/',payload)
        self.assertEqual(response.status_code, 400)

    def test_update_valid_category_returns200(self):
        id = 1
        instance = Category.objects.filter(pk=id).first()
        payload = {
            'name': 'category editado'
        }
        response = self.client.put(f'/api/category/{instance.id}', json=payload, headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    



