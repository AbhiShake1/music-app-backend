import os.path

import textract
from django.conf import settings
from django.http import HttpResponse, HttpRequest
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from music_upload.models import Music


@csrf_exempt
def upload_music(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES['music']:
        import json
        post_data = json.loads(request.body.decode())
        title = post_data['title']
        description = post_data['description']
        artist = post_data['artist']
        file = request.FILES['music']
        music = Music.objects.create(title=title, description=description, artist=artist, file=file)
        return HttpResponse(music.title)
    return HttpResponse(status=401)


@csrf_exempt
def get_music(request: HttpRequest) -> HttpResponse:
    def get_content(file):
        return textract.process(file, method='PDFminer')

    musics = Music.objects.all()
    result: dict = {}
    for music in musics:
        key = str(music.artist)
        detail = {'title': music.title, 'description': music.description, 'content': get_content(music.file.path)}
        if key in result:
            result[key] += detail
        else:
            result[key] = detail
    import json
    return HttpResponse(json.dumps(result))


@csrf_exempt
def delete_music(request: HttpRequest) -> HttpResponse:
    if request.method == 'DELETE':
        import json
        post_data: dict = json.loads(request.body.decode())
        file_name = os.path.join(settings.MUSIC_ROOT, post_data['file_name'])
        if os.path.exists(file_name):
            os.remove(file_name)
            Music.objects.get(artist=post_data[file_name]).delete()
        files = os.listdir(settings.MUSIC_ROOT)
        return HttpResponse(json.dumps(files))
    return HttpResponse(status=401)
