from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

from core.user_detail_response import get_user_detail_response


# Create your views here.
def recover_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        try:
            import json
            post_data: dict = json.loads(request.body.decode())
            email: str = post_data['email']
            new_password: str = post_data['password']
            user: User = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return get_user_detail_response(user)
        except Exception:
            return HttpResponse(content='Something went wrong', status=401)
    return HttpResponse(status=401)
