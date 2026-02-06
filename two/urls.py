from django.urls import path
from .views import Salom1ListCreateView, Salom2ListCreateView, Salom3ListCreateView, Salom4ListCreateView

urlpatterns = [
    path('salom1/', Salom1ListCreateView.as_view()),
    path('salom2/', Salom2ListCreateView.as_view()),
    path('salom3/', Salom3ListCreateView.as_view()),
    path('salom4/', Salom4ListCreateView.as_view()),
]
