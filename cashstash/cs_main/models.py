from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Ipon(models.Model):
    fld_ipon_id = models.AutoField(primary_key=True)
    fld_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fld_ipon = models.DecimalField(decimal_places=2, max_digits=9)
    fld_ipon_desc = models.TextField()
    fld_title = models.CharField(default='', max_length=50)

class Money(models.Model):
    types = (
        ('a','add'),
        ('m','minus')
    )

    fld_money_id = models.AutoField(primary_key=True)
    fld_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fld_value = models.DecimalField(decimal_places=2, max_digits=9)
    fld_description = models.TextField(default='')
    fld_type = models.CharField(choices=types, max_length=5)
    fld_date_added = models.DateTimeField(auto_now=True)
    fld_title = models.CharField(default='', max_length=50)
