from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Salom1, Salom2, Salom3, Salom4
from .serializers import Salom1Serializer, Salom2Serializer, Salom3Serializer, Salom4Serializer


class Salom1APIView(ListCreateAPIView):
    queryset = Salom1.objects.all()
    serializer_class = Salom1Serializer


class Salom2APIView(ListCreateAPIView):
    queryset = Salom2.objects.all()
    serializer_class = Salom2Serializer


class Salom3APIView(ListCreateAPIView):
    queryset = Salom3.objects.all()
    serializer_class = Salom3Serializer


class Salom4APIView(ListCreateAPIView):
    queryset = Salom4.objects.all()
    serializer_class = Salom4Serializer
