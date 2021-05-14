from django.contrib import admin
from .models import Cat


# Register your models here.

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['breed', 'body_type', 'location_origin', 'coat_length', 'pattern']
    list_filter = ['breed', 'body_type', 'location_origin',  'coat_length', 'pattern']

