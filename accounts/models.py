from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

def validate_date(d):
    if datetime.date < d :
        raise ValidationError("Enter Valid Date of Birth")
    else:
        return d


class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField()
    tel=PhoneNumberField(region="IN")