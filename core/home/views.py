from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def home(request):
    record = Student.objects.all()
    serializer = StudentSerializers(record,many=True)
    return Response({'status':200,'students':serializer.data})


@api_view(['POST'])
def create(request):
    data = request.data
    serializer = StudentSerializers(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.errors,'message':'smth wrong'})
    serializer.save()
    record = Student.objects.all()
    serializer = StudentSerializers(record,many=True)
    return Response({'status':200,'students':serializer.data,'message':'data saved'})
    