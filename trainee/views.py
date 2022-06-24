from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .Serializers import  *


@api_view(['GET'])
def list(request,id=0):
    if id==0 :
          trainess=Trainee.objects.all()
          if trainess :
                 data = Traineeserilzer(trainess, many=True)
                 print(data.data)
                 return Response(data.data)
          else:
              return Response("data is empty")
    else:
        trainess = Trainee.objects.get(id=id)
        if trainess:
              data=Traineeserilzer(trainess)
              return Response(data.data)
        else:
            return Response({'error': 'trainee not found'})



@api_view(['POST'])
def insert(request):
    print(request.data)
    t=Traineeserilzer(data=request.data)
    if t.is_valid():
        t.save()
        return Response(t.data)
    else:
        return Response(status=status.HTTP_306_RESERVED)

@api_view(['PUT'])
def update(request,id):
    t = Trainee.objects.get(id=id)
    data = Traineeserilzer(instance=t, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['delete'])
def delete(request,id):
    traines = Trainee.objects.get(id=id)
    traines.delete()
    return Response(status=status.HTTP_202_ACCEPTED)