from rest_framework.generics import ListCreateAPiVIew
from .models import Salom1, Salom2, Salom3, Salom4
from .serializers import Salom1Serializer, Salom2Serializer, Salom3Serializer, Salom4Serializer

# Create your views here.



class Salom1ListCreateView(ListCreateAPiVIew):
    queryset = Salom1.objects.all()
    serializer_class = Salom1Serializer


class Salom2ListCreateView(ListCreateAPiVIew):
    queryset = Salom2.objects.all()
    serializer_class = Salom2Serializer


class Salom3ListCreateView(ListCreateAPiVIew):
    queryset = Salom3.objects.all()
    serializer_class = Salom3Serializer


class Salom4ListCreateView(ListCreateAPiVIew):
    queryset = Salom4.objects.all()
    serializer_class = Salom4Serializer
