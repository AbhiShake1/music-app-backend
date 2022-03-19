from django.http import HttpRequest, HttpResponse
from django.contrib import auth


# Create your views here.
def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return HttpResponse({'status': 'Successful'})
