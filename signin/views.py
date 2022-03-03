from typing import Optional

from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from core.user_detail_response import get_user_detail_response


@csrf_exempt
def signin(request: HttpRequest) -> Optional[HttpResponse]:
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode())
        username = post_data['username']
        password = post_data['password']
        user: User = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse(content='Invalid credentials', status=401)
        user.save()
        return get_user_detail_response(user)
    return HttpResponse(status=401)
