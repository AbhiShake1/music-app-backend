from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models import *


# Create your models here.
class Feedback(Model):
    username = ForeignKey(User, on_delete=CASCADE)
    issues = TextField()
    description = TextField()
    screenshot = FileField()
