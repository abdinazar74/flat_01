from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Agent)
class ProductTranslationOptions(TranslationOptions):
    fields = ('areas',)

@register(Apartment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('location','about_property', 'address')

@register(Review)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)

@register(ApartmentBonus)
class ProductTranslationOptions(TranslationOptions):
    fields = ('bonus_name',)