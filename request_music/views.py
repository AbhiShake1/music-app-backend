# Create your views here.
from django.http import HttpResponse

from request_music.models import RequestedMusic


def request_music(request):
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode())
        artist = post_data['artis']
        song_name = post_data['song_name']
        RequestedMusic.objects.create(artist=artist, song_name=song_name)
        return HttpResponse('Successful')
    return HttpResponse('Bad Request. Only POST allowed', status=401)
