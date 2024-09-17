# contacts/tasks.py
from celery import shared_task
from .serializers import ContactSerializer

@shared_task
def create_contacts(contact_list):
    """
    Cria contatos a partir de uma lista de dicionários com dados dos contatos.
    """
    contacts_created = []
    for contact_data in contact_list:
        serializer = ContactSerializer(data=contact_data)
        if serializer.is_valid():
            contact = serializer.save()
            contacts_created.append(contact)
        else:
            print(f"Validation error for data: {contact_data} - {serializer.errors}")
    
    return [contact.uuid for contact in contacts_created]
