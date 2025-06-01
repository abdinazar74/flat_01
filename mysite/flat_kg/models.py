from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)

class Agent(UserProfile):
    info = models.CharField(max_length=145)
    agent_image = models.ImageField(upload_to='agent_images')
    LAN_CHOICES = (
        ('English', 'English'),
        ('Russian', 'Russian'),
        ('Kyrgyz', 'Kyrgyz'),
        ('French', 'French'),
        ('Chinese', 'Chinese')
    )
    languages = MultiSelectField(choices=LAN_CHOICES,
                                 max_choices=5,
                                 max_length=112)
    # phone_number = PhoneNumberField(null=True, blank=True)
    experience_since = models.DateField()
    areas = models.CharField(max_length=123)
    company = models.ImageField(upload_to='company_images')


class Apartment(models.Model):
    DEAL_TYPE_CHOICES = (
    ('Buy', 'Buy'),
    ('Rent', 'Rent')
    )
    deal = models.CharField(choices=DEAL_TYPE_CHOICES)
    apartment_name = models.CharField(max_length=123)
    apartment_image = models.ImageField(upload_to='apartment_images')
    SERIAS_CHOICES = (
        ('Elite', 'Elite'),
        ('105', '105'),
        ('106', '106'),
        ('104', '104'),
        ('Individual Project', 'Individual Project')
    )
    serias = models.CharField(max_length=53, choices=SERIAS_CHOICES)
    numberroom = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 7)])
    BATHROOM_CHOICES = (
        ('Combined', 'Combined'),
        ('Separate', 'Separate')
    )
    bathroom = models.CharField(choices=BATHROOM_CHOICES)
    TYPE_PARK = (
        ('Ground', 'Ground'),
        ('Underground', 'Underground'),
        ('No', 'No')
    )
    parking = models.CharField(choices=TYPE_PARK)
    location = models.CharField(max_length=43)
    floor = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(14)])

    price = models.DecimalField(decimal_places=2, max_digits=10)
    PROPERTY_TYPE = (
    ('Apartment', 'Apartment'),
    ('Townhouse', 'Townhouse'),
    ('Penthouse', 'Penthouse'),
    ('Office', 'Office')
    )
    about_property = models.TextField()
    AMINITIES_CHOICES = (
        ('Balkony', 'Balkony' ),
        ('Microwave', 'Microwave'),
        ('WiFi', 'WiFi'),
        ('Coverad parking', 'Coverad parking'),
        ('TV', 'TV'),
        ('Central heating','Central heating'),
        ('Washing machine', 'Washing machine'),
        ('Air-conditioner', 'Air-conditioner'),
        ('Tableware', 'Tableware'),
        ('Swimming pool', 'Swimming pool'),
        ('Gym', 'Gym')
    )
    aminities = MultiSelectField(choices=AMINITIES_CHOICES,
                                 max_choices=5,
                                 max_length=43)
    address = models.CharField(max_length=133)
    owner = models.ForeignKey(UserProfile, related_name='apart_owner',on_delete=models.CASCADE)
    square = models.PositiveSmallIntegerField()
    # agent = models.ForeignKey(Agent,related_name='flat_agent', on_delete=models.CASCADE)

class HousePictures(models.Model):
    house_pictures = models.ImageField(upload_to='house_photos')
    apartment = models.ForeignKey(Apartment, related_name='house_pictures', on_delete=models.CASCADE)

class ApartmentBonus(models.Model):
    apartment = models.ForeignKey(Apartment,related_name='house_bonus', on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icons')
    bonus_name = models.CharField(max_length=143)

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.CharField(max_length=123)

