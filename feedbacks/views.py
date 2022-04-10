import pusher
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from feedbacks.models import Post

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
        comment = post_data['comment']
        username = User.objects.get(username=post_data['username'])
        rating = post_data['rating']
        message = Post.objects.create(username=username, comment=comment, rating=int(rating))
        data = {
            'post_id': message.id,
            'comment': comment,
        }
        return HttpResponse(json.dumps(data), headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        })
    if request.method == 'GET':
        import json
        messages = Post.objects.all()
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
