from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class HousePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePictures
        fields = '__all__'

class ApartmentBonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentBonus
        fields = '__all__'

class AgentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'first_name', 'last_name',]

class ApartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['apartment_name', 'location', 'price', 'apartment_image']


class AgentDetailSerializer(serializers.ModelSerializer):
    flat_agent = ApartmentListSerializer(read_only=True, many=True)
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name','flat_agent', 'languages', 'areas',
                  'experience_since', 'phone_number', 'email', 'company']

class AgentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class ApartmentListTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['property_type', 'apartment_name', 'apartment_image', 'house_bonus','location', 'price']

class ApartmentDetailSerializer(serializers.ModelSerializer):
    agent = AgentListSerializer()
    owner = UserProfileSerializer()
    class Meta:
        model = Apartment
        fields = ['property_type', 'apartment_name', 'apartment_image', 'house_bonus','location', 'price'
                  'deal', 'serias', 'numberroom', 'bathroom', 'parking', 'location', 'price', 'about_property',
                  'aminities', 'address', 'owner', 'square', 'agent']

class ApartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'