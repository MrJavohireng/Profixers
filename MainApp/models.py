from django.db import models
from django.contrib.auth.models import User
def upload_avatar(instance:"Profile", filename:str):
    return f"avatars/{instance.pk}) {instance.full_name}/{filename}"

class Profile(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.PROTECT)
    full_name=models.TextField()
    phone_number=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)
    balance=models.DecimalField(max_digits=7, decimal_places=2, default=0)
    avatar=models.ImageField(upload_to=upload_avatar, blank=True, null=True)