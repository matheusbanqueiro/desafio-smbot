from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Contact
import uuid

class ContactAPITestCase(APITestCase):

    def setUp(self):
        
        self.contact_uuid = uuid.uuid4()
        self.contact = Contact.objects.create(
            uuid=self.contact_uuid,
            name="Test User",
            phone="1234567890"
        )
        self.contact_url = reverse('list_contactss')
        self.manager_url = reverse('contact_manager')
        self.bulk_create_url = reverse('bulk_create_contacts') 
        
    def test_list_contactss(self):
        """Teste de integração para obter todos os contatos"""
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_single_contact(self):
        """Teste de integração para obter um contato específico"""
        response = self.client.get(self.manager_url, {'uuid': str(self.contact.uuid)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.contact.name)

    def test_create_contact(self):
        """Teste de integração para criar um novo contato"""
        data = {
            "uuid": str(uuid.uuid4()),
            "name": "New Contact",
            "phone": "0987654321"
        }
        response = self.client.post(self.manager_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)

    def test_update_contact(self):
        """Teste de integração para atualizar um contato existente"""
        update_data = {
            "uuid": str(self.contact.uuid),
            "name": "Updated Name"
        }
        response = self.client.put(self.manager_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Updated Name")

    def test_delete_contact(self):
        """Teste de integração para deletar um contato existente"""
        delete_data = {"uuid": str(self.contact.uuid)}
        response = self.client.delete(self.manager_url, delete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Contact.objects.filter(uuid=self.contact.uuid).exists())

    def test_bulk_create_contacts(self):
        """Teste de integração para criar contatos em massa"""
        data = {
            "contacts": [
                {"name": "Jane Smith", "phone": "1234567890"},
                {"name": "John Silveira", "phone": "0987654321"}
            ]
        }
        response = self.client.post(self.bulk_create_url, data, format='json')
        
        
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn('task_id', response.data)