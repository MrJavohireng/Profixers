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
    def __str__(self):
        return f"{self.pk}) {self.full_name}.({self.user.username})"
    
class WorkDays(models.Model):
    work_day_choices=[("Mon","Понедельник"),("Tue","Вторник"),("Wen","Среда"),("Thu","Четверг"),("Fri","Пятница"),("Sat","Суббота"),("Sun","Воскресенье")]
    name=models.CharField(max_length=15, unique=True, choices=work_day_choices)
    def __str__(self):
        return f"{self.pk}) {self.name}"
    
class Services(models.Model):
    user=models.ForeignKey(to=Profile, on_delete=models.PROTECT)
    name=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(max_digits=7, decimal_places=2)
    active_days=models.ManyToManyField(to=WorkDays)
    rating=models.DecimalField(max_digits=2,decimal_places=1, default=0)
    
    
    
# status_choices=[("accepted","Принята"),("process","В процессе")]
# status=models.CharField(choices=status_choices, max_length=25, default="process")
    
class Basket(models.Model):
    user=models.ForeignKey(to=Profile, on_delete=models.PROTECT)
    services=models.ManyToManyField(to=Services)
    def __str__(self):
        return f"{self.pk}) {self.user.full_name}'s basket"

class Order(models.Model):
    pay_choices=[("card_online","Картой онлайн"), ("money","Наличными при визите"), ("card_offline", "Картой при визите")]
    basket=models.ForeignKey(to=Basket, on_delete=models.PROTECT)
    city=models.CharField(max_length=200)
    street=models.CharField(max_length=200)
    house=models.CharField(max_length=200)
    apartment=models.CharField(max_length=200)
    comment_house=models.TextField()
    date=models.DateTimeField()
    pay_type=models.CharField(choices=pay_choices, max_length=50)
    comment=models.TextField()
    def __str__(self):
        return f"{self.pk}) {self.basket.user.full_name}-{self.city}:{self.street}-{self.date}"