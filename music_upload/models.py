from django.db.models import *
from gdstorage.storage import GoogleDriveStorage


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


# Create your models here.


class Music(Model):
    title = CharField(max_length=60, primary_key=True)
    artist = CharField(max_length=60)
    file = FileField(validators=[validate_file_extension],
                     upload_to='music/',
                     storage=GoogleDriveStorage())
