from django.db import models

class user(models.Model):


    ROLE_CHOICES=(
        ('STAFF', "staff"),
        ('ADMIN', "System Admin"),
        ('SUPPORT', "IT Support")
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=20, unique=True)

