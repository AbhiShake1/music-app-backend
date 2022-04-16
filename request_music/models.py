import this

from django.db.models import *


# Create your models here.
class RequestedMusic(Model):
    artist = CharField(max_length=60)
    song_name = CharField(max_length=60)

    def __str__(self):
        return f'{self.artist} {self.song_name}'
