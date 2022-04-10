from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models import *


# Create your models here.
class Post(Model):
    username = ForeignKey(User, on_delete=CASCADE)
    comment = TextField()
    rating = PositiveIntegerField(validators=[MaxValueValidator(5, message='Rating cannot go beyond 5')])
