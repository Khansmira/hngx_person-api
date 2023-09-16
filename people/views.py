from django.http import JsonResponse
from .models import person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def person_list(request, format=None):
    #get all people, serialize them and return json
    if request.method == 'GET':
        people = person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id, format=None):

    try:
        person_dict = person.objects.get(pk=id)
    except person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person_dict)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person_dict, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person_dict.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
