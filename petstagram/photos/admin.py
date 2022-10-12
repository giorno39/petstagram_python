from django.contrib import admin

# Register your models here.
from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "date_of_publication",
        "description",
        'location',
        "get_tagged_pets",
    ]

    @staticmethod
    def get_tagged_pets(obj):
        tagged_pets = ", ".join([pet.name for pet in obj.tagged_pets.all()])
        return tagged_pets
