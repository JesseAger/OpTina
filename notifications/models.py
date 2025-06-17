from django.db import models
from users.models import user
from tickets.models import tickets



class notifications(models.Model):
    staff = models.ForeignKey(user, on_delete=models.CASCADE)
    ticket = models.ForeignKey(tickets, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)