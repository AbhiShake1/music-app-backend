import os.path

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse, HttpRequest
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_music(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES['music']:
        upload: InMemoryUploadedFile = request.FILES['music']
        fss = FileSystemStorage()
        file = fss.save(os.path.join(settings.MUSIC_ROOT, upload.name), upload)
        return HttpResponse(fss.url(file))
    return HttpResponse(status=401)


@csrf_exempt
def get_music(request: HttpRequest) -> HttpResponse:
    files = os.listdir(settings.MUSIC_ROOT)
    import json
    return HttpResponse(json.dumps(files))
