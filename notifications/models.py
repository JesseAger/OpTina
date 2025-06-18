from django.db import models
# from users.models import CustomUser
from tickets.models import tickets
from django.conf import settings


class notifications(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODELS, on_delete=models.CASCADE)
    ticket = models.ForeignKey(tickets, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)