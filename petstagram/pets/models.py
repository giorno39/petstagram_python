from django.db import models

# Create your models here.
from django.utils.text import slugify

"""
Let us start by creating the Pet model.
The fields Name and Pet Photo are required:
•	Name - it should consist of a maximum of 30 characters.
•	Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
•	Date of Birth - pet's day, month, and year of birth
•	Slug - a slug automatically generated using the pet's name and the pet's id, separated by a "-" (dash).
"""


class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    personal_pet_photo = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            temp_slug = slugify(f"{self.name}-{self.id}")
            self.slug = temp_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
