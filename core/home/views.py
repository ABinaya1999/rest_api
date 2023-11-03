from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def home(request):
    record = Student.objects.all()
    serializers = StudentSerializers(record,many=True)
    return Response({'status':200,'students':serializers.data})
    