from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import person

class PersonAPITest(TestCase):
    def setUp(self):
        self.person1 = person.objects.create(
            name="Alice",
            email="alice@example.com",
            gender="female",
            address="123 Elm St"
        )
        self.person2 = person.objects.create(
            name="Bob",
            email="bob@example.com",
            gender="male",
            address="456 Oak St"
        )

    def test_list_people(self):
        # Test GET request to retrieve all people
        client = APIClient()
        response = client.get('/api/people/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if two persons were returned

    def test_retrieve_person(self):
        # Test GET request to retrieve a specific person by ID
        client = APIClient()
        response = client.get(f'/api/people/{self.person1.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Alice")

    def test_create_person(self):
        # Test POST request to create a new person
        client = APIClient()
        data = {
            "name": "New Person",
            "email": "new@example.com",
            "gender": "male",
            "address": "123 Test St"
        }
        response = client.post('/api/people/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Person")

    def test_update_person(self):
        # Test PUT request to update a specific person by ID
        client = APIClient()
        data = {
            "name": "Updated Name",
            "email": "updated@example.com",
            "gender": "female",
            "address": "456 Updated St"
        }
        response = client.put(f'/api/people/{self.person2.id}/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Updated Name")  # Check if the name was updated

    def test_delete_person(self):
        # Test DELETE request to delete a specific person by ID
        client = APIClient()
        response = client.delete(f'/api/people/{self.person1.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
