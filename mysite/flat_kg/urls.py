from rest_framework.urls import path
from .views import (ReviewEditAPIView, ReviewCreateAPIView, ReviewListAPIView,
                    ApartmentListAPIView,ApartmentListTwoAPIView,ApartmentCreateAPIView,
                    ApartmentDetailAPIView,AgentListAPIView,AgentCreateAPIView,
                    AgentDetailAPIView,UserProfileViewSets)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('UserProfile', UserProfileViewSets, basename='UserProfile')

urlpatterns = [
    path('apartments/', ApartmentListAPIView.as_view(), name='apartment_list'),
    path('apartment/', ApartmentListTwoAPIView.as_view(), name='apartment_list_second'),
    path('apartment/<int:pk>/', ApartmentDetailAPIView.as_view(), name='apartment_detail'),
    path('apartment/create/', ApartmentCreateAPIView.as_view(), name='apartment_create'),

    path('agents/', AgentListAPIView.as_view(), name='agent_list' ),
    path('agents/create/', AgentCreateAPIView.as_view(), name='agent_create'),
    path('agents/<int:pk>/', AgentDetailAPIView.as_view(), name='agent_detail'),

    path('reviews/', ReviewListAPIView.as_view(), name='reviews_list'),
    path('reviews/create', ReviewCreateAPIView.as_view(), name='reviewsCreate')

]