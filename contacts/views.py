from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .tasks import create_contacts
from .models import Contact
from .serializers import ContactSerializer

@api_view(['GET'])
def get_contact(request):
    if request.method == 'GET':
        
        cache_key = 'all_contacts'

        contacts_data = cache.get(cache_key)

        if not contacts_data:
            contacts = Contact.objects.all()

            serializer = ContactSerializer(contacts, many=True)

            contacts_data = serializer.data
            cache.set(cache_key, contacts_data, timeout=60)

        return Response(contacts_data)

    return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def bulk_create_contacts(request):
    
    contact_list = request.data.get('contacts', [])
    if not contact_list:
        return Response({"error": "No contacts provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Adiciona a tarefa à fila Celery
    task = create_contacts.delay(contact_list)
    
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def contact_manager(request):
    if request.method == 'GET':
        uuid = request.GET.get('uuid')
        if not uuid:
            return Response({"error": "UUID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            contact = Contact.objects.get(pk=uuid)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"error": "UUID is required for updating"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            contact = Contact.objects.get(pk=uuid)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"error": "UUID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            contact = Contact.objects.get(pk=uuid)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
        
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
