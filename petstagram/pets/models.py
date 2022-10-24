from django.db import models

# Create your models here.
from django.utils.text import slugify




class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,


    )

    personal_pet_photo = models.URLField(

    )

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
