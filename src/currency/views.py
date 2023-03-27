from django.shortcuts import render
from asgiref.sync import sync_to_async

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from .models import ExangeRate


class ExangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExangeRate
        fields = ('pk', 'currency', 'value')


# Create your views here.

@sync_to_async
@api_view(['GET', 'POST'])
def rates_list(request):
    if request.method == 'GET':
        data = ExangeRate.objects.all()
        serializer = ExangeRateSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = ExangeRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@sync_to_async
@api_view(['PUT', 'DELETE'])
def rate_detail(request, id):
    try:
        order = ExangeRate.objects.get(id=id)
    except ExangeRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ExangeRateSerializer(
            order, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
