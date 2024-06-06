from django.db import models


# Create your models here.
# user model
class Member(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)


class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    acquired_on = models.DateField()
    customer_status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name