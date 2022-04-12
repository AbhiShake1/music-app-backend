from django.http import HttpResponse

# Create your views here.
from notifications.models import Notification


def get_notifications(request):
    notifications = Notification.objects.all()
    result = []
    for notification in notifications:
        result.append({str(notification.title): notification.description})
    import json
    return HttpResponse(json.dumps(result, default=str))
