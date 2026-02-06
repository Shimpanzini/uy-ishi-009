from rest_framework.generics import ListAPIView
from .models import Salom1
from .serializers import Salom1Serializer

# Create your views here.



class Salom1APIView(ListAPIView):
    queryset = Salom1.objects.all()
    serializer_class = Salom1Serializer
