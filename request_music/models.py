from django.db.models import *


# Create your models here.
class RequestedMusic(Model):
    artist = CharField(max_length=60)
    song_name = CharField(max_length=60)
