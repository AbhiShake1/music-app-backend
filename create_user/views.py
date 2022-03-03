from typing import Optional

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, Http404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from core.user_detail_response import get_user_detail_response


@csrf_exempt
def create_user(request: HttpRequest) -> Optional[HttpResponse]:
    if request.method == 'POST':
        import json
        post_data: dict = json.loads(request.body.decode())
        try:
            username = post_data['username']
            email = post_data['email']
            password = post_data['password']
            first_name = post_data.get('first_name')
            last_name = post_data.get('last_name')
            user: User = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return get_user_detail_response(user)
        except Exception:
            return HttpResponse(content='User already exists', status=401)
    return HttpResponse(status=401)
