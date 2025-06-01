from django.contrib import admin
from .models import UserProfile, Apartment, Agent, Review, HousePictures, ApartmentBonus
from modeltranslation.admin import TranslationAdmin

class ApartmentBonusInline(admin.TabularInline):
    model = ApartmentBonus
    extra = 1

class HousePicturesInline(admin.TabularInline):
    model = HousePictures
    extra = 1

@admin.register( Apartment )
class ProductAdmin(TranslationAdmin):
    inlines = [ApartmentBonusInline, HousePicturesInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Agent, Review,ApartmentBonus )
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(HousePictures)