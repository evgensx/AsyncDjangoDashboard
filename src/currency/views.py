from django.shortcuts import render
from asgiref.sync import sync_to_async

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from .models import ExangeRate


import datetime
from django.http import HttpResponse


async def current_datetime(request):
    rate = await ExangeRate.objects.aupdate_or_create(currency='usd', defaults={'value': 12.3456})
    print(rate)
    html = "<html><body>It is now %s</body></html>" % rate[0]
    return HttpResponse(html)


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


# async def edit(request, id):
#     try:
#         rate = ExangeRate.objects.aget(id=id)
#         if request.method == "POST":
#             rate. = request.POST.get("name")
#             rate.
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"person": person})
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")