from django.db import models
from datetime import date
import re
# import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['name']) <2:
            errors["name"] = "Name should be greater than two characters"
        if len(postData['address']) <2:
            errors["address"] = "Address should be greater than two characters"
        if len(postData['city']) <2:
            errors["city"] = "City should be greater than two characters"
        if len(postData['state']) == 2:
            errors["state"] = "State should be two characters"
        if len(postData['zip_code']) <5:
            errors["zip_code"] = "Zip Code should be greater than five characters"
        if len(postData['policy_number']) < 5:
            errors["policy_number"] = "Policy Number should be greater than five characters"
        return errors

    def login_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if not check:
            errors['email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), check[0].password.encode()):
                errors['password'] = "Email and password do not match."
        return errors

class Adjuster(models.Manager):
    def appt_validator(self, postData):
        errors = {}
        today = date.today()
        if len(postData['name']) <2:
            errors["name"] = "Name should be greater than two characters" 
        if len(postData['code']) ==0:
            errors['code'] = "Must enter valid code"
        elif (postData['code']) < str(today):
            errors["code"] = "Code should be in the future."
        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    address = models.EmailField(max_length=255)
    city = models.EmailField(max_length=255)
    state = models.EmailField(max_length=255)
    zip_code = models.EmailField(max_length=255)
    policy_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Adjuster(models.Model):
    name = models.CharField(max_length=255)
    code = models.DateField()
    active = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='tasks', null= True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = AppointmentManager()

class Claim(models.Model):
    Policy_number = models.CharField(max_length=255)
    user_name = models.DateField()
    claim_number = models.CharField(max_length=255)
    # user_adj = models.ForeignKey(User, related_name='tasks', null= True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = AppointmentManager()