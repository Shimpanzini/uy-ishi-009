from rest_framework.serializers import ModelSerializer
from .models import Salom1


class Salom1Serializer(ModelSerializer):
    class Meta:
        model = Salom1
        fields = '__all__'
