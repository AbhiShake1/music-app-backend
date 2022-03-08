from django.contrib.auth.models import User
from django.http import HttpResponse


def get_user_detail_response(user: User) -> HttpResponse:
    import json
    data = {
        'userName': user.username,
        'email': user.email,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'dateJoined': str(user.date_joined),
        'isActive': user.is_active,
    }
    return HttpResponse(json.dumps(data), headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    })
