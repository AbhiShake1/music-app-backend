from django.http import HttpRequest, HttpResponse
from django.contrib import auth


# Create your views here.
def logout(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponse({'status': 'Successful'})
    return HttpResponse(status=401)
