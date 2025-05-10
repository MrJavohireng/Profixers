from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.PROTECT)
    full_name=models.TextField()
    phone_number=models.CharField(max_length=100)
    balance=models.DecimalField(decimal_places=2, max_digits=8)
    def __str__(self):
        return f"{self.pk}) {self.full_name}"

class Offer(models.Model):
    user=models.ForeignKey(to=Profile, on_delete=models.PROTECT)
    name=models.TextField()
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.pk}) {self.name}-{self.price}"
    
class Order(models.Model):
    user=models.ForeignKey(to=Profile, on_delete=models.PROTECT)
    order=models.ForeignKey(to=Offer, on_delete=models.PROTECT)
    status=models.TextField()
    def __str__(self):
        return f"{self.pk}) {self.user.full_name}-{self.order.name}"