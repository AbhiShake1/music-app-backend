import pusher
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from feedbacks.models import Feedback

pusher_client = pusher.Pusher(
    app_id='1363891',
    key='6c72a292bcf1d2ca2eb6',
    secret='079a81394ef64fb65c14',
    cluster='ap2',
    ssl=True
)


# Create your views here.
@csrf_exempt
def post_detail(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        post_data: dict = json.loads(request.body.decode())
        issues = post_data['issues']
        username = User.objects.get(username=post_data['username'])
        description = post_data['description']
        message = Feedback.objects.create(username=username, issues=issues, description=description)
        data = {
            'post_id': message.id,
            'issues': issues,
        }
        return HttpResponse(json.dumps(data), headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        })
    if request.method == 'GET':
        import json
        messages = Feedback.objects.all()
        result: dict = {}
        for message in messages:
            key = str(message.username)
            if key in result:
                result[key] += message.comment
            else:
                result[key] = [message.comment]
        return HttpResponse(json.dumps(result, default=str), headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        })
