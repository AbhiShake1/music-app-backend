from django.contrib.auth.models import User
from django.http import HttpResponse


def get_user_detail_response(user: User) -> HttpResponse:
    import json
    data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_joined': str(user.date_joined),
        'is_active': user.is_active,
    }
    return HttpResponse(json.dumps(data))