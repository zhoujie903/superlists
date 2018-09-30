from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True

class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=40)