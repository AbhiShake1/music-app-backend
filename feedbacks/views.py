import pusher
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    from messages_repo import MessagesRepo

    repo = MessagesRepo()

    if request.method == 'POST':
        import json
        post_data: dict = json.loads(request.body.decode())
        post_id = post_data['post_id']
        comment = post_data['comment']
        username = post_data['username']
        rating = post_data['rating']
        message = repo.create(post_id, username, comment, int(rating))
        pusher_client.trigger(post_id, 'feedback', message)
        data = {'post_id': post_id,
                'comment': comment,
                }
        return HttpResponse(json.dumps(data), headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        })
    if request.method == 'GET':
        import json
        messages = repo.get_all()
        return HttpResponse(json.dumps(messages), headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        })
