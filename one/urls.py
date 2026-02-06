from django.urls import path
from .views import Salom1APIView

urlpatterns = [
    path('salom1/', Salom1APIView.as_view()),
]
