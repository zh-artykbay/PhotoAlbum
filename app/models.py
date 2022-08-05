from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator


class Album(models.Model):
    name = models.CharField(max_length=1024)
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    created = models.DateField(auto_now_add=True)
    tags = TaggableManager()

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    image = models.ImageField(upload_to="photo/", validators=[validate_image, FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])])

    def __str__(self):
        return self.name
