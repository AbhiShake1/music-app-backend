from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from music_upload.models import Music


@csrf_exempt
def upload_music(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES['music']:
        try:
            import json
            post_data = request.POST
            title = post_data['title']
            artist = post_data['artist']
            file = request.FILES['music']
            try:
                music = Music.objects.create(title=title, artist=artist, file=file)
            except:
                return HttpResponse('This song already exists', status=403)
            return HttpResponse(json.dumps({
                'title': music.title,
                'artist': music.artist,
                'url': music.file.url,
            }))
        except Exception as e:
            return HttpResponse(str(e), status=500)
    return HttpResponse(status=401)


@csrf_exempt
def get_music(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        requested_music = json.loads(request.body.decode())['title']
        try:
            m = Music.objects.get(title=requested_music)
        except MultipleObjectsReturned:
            m = Music.objects.get(title=requested_music)[0]
        except:
            return HttpResponse('The requested music does not exist', status=404)
        return HttpResponse(json.dumps({
            'title': m.title,
            'artist': m.artist,
            'url': m.file.url
        }))
    return HttpResponse(status=401)


@csrf_exempt
def get_all_music(request):
    result = []
    music = Music.objects.all()
    for m in music:
        result.append({
            'title': m.title,
            'artist': m.artist,
            'url': m.file.url
        })
    import json
    return HttpResponse(json.dumps(result))


@csrf_exempt
def delete_music(request: HttpRequest) -> HttpResponse:
    if request.method == 'DELETE':
        import json
        post_data: dict = json.loads(request.body.decode())
        Music.objects.get(title=post_data['title']).delete()
        return HttpResponse('deleted')
    return HttpResponse(status=401)
