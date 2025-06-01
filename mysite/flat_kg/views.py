from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import (UserProfileSerializer,HousePictureSerializer,ApartmentDetailSerializer,
                          ApartmentListSerializer,ApartmentListTwoSerializer,
                          ReviewSerializer, AgentListSerializer,AgentCreateSerializer,
                          AgentDetailSerializer,ApartmentCreateSerializer,ApartmentBonusSerializer)
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class AgentListAPIView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentListSerializer

class AgentDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentDetailSerializer

class AgentCreateAPIView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentCreateSerializer

class ApartmentListAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer

class ApartmentListTwoAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListTwoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['deal',]
    search_fields = ['apartment_name', ]
    ordering_fields = ['price']


class ApartmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDetailSerializer

class ApartmentCreateAPIView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentCreateSerializer

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

