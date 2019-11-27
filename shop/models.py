from django.db import models
from os import path
from uuid import uuid4

SCHOOL_CHOICES = (
    # More about Dutch school system 😉
    # https://www.iamexpat.nl/expat-info/family-kids/types-of-childcare-netherlands
    ("praktijkonderwijs", "praktijkonderwijs"),
    ("vmbo", "vmbo"),
    ("mbo", "mbo"),
    ("opleidingsbedrijf", "opleidingsbedrijf"),
)


def get_image_path(instance, filename):
    """returns a random path of the image"""
    filename, file_extension = path.splitext(filename)
    return path.join(str(uuid4()) + file_extension)


class Category(models.Model):
    title = models.CharField(max_length=256)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=get_image_path)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to=get_image_path)
    categories = models.ManyToManyField(Category)
    school_type = models.CharField(max_length=160, choices=SCHOOL_CHOICES, null=False)
    price = models.FloatField()
    expiration_date = models.DateField(null=False)

    def get_abbreviated_description(self):
        """returns only the first 25 words of the description"""
        word_array = str(self.description).split()[:25]
        abbreviated_description = " ".join(word_array)
        return abbreviated_description

    class Meta:
        ordering = ["-expiration_date", "name"]

    def __str__(self):
        return self.name
