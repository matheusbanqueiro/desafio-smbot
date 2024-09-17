from django.test import TestCase
from ..models import Contact
import uuid
from django.utils import timezone

class ContactModelTest(TestCase):

    def setUp(self):
       
        self.contact = Contact.objects.create(
            uuid=uuid.uuid4(),
            name="Test User",
            phone="1234567890",
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def test_contact_creation(self):
        """Testando se o contato foi criado de maneira correta"""
        contact = self.contact
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(contact.__str__(), f'Uuid: {contact.uuid} | Name: {contact.name}')

    def test_default_values(self):
        """Testa os valores padrão dos campos"""
        contact = Contact.objects.create(
            uuid=uuid.uuid4(),
            name="Another User",
            phone="0987654321"
        )
        self.assertIsNotNone(contact.created_at)
        self.assertIsNotNone(contact.updated_at)

    def test_updated_at_on_update(self):
        """Testando se o campo updated_at foi atualizado com sucesso e não mantém seu valor antigo"""
        contact = self.contact
        old_updated_at = contact.updated_at
        contact.name = "Updated User"
        contact.save()
        contact.refresh_from_db()
        self.assertNotEqual(contact.updated_at, old_updated_at)